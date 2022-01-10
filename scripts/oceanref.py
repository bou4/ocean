import re

from bs4 import BeautifulSoup

# Current tag
tag = None


def parse_chapter(index):
    """Parse chapter."""
    global tag

    # Open the corresponding chapter of the Ocean reference manual
    file = open(f'../docs/oceanref/chap{index}.html')

    # Read file
    content = file.read()

    # Replace some HTML entities before parsing it with Beautiful Soup
    content = content.replace('&#8217;', '\'')
    content = content.replace('&#8216;', '\'')
    content = content.replace('&#8230;', '...')

    # Parse the file using BeautifulSoup4
    tag = BeautifulSoup(content, 'html5lib')

    # Remove all useless anchors
    for pgfId in tag.find_all('a', attrs={'name': re.compile('pgfId-\d+')}):
        pgfId.decompose()

    for marker in tag.find_all('a', attrs={'name': re.compile('marker-\d+')}):
        marker.decompose()

    # Replace all code tags
    for code in tag.find_all('code'):
        code.unwrap()

    # Parse content
    return parse_content()


def parse_content():
    """Parse content in the chapter."""
    global tag

    # Find main content, and eat it
    tag = tag.find('div', id='main-content')
    tag = tag.contents[0]

    functions = []

    # Parse functions
    while function := parse_function():
        functions.append(function)

    return functions


def parse_function():
    """Parse function in the content."""
    global tag

    # Find function
    tag = tag.find_next('h3')

    name = ''

    if tag:
        name = tag.get_text(strip=True)
    else:
        return None

    # Parse description
    description = parse_description()

    # Parse arguments
    arguments = parse_arguments()

    # Parse return values
    return_values = parse_return_values()

    return {'name': name, 'description': description, 'arguments': arguments, 'return_values': return_values}


def parse_description():
    """Parse description in the function."""
    global tag

    # Find description
    tag = tag.find_next('h4')
    tag = tag.find_next()

    # This give erroneous results if get_text(strip=True) is used
    return tag.text.lstrip().rstrip()


def parse_arguments():
    """Parse arguments in the function."""
    global tag

    # Find arguments
    tag = tag.find_next('h4')
    tag = tag.find_next()

    # Parse arguments
    arguments = []

    if tag.name == 'table':
        # Remember where we where
        temp = tag

        # Move the tag to the first row
        tag = tag.find('tr')

        while argument := parse_argument():
            arguments.append(argument)

        # Restore we where
        tag = temp

    return arguments


def parse_argument():
    """Parse argument in the arguments."""
    global tag

    if tag is not None:
        # Get all columns
        td = tag.find_all('td')

        # The first column is always the name
        td_name = td[0]

        # The second column might not exist...
        td_description = None

        if len(td) == 2:
            td_description = td[1]
        else:
            # ..., if this happens, move the tag to the next row
            tag = tag.find_next_sibling('tr')
            # and select the second column
            td_description = tag.find_all('td')[1]

        # Extract the text from the respective columns
        name = td_name.text.lstrip().rstrip()
        description = td_description.text.lstrip().rstrip()

        # Move the tag to the next row
        tag = tag.find_next_sibling('tr')

        return {'name': name, 'description': description}

    return None


def parse_return_values():
    """Parse return values in the function."""
    global tag

    # Find returns
    tag = tag.find_next('h4')
    tag = tag.find_next()

    # Parse returns
    return_values = []

    if tag.name == 'table':
        # Remember where we where
        temp = tag

        # Move the tag to the first row
        tag = tag.find('tr')

        while return_value := parse_return_value():
            return_values.append(return_value)

        # Restore we where
        tag = temp

    return return_values


def parse_return_value():
    """Parse return value in the return values."""
    global tag

    if tag is not None:
        # Get all columns
        td = tag.find_all('td')

        # The first column is always the name
        td_name = td[0]

        # The second column might not exist...
        td_description = None

        if len(td) == 2:
            td_description = td[1]
        else:
            # ..., if this happens, move the tag to the next row
            tag = tag.find_next_sibling('tr')
            # and select the second column
            td_description = tag.find_all('td')[1]

        # Extract the text from the respective columns
        name = td_name.text.lstrip().rstrip()
        description = td_description.text.lstrip().rstrip()

        # Move the tag to the next row
        tag = tag.find_next_sibling('tr')

        return {'name': name, 'description': description}

    return None


def generate_python(filename, functions):
    template = '''def {name}():
    """{docstring}
    """
    raise NotImplementedError


'''

    file = open(filename, 'wb')

    for function in functions:
        file.write(template.format(
            name=function_name(function['name']),
            docstring=generate_docstring(function)).encode('utf-8'))


pattern = re.compile(r'(?<!^)(?=[A-Z])')


def function_name(name):
    """Convert a function name to python syntax"""
    return pattern.sub('_', name).lower()


def argument_name(name):
    """Convert an argument name to python syntax"""
    name = name.split()

    if len(name) == 1:
        name = name[0]

        # Strip type identifier
        if re.match('^[a-z]_', name):
            name = name[2:]
    elif len(name) == 2:
        # Strip ?
        name = name[0][1:]
    elif len(name) == 3:
        # Nothing to strip, this is a bug
        name = name[1]
    else:
        name = '(' + ' '.join(name[1:-1]) + ')'

    return pattern.sub('_', name).lower()


def indent(x):
    """Return spaces for number of indents"""
    return '    ' * x


def generate_docstring(function):
    """Generate docstring for a function"""
    docstring = ''

    description = function['description'].split('.')
    # Remove empty elements
    description = [x for x in description if x]

    for i, s in enumerate(description):
        docstring += s.lstrip().rstrip() + '.\n'

        if i == 0 or i == len(description) - 1:
            docstring += '\n'

        docstring += indent(1)

    if function['arguments']:
        docstring += 'Args:\n'
        docstring += indent(2)

    for i, s in enumerate(function['arguments']):
        description = s['description'].split('.')
        # Remove empty elements
        description = [x for x in description if x]

        if len(description) == 1:
            docstring += argument_name(s['name']) + \
                ': ' + description[0] + '\n'
            docstring += indent(2)
        else:
            docstring += argument_name(s['name']) + ':\n'
            docstring += indent(3)

            for j, s in enumerate(description):
                docstring += s.lstrip().rstrip() + '.\n'

                if j == len(description) - 1:
                    docstring += indent(2)
                else:
                    docstring += indent(3)

        if i == len(function['arguments']) - 1:
            docstring += '\n'
            docstring += indent(1)

    if function['return_values']:
        docstring += 'Returns:\n'
        docstring += indent(2)

    for i, s in enumerate(function['return_values']):
        description = s['description'].split('.')
        # Remove empty elements
        description = [x for x in description if x]

        if len(description) == 1:
            docstring += argument_name(s['name']) + \
                ': ' + description[0] + '\n'
            docstring += indent(2)
        else:
            docstring += argument_name(s['name']) + ':\n'
            docstring += indent(3)

            for j, s in enumerate(description):
                docstring += s.lstrip().rstrip() + '.\n'

                if j == len(description) - 1:
                    docstring += indent(2)
                else:
                    docstring += indent(3)

        if i == len(function['return_values']) - 1:
            docstring += '\n'
            docstring += indent(1)

    return docstring.rstrip()


generate_python('../src/ocean/environment.py', parse_chapter(5))
generate_python('../src/ocean/simulation.py', parse_chapter(6))
generate_python('../src/ocean/data_access.py', parse_chapter(7))
generate_python('../src/ocean/calculator.py', parse_chapter(10))
generate_python('../src/ocean/parametric_analysis.py', parse_chapter(11))
generate_python('../src/ocean/distributed_processing.py', parse_chapter(12))

def append_path():
    """Appends a new path to the end of the search path list.

    You can append as many paths as you want with this command.

    Args:
        dir_name1: Directory path
        dir_name_n: Additional directory paths

    Returns:
        dir_name_n: Returns the last path specified
        nil: Returns nil and prints an error message if the paths cannot be appended
    """
    raise NotImplementedError


def path():
    """Sets the search path for included files.

    Args:
        dir_name1: Directory path
        dir_name_n: Additional directory path

    Returns:
        path_list: Returns the entire list of search paths specified
        nil: Returns nil and prints an error message if the paths cannot be set
    """
    raise NotImplementedError


def prepend_path():
    """Adds a new path to the beginning of the search path list.

    You can add as many paths as you want with this command.

    Args:
        dir_name1: Directory path
        dir_name_n: Additional directory path

    Returns:
        undefined: The return value for this command/function is undefined
        nil: Returns nil and prints an error message if the paths cannot be added
    """
    raise NotImplementedError


def setup():
    """Specifies default values for parameters.

    Returns:
        t: Returns t if the value is assigned to the name
        nil: Returns nil if there is a problem
    """
    raise NotImplementedError


def history():
    """Displays the command history.

    By default, it prints the last 20 commands from the current session and the most recently terminated session.
    More commands can be printed by giving a number as an argument.

    Args:
        number:
            The number of previously entered commands to be listed.
            Default value: 20.

    Returns:
        t: Returns t to indicate that the commands from history have been listed
    """
    raise NotImplementedError


def ocn_set_silent_mode():
    """Filters out OCEAN warning and information  messages and allows only error messages to be written.

    This functionality is useful while running the OCEAN scripts when you might want to skip all OCEAN messages except errors.

    Args:
        silent_mode:
            Accepts boolean values t or nil.
            Set to t to suppress the OCEAN warning and information messages.
            Set to nil to allow all OCEAN messages to be displayed.

    Returns:
        t: Returns t to indicate the successful assignment of the passed argument
    """
    raise NotImplementedError

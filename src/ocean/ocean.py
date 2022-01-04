"""
Python interface to the Open Command Environment for Analysis (OCEAN).

OCEAN lets you set up, simulate, and analyze circuit data without starting
Virtuoso Analog Design Environment L, XL or GXL.
"""
from skillbridge import Workspace, Symbol
from enum import Enum

# TODO: Make the user configure the workspace
ws = Workspace.open()


class _SymbolEnum(Enum):
    def __repr_skill__(self):
        return self.value.__repr_skill__()

# ------------------------------------------------------------------------------
# 1. OCEAN Environment Commands
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# 2. Simulation commands
# ------------------------------------------------------------------------------


class Simulator(_SymbolEnum):
    """Simulator."""
    ADSsim = Symbol('ADSsim')
    ams = Symbol('ams')
    hspiceD = Symbol('hspiceD')
    spectre = Symbol('spectre')
    UltraSim = Symbol('UltraSim')


class Mode(_SymbolEnum):
    """Mode."""
    read = Symbol('r')
    write = Symbol('w')
    append = Symbol('a')


class Category(_SymbolEnum):
    """Category."""
    analog = Symbol('analog')
    digital = Symbol('digital')


class SaveType(_SymbolEnum):
    """Save Types."""
    v = Symbol('v')
    i = Symbol('i')
    all = Symbol('all')
    allv = Symbol('allv')
    alli = Symbol('alli')


def simulator(sim: Simulator) -> Simulator:
    """Starts an OCEAN session and sets the simulator name for that session.

    The previous session (if any) is closed and all session information is cleared.

    Args:
        sim: Name of the simulator.

    Returns:
        Name of the simulator.
    """
    return Simulator(ws['simulator'](sim))


def design(*args, **kwargs):
    """Refer to the documentation of :func:`design_netlist()` and :func:`design_name()`.
    """
    if len(args) == 1:
        return design_netlist(*args)
    elif len(args) == 3:
        return design_name(*args, **kwargs)

    raise TypeError()


def design_netlist(file: str) -> str:
    """Specifies the directory path to the netlist of a design to be simulated.

    Args:
        file:
            Directory path to the netlist followed by the name of the netlist file.
            Name of the netlist file must be `netlist`.
            The `netlistHeader` and `netlistFooter` files must be in the same directory.
            Otherwise, `file` is a pre-existing netlist file from another source.

    Returns:
        Name of the design if successful.
    """
    return ws['design'](file)


def design_name(lib: str, cell: str, view: str, mode: Mode = Mode.append) -> tuple[Symbol, Symbol, Symbol]:
    """Specifies the name of a design to be simulated.

    You can specify the mode using any member of :class:`Mode` in which the design should be opened.

    Args:
        lib: Name of the library that contains the design.
        cell: Name of the design.
        view: View of the design (typically `schematic`).
        mode:
            The mode in which the design should be opened.
            The value can be any member of :class:`Mode`.
            The default mode is :attr:`Mode.append`.
            Read-only designs can be netlisted only by direct netlisters, and not socket.
            The :attr:`Mode.write` mode should not be used as it overwrites the design.

    Returns:
        Name of the view for an Virtuoso Analog Design Environment design if successful.
    """
    ret = ws['design'](lib, cell, view, mode)

    return tuple(ret)


def model_file(*model_files: str | tuple[str, str] | list[str | tuple[str, str]]) -> list[tuple[str, str]]:
    """Specifies model files to be included in the simulator input file.

    This command returns the model files used.
    When model files are specified through the arguments, the model files are set accordingly.
    Use of full paths for the model file is recommended.

    Args:
        model_files:
            Can be a string to specify the name of the model file.
            Can also be a tuple of two strings to specify the name of the model file and the name of the section.
            Can also be a list of either of the above.

    Returns:
        A list of all model file/section pairs.
    """
    return [tuple(i) for i in ws['modelFile'](*model_files)]


def des_var(vars: dict = None) -> str | dict:
    """Sets the values of design variables used in your design.

    You can set the values for as many design variables as you want.

    Args:
        vars:
            Dictionary containing the name/value pairs of the design variables.

    Returns:
        If no argument is passed, the current design variables are returned as a dictionary, else, the value of the last set variable is returned.
    """
    if vars is None:
        ret = ws['desVar']()

        if ret:
            return {y[0]: y[1] for y in ret}
        else:
            return {}
    else:
        x = [None] * (2 * len(vars))
        x[0:: 2] = vars.keys()
        x[1:: 2] = vars.values()
        return ws['desVar'](*x)


def save(save_type: SaveType = None, names: list[str] = None, category: Category = None) -> None:
    """Specifies the outputs to be saved and printed during simulation.

    When specifying particular outputs with saveName, you can include as many outputs as you
    want. If you want to turn off the default of save, `allv, use the delete(`save )
    command.

    Arguments:
        save_type:
            Type of outputs to be saved.
            The value can be any member of :class:`SaveType`.
            The default save type is :attr:`SaveType.allv`.
        names:
            List of nets, devices or other objects.
        category:
            Type of simulator to be used.
            The value can be any member of :class:`Category`.
            The default category is :attr:`Category.analog`.
    
    Returns:
        TODO
    """
    class Keyword:
        def __init__(self, name: str) -> None:
            self.name = name

        def __repr_skill__(self) -> str:
            return f'?{self.name}'

    args = []

    if category is not None:
        args.append(Keyword('categ'))
        args.append(category)

    if save_type is not None:
        args.append(save_type)

    if names is not None:
        args += names

    return ws['save'](*args)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

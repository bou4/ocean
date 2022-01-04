"""
Python interface to the Open Command Environment for Analysis (OCEAN).

OCEAN lets you set up, simulate, and analyze circuit data without starting
Virtuoso Analog Design Environment L, XL or GXL.
"""
from skillbridge import Workspace, Symbol, Key, Var
from enum import Enum

# TODO: Make the user configure the workspace
ws = Workspace.open()
ws['load']('abWaveToList.il')


class _SymbolEnum(Enum):
    def __repr_skill__(self):
        return self.value.__repr_skill__()


class Waveform:
    """Waveform."""
    def __init__(self, waveform) -> None:
        self.waveform = waveform

    def __add__(self, other: 'Waveform') -> 'Waveform':
        return Waveform(ws['plus'](self.waveform, other.waveform))

    def __sub__(self, other: 'Waveform') -> 'Waveform':
        return Waveform(ws['plus'](self.waveform, ws['minus'](other.waveform)))

    def pull(self) -> tuple[list[float], list[float]]:
        """Pull the waveform for further processing in the local environment.

        Args:
            waveform: The waveform to pull.

        Returns:
            Tuple containing the x and y values of the waveform.
        """
        x, y = ws['abWaveToList'](self.waveform, transpose=True)

        return x, y


# ------------------------------------------------------------------------------
# 1. OCEAN Environment Commands
# The following OCEAN environment commands let you start, control, and quit the OCEAN environment.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# 2. Simulation commands
#
# The following OCEAN simulation commands let you set up and run your simulation.
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


class AnalysisType(_SymbolEnum):
    """Analysis Types."""
    pz = Symbol('pz')
    lf = Symbol('lf')
    acmatch = Symbol('acmatch')
    dcmatch = Symbol('dcmatch')
    stb = Symbol('stb')
    tran = Symbol('tran')
    envlp = Symbol('envlp')
    ac = Symbol('ac')
    dc = Symbol('dc')
    noise = Symbol('noise')
    xf = Symbol('xf')
    sp = Symbol('sp')
    pss = Symbol('pss')
    pac = Symbol('pac')
    pstb = Symbol('pstb')
    pnoise = Symbol('pnoise')
    pxf = Symbol('pxf')
    psp = Symbol('psp')
    qpss = Symbol('qpss')
    qpac = Symbol('qpac')
    qpnoise = Symbol('qpnoise')
    qpxf = Symbol('qpxf')
    qpsp = Symbol('qpsp')
    hb = Symbol('hb')
    hbac = Symbol('hbac')
    hbstb = Symbol('hbstb')
    hbnoise = Symbol('hbnoise')
    hbxf = Symbol('hbxf')
    hbsp = Symbol('hbsp')
    sens = Symbol('sens')
    include = Symbol('include')
    gnt = Symbol('gnt')
    custom = Symbol('custom')


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

    Args:
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
        TODO: Write the 'Returns' part of the save function documentation.
    """
    args = []

    if category is not None:
        args.append(Key('categ'))
        args.append(category)

    if save_type is not None:
        args.append(save_type)

    if names is not None:
        args += names

    ret = ws['save'](*args)

    if isinstance(ret, list):
        if all(isinstance(x, Symbol) for x in ret):
            return [SaveType(x) for x in ret]
    else:
        if isinstance(ret, Symbol):
            return SaveType(ret)

    return ret


def analysis(analysis_type: AnalysisType, **kwargs) -> None:
    """Specifies the analysis to be simulated.

    You can include as many analysis options as you want.
    Analysis options vary, depending on the simulator you are using.
    To include an analysis option, include the corresponding keyword argument.
    If you have an AC analysis, the first option/value pair might be `from=0`.

    Note: Some simplified commands are available for basic SPICE analyses.
    See the :func:`ac`, :func:`dc`, :func:`tran`, and :func:`noise` functions.

    TODO: Implement ac, dc, tran, and noise functions.

    Args:
        analysis_type:
            Type of the analysis.
            The value can be any member of :class:`AnalysisType`, but not all members can be used with any simulator.
        **kwargs: Analysis options.
    """
    return ws['analysis'](analysis_type, **kwargs)


def run() -> None:
    """TODO: Extend run
    """
    return ws['run']()


# ------------------------------------------------------------------------------
# 3. Data Access Commands
#
# The data access commands let you open results and select different types of results to analyze.
# You can get the names and values of signals and components in the selected results, and you can print different types of reports.
# ------------------------------------------------------------------------------

def select_result(results_name: AnalysisType, sweep_value: float | int = None) -> None:
    """Selects the results from a particular analysis whose data you want to examine.

    The argument that you supply to this command is a data type representing the particular type of analysis results you want.
    All subsequent data access commands use the information specified with :func:`select_result`.

    Args:
        results_name: Results from an analysis.
        sweep_value: The sweep value you wish to select for an analysis.

    Returns:
        The object representing the selected results.
    """
    if sweep_value is None:
        return ws['selectResult'](results_name)
    else:
        return ws['selectResult'](results_name, sweep_value)


def get_data(name: str, result_name: AnalysisType = None, results_directory: str = None) -> float | Waveform:
    """Returns the number or waveform for the signal name specified.

    The type of value returned depends on how the command is used.

    Args:
        name: Name of the signal.
        result_name:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by :func:`select_result`.
            The default is the current result selected with :func:`select_result`.
        results_directory:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the `result_name` argument.
            When specified, this argument will only be used internally and will not alter the current results directory which was set by :func:`open_results`.
            The default is the current results directory set by :func:`open_results`.
    Returns:
        The integer simulation result or a waveform object.
        A waveform object represents simulation results that can be displayed as a series of points on a grid.

    TODO: Implement open_results().
    """
    args = [name]

    if result_name is not None:
        args.append(result_name)

        if results_directory is not None:
            args.append(results_directory)

    ret = ws['getData'](*args)

    # An error has occurred
    if ret is None:
        raise ValueError()

    # TODO: Check if getData() ever returns an integer
    if isinstance(ret, float):
        return ret
    else:
        return Waveform(ret)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

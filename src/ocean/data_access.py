from ocean.workspace import ws
from ocean.waveform import *
from ocean.family import *
from ocean.symbol import *


def data_types():
    """Returns the list of data types that are used in an analysis previously specified with selectResult.

    Returns:
        data_types: Returns the list of data types
        nil: Returns nil and an error message if the list of datatypes cannot be returned
    """
    raise NotImplementedError


def delete_subckt():
    """Deletes the specified subcircuit instance saved using the saveSubckt command.

    Args:
        name: The name of the subcircuit instance

    Returns:
        t: Returns t if the selected subcircuit instances is deleted
        nil: Returns nil if the name of the specified instance is not correct
    """
    raise NotImplementedError


def display_subckt():
    """Prints the subcircuit information to the output file.

    Args:
        args: The value of this argument should always be nil
        out_port:
            The name of the file to save the subcircuit information.
            If you do not specify the location with the filename, the file is saved in the current working directory.

    Returns:
        t: Returns t if the subcircuit information is printed in the specified output file
        nil: Returns nil if the name of the output file is not specified, or an error occurred
    """
    raise NotImplementedError


def get_data(name: str, result_name: AnalysisType = None, results_directory: str = None) -> float | Family | RemoteWaveform:
    """Returns the number or waveform for the signal name specified.

    The type of value returned depends on how the command is used.

    Args:
        name (str): Name of the signal
        result_name (AnalysisType, optional):
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by the :func:`select_result()` command.
            The default is the current result selected with the :func:`select_result()` command.
        results_dir (str, optional):
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the `result_name` argument.
            When specified, this argument will only be used internally and will not alter the current results directory which was set by the :func:`open_results()` command.
            The default is the current results directory set by the :func:`open_results()` command.

    Returns:
        float | RemoteWaveform: 
            An integer simulation result or a :obj:`RemoteWaveform` object.
            A :obj:`RemoteWaveform` object represents simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.).

    Raises:
        ValueError: The value cannot be returned.
    """
    args = [name]

    if result_name is not None:
        args.append(result_name)

        if results_directory is not None:
            args.append(results_directory)

    ret = ws['getData'](*args)

    if ret is None:
        raise ValueError('The value cannot be returned.')

    if isinstance(ret, float):
        return ret
    elif fam_is_family(ret):
        return Family(ret)
    else:
        return RemoteWaveform(ret)


def get_result():
    """Gets the data object for a specified analysis without overriding the status of any previously executed selectResult() or openResults() commands.

    Args:
        result_name:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by the selectResult command.
            The default is the current result selected with the selectResult command.
        results_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the resultName argument.
            When specified, this argument will only be used internally and will not alter the current results directory which was set by the openResults command.
            The default is the current results directory set by the openResults command.

    Returns:
        results: Returns the object representing the selected results
        nil: Returns nil and an error message if there are problems accessing the analysis
    """
    raise NotImplementedError


def i():
    """Returns the current through the specified component.

    Args:
        component: Name of the component
        result_name:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by the selectResult command.
            The default is the current result selected with the selectResult command.
        results_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the resultName argument.
            When specified, this argument will only be used internally and will not alter the current results directory which was set by the openResults command.
            The default is the current results directory set by the openResults command.

    Returns:
        waveform:
            Returns a waveform object.
            A waveform object represents simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        nil: Returns an error message and nil if there is a problem
    """
    raise NotImplementedError


def ocn_help():
    """Provides online help for the specified command.

    Args:
        filename:
            File in which to write the information.
            The ocnHelp command opens the file, writes to the file, and closes the file.
            If you specify the filename without a path, the ocnHelp command creates the file in the directory pointed to by your SKILL Path.
            To find out what your SKILL path is, type getSkillPath() at the OCEAN prompt.
        port:
            Port (previously opened with outfile) through which to append the information to a file.
            You are responsible for closing the port.
            See the outfile command for more information.
        command: Command for which you want help

    Returns:
        t: Displays the online help and returns t
        nil: Returns nil and an error message if help cannot be displayed
    """
    raise NotImplementedError


def ocn_reset_results():
    """Unsets the results opened by the openResults command.

    Use this command to return to the state that existed prior to using the openResults command.

    Returns:
        t: Resets the results and returns t
    """
    raise NotImplementedError


def open_results(arg: str | Symbol | AnalysisType = None, enable_calc_expressions: bool = None) -> str:
    """Refer to the documentation of :func:`open_job()`, and :func:`open_dir()`.

    All function signatures can be used when calling :func:`open_results()`.

    Raises:
        TypeError: The wrong function signature is used.
    """
    if arg is None:
        ret = open_query()
    if isinstance(arg, Symbol) or isinstance(arg, AnalysisType):
        ret = open_job(arg)
    elif isinstance(arg, str):
        ret = open_dir(arg, enable_calc_expressions)
    else:
        raise TypeError('The wrong function signature is used.')

    return ret


def open_query() -> str:
    """Queries the directory for the results that are currently open.

    Returns:
        str: The directory for the results that are currently open.

    Raises:
        ValueError: There are problems opening the results.
    """
    ret = ws['openResults']()

    if ret is None:
        raise ValueError('There are problems opening the results.')

    return ret


def open_job(job_name: Symbol) -> str:
    """Opens the results from a specified job.

    A job name is defined when a :func:`run()` is issued.

    Args:
        job_name (Symbol):
            The name of a distributed process job.
            `job_name` is a job name and is defined when a run command is issued.

    Returns:
        str: The directory containing the PSF files.

    Raises:
        ValueError: There are problems opening the results.
    """
    ret = ws['openResults'](job_name)

    if ret is None:
        raise ValueError('There are problems opening the results.')

    return ret


def open_dir(dir_name: str, enable_calc_expressions: bool = True) -> str:
    """Opens simulation results stored in PSF files.

    The results must have been created by a previous simulation run through OCEAN or the Virtuoso® Analog Design Environment.
    The directory must contain a file called `logFile` and might contain a file called `runObjFile`.
    When you perform tasks in the design environment, the `runObjFile` is created.
    Otherwise, only `logFile` is created.

    Args:
        dir_name (str): The directory containing the PSF files
        enable_calc_expressions (bool, optional):
            An optional argument, which when set to True, allows the evaluation of Calculator expressions.
            For this argument to work, the directory mentioned in `dir_name` must be a psf directory and must contain `runObjFile`.
            The default value for this argument is True.

    Returns:
        str: The directory containing the PSF files

    Raises:
        ValueError: There are problems opening the results.
    """
    ret = ws['openResults'](dir_name, enable_calc_expressions)

    if ret is None:
        raise ValueError('There are problems opening the results.')

    return ret


def output_params():
    """Returns the list of output parameters for the specified component.

    Args:
        comp_type: Name of a component
        result:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by the selectResult command.
            The default is the current result selected with the selectResult command.
        results_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the resultName argument.
            When specified, this argument will only be used internally and will not alter the current results directory which was set by the openResults command.
            The default is the current results directory set by the openResults command.

    Returns:
        output_params: Returns the list of parameters
        nil: Returns nil and an error message if there are no associated parameters or if the specified component (compType) does not exist
    """
    raise NotImplementedError


def outputs():
    """Returns the names of the outputs whose results are stored for an analysis.

    You can plot these outputs or use them in calculations.

    Args:
        result:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by the selectResult command.
            The default is the current result selected with the selectResult command.
        result_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the resultName argument.
            When specified, this argument will only be used internally and will not alter the current results directory which was set by the openResults command.
            The default is the current results directory set by the openResults command.
        type: Data type of the signal

    Returns:
        outputs: Returns the list of outputs
        nil: Returns nil and an error message if there are problems returning the names of the stored outputs
    """
    raise NotImplementedError


def phase_noise():
    """Returns the phase noise waveform which is calculated using information from two PSF data files.

    Args:
        harmonic: List of harmonic frequencies
        result:
            Name of the result that stores the signal waveform.
            Use the results() command to obtain the list results.
        results_dir:
            Name of the result that stores the "positive output signal" and "negative output signal" noise waveforms.
            When specified, this argument will only be used internally and will not alter the current result which was set by the selectResult command.
            The default is the current result selected with the selectResult command.
        results_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the S_noiseResultName argument.
            Both the S_signalResultName and S_noiseResultName arguments are read from this directory.
            When specified, this argument will only be used internally and will not alter the current results directory which was set by the openResults command.
            The default is the current results directory set by the openResults command.

    Returns:
        waveform: Waveform representing the phase noise
        nil: Returns nil if there is an error
    """
    raise NotImplementedError


def pv():
    """Returns the value of the specified component parameter.

    You can use the outputParams command to get the list of parameters for a particular component.

    Args:
        name: Name of the node or component
        param: Name of the parameter
        result:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result that was set using the selectResult command.
            The default is the current result selected using the selectResult command.
            To get the correct value of the variables while running parametric analysis, use the designParamVals value for the resultName argument.
        results_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the resultName argument.
            When specified, this argument will only be used internally and will not alter the current results directory that was set using the openResults command.
            The default is the current results directory set using the openResults command.

    Returns:
        value: Returns the requested parameter value
        nil: Returns nil and prints an error message
    """
    raise NotImplementedError


def result_param():
    """Returns the value of a header property from the selected result data.

    Args:
        property_name: Name of the parameter
        result:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by the selectResult command.
            The default is the current result selected with the selectResult command.
        results_dir:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by the selectResult command.
            The default is the current result selected with the selectResult command.

    Returns:
        l_value:
            Value of the parameter.
            The data type depends on the data type of the parameter.
        nil: Returns nil and an error message if there are problems returning the results
    """
    raise NotImplementedError


def results():
    """Returns a list of the type of results that can be selected.

    Args:
        results_dir:
            Directory containing the PSF files (results).
            When specified, this argument will only be used internally and will not alter the current results directory which was set by the openResults command.
            The default is the current results directory set by the openResults command.

    Returns:
        results: Returns the list of result types
        nil: Returns nil and an error message if there are problems returning the results
    """
    raise NotImplementedError


def save_subckt():
    """Saves and modifies the specified subcircuit instances and signals.

    Args:
        name: The name of the subcircuit instance
        voltage: Specifies whether you want to save the voltage for the subcircuit
        current: Specifies whether you want to save the current for the subcircuit
        power: Specifies whether you want to save the power signals for the subcircuit
        v_depth:
            The hierarchy level to which you want to save the voltage signal for the subcircuit.
            If not specified, voltage for all the levels of hierarchy are saved.
        i_depth:
            The hierarchy level to which you want to save the current signal for the subcircuit.
            If not specified, current for all the levels of hierarchy are saved.
        pwr_depth:
            The hierarchy level to which you want to save the power signal for the subcircuit.
            If not specified, power signals for all the levels of hierarchy are saved.
        compress:
            Specifies whether you want to reduce the size of the output file.
            When enabled, the spectre simulator saves the data for a signal only when the value of that signal changes.
        filter_r_c: Specifies whether to filter out the nodes that are connected only to parasitic elements from the output signal list
        ports: Specifies whether to save the output port information for the specified subcircuit
        user_options: Specify the other save options that you want to define for the signal

    Returns:
        t: Returns t if the subcircuit instance is saved
        nil: Returns nil if the name of the specified instance is not correct
    """
    raise NotImplementedError


def select_result(results_name: AnalysisType, sweep_value: float | int = None) -> None:
    """Selects the results from a particular analysis whose data you want to examine.

    The argument that you supply to this command is a data type representing the particular type of analysis results you want.
    All subsequent data access commands use the information specified with :func:`select_result`.

    Args:
        results_name (AnalysisType): Results from an analysis
        sweep_value (float | int, optional): The sweep value you wish to select for an analysis

    Returns:
        The object representing the selected results

    Raises
        ValueError: There are problems selecting the analysis.
    """
    if sweep_value is None:
        ret = ws['selectResult'](results_name)
    else:
        ret = ws['selectResult'](results_name, sweep_value)

    if ret is None:
        raise ValueError('There are problems selecting the analysis.')

    return ret


def sp():
    """Returns S-parameters for N port networks.

    Args:
        i_index: The ith index of the coefficient in the scattering matrix
        j_index: The jth index of the coefficient in the scattering matrix
        result_name:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by the selectResult command.
            The default is the current result selected with the selectResult command.
        results_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the resultName argument.
            When specified, this argument will only be used internally and will not alter the current results directory which was set by the openResults command.
            The default is the current results directory set by the openResults command.

    Returns:
        waveform: Waveform object representing the S-parameter
        nil: Returns nil if there is an error
    """
    raise NotImplementedError


def sprobe_data():
    """Returns the waveform for the specified analysis and parameter type of the given sprobe instance.

    Args:
        waveform:
            Waveform object that displays a series of points on a grid.
            srrWave:XXXXX is used as the waveform object identifier.
        nil: Returns nil if there is an error and a waveform cannot be returned
    """
    raise NotImplementedError


def sweep_names(waveform: RemoteWaveform = None, result: str = None, results_dir: str = None) -> list[str]:
    """Returns the names of all the sweep variables for either a supplied waveform, a currently selected result (via :func:`select_result()`) or a specified result.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX).
            When this argument is used, the `results_dir` and `result_name` arguments are ignored.
        result:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by the :func:`select_result()` command.
            The default is the current result selected with the :func:`select_result()` command.
        results_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the `result_name` argument.
            When specified, this argument will only be used internally and will not alter the current results directory which was set by the :func:`open_results()` command.
            The default is the current results directory set by the :func:`open_results()` command.

    Returns:
        list: Returns a list of the sweep names

    Raises:
        ValueError: The sweep names cannot be returned.
    """
    ret = None

    args = []

    if waveform is not None:
        args += [waveform]
    elif result is not None:
        args += [result]

        if results_dir is not None:
            args += [results_dir]

    ret = ws['sweepNames'](*args)

    if ret is None:
        raise ValueError('The sweep names cannot be returned.')

    return ret


def sweep_values(waveform: RemoteWaveform = None):
    """Returns the list of sweep values of the outermost sweep variable of either the selected results or the supplied waveform.

    This command is particularly useful for parametric analyses.

    Args:
        waveform:
            Waveform object representing simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.).

    Returns:
        list: Returns the list of sweep values.

    Raises:
        ValueError: The list of sweep values cannot be returned.
    """
    args = []

    if waveform is not None:
        args += [waveform]

    ret = ws['sweepValues'](*args)

    if ret is None:
        raise ValueError('The list of sweep values cannot be returned.')

    return ret


def sweep_var_values():
    """Returns the list of sweep values for a particular swept variable name.

    This command is particularly useful for parametric analyses.

    Args:
        var_name: Name of the specific variable from which the values are retrieved
        result:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by the selectResult command.
            The default is the current result selected with the selectResult command.
        results_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the resultName argument.
            When specified, this argument will only be used internally and will not alter the current results directory which was set by the openResults command.
            The default is the current results directory set by the openResults command.

    Returns:
        sweep_values: Returns the list of sweep values
        nil: Returns nil and an error message if the list of sweep values cannot be returned
    """
    raise NotImplementedError


def v():
    """Returns the voltage of the specified net.

    Args:
        net: Name of the net
        result:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by the selectResult command.
            The default is the current result selected with the selectResult command.
        results_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the resultName argument.
            When specified, this argument will only be used internally and will not alter the current results directory which was set by the openResults command.
            The default is the current results directory set by the openResults command.

    Returns:
        waveform:
            Returns a waveform object.
            A waveform object represents simulation results that can be displayed as a series of points on a grid.
            (A waveform object identifier looks like this: srrWave:XXXXX.
            ).
        nil: Returns an error message and nil if there is a problem
    """
    raise NotImplementedError


def vswr():
    """Computes the voltage standing wave ratio.

    Args:
        index: Index of the port
        result:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by the selectResult command.
            The default is the current result selected with the selectResult command.
        results_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the resultName argument.
            When specified, this argument will only be used internally and will not alter the current results directory which was set by the openResults command.
            The default is the current results directory set by the openResults command.

    Returns:
        waveform: Waveform object representing the voltage standing wave ratio
        nil: Returns an error message or nil if there is a problem
    """
    raise NotImplementedError


def zm():
    """Computes the port input impedance.

    Args:
        index: Index of the port
        result:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by the selectResult command.
            The default is the current result selected with the selectResult command.
        results_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the resultName argument.
            When specified, this argument will only be used internally and will not alter the current results directory which was set by the openResults command.
            The default is the current results directory set by the openResults command.

    Returns:
        waveform: Waveform object representing the port input impedance
        nil: Returns an error message and nil if there is a problem
    """
    raise NotImplementedError


def zref():
    """Returns the reference impedance for an N-port network.

    Args:
        port_index: Index of the port
        result:
            Results from an analysis.
            When specified, this argument will only be used internally and will not alter the current result which was set by the selectResult command.
            The default is the current result selected with the selectResult command.
        results_dir:
            Directory containing the PSF files (results).
            If you supply this argument, you must also supply the resultName argument.
            When specified, this argument will only be used internally and will not alter the current results directory which was set by the openResults command.
            The default is the current results directory set by the openResults command.

    Returns:
        impedance: Reference impedance
        nil: Returns an error message and nil if there is a problem
    """
    raise NotImplementedError

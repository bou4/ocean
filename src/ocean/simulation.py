from ocean.workspace import ws
from ocean.utils import Symbol, SymbolEnum, Key


class AnalysisType(SymbolEnum):
    """Analysis Type"""
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


class Categ(SymbolEnum):
    """Category"""
    analog = Symbol('analog')
    digital = Symbol('digital')


class Mode(SymbolEnum):
    """Mode"""
    read = Symbol('r')
    write = Symbol('w')
    append = Symbol('a')


class SaveType(SymbolEnum):
    """Save Type"""
    #: Specifies that a list of subsequent net names be saved.
    v = Symbol('v')
    #: Specifies that a list of subsequent currents be saved.
    i = Symbol('i')
    #: Specifies that all nets and all currents are to be saved.
    all = Symbol('all')
    #: Specifies that all voltages are to be saved.
    allv = Symbol('allv')
    #: Specifies that all currents are to be saved.
    alli = Symbol('alli')


class Simulator(SymbolEnum):
    """Simulator"""
    ADSsim = Symbol('ADSsim')
    ams = Symbol('ams')
    hspiceD = Symbol('hspiceD')
    spectre = Symbol('spectre')
    UltraSim = Symbol('UltraSim')


def ac():
    """Specifies an AC analysis.

    Args:
        from_value: Starting value for the AC analysis
        to_value: Ending value
        pts_per_dec: Points per decade
        inc_type:
            Increment type.
            Valid values: 

For the Spectre® circuit simulator, "Linear", "Logarithmic", or "Automatic".
            For other simulators, "Linear" or "Logarithmic".
        points: Either the linear or the logarithmic value, which depends on t_incType

    Returns:
        undefined: The return value for this command/function is undefined
        nil: Returns nil and prints an error message if the analysis is not specified
    """
    raise NotImplementedError


def analysis(analysis_type: AnalysisType, **analysis_options) -> None:
    """Specifies the analysis to be simulated.

    Args:
        analysis_type:
            Type of the analysis.
            The value can be any member of a particular subset (depending on the simulator) of :class:`AnalysisType`.
            The basic SPICE2G-like choices: :attr:`AnalysisType.tran`, :attr:`AnalysisType.dc`, :attr:`AnalysisType.ac`, and :attr:`AnalysisType.noise`.
        analysis_options:
            Analysis options.
            The analysis options available depend on which simulator you use.
            (See the documentation for your simulator.)
            If you are using the Spectre® circuit simulator, see the information about analysis statements in the Virtuoso Spectre Circuit Simulator Reference for analysis options you can use.

    Returns:
        undefined: The return value for this function is undefined

    Raises:
        ValueError: There is a problem specifying the analysis.
    """
    ret = ws['analysis'](analysis_type, **analysis_options)

    if ret is None:
        raise ValueError('There is a problem specifying the analysis.')

    return ret


def converge():
    """Sets convergence criteria on nets.

    Args:
        conv_name:
            Name of the convergence type.
            Valid values are one of nodeset ic and forcenode.
            forcenode is not supported for the spectre simulator.
        net_name1: Name of the net to which you want to set convergence criteria
        value1: Voltage value for the net
        net_name_n: Name of the additional net
        value: Voltage value for the additional net

    Returns:
        undefined: The return value for this command/function is undefined
        nil: Returns nil and prints an error message if the function fails
    """
    raise NotImplementedError


def connect_rules():
    """Sets connect rules for a given AMS OCEAN session required by the elaborator.

    To specify multiple connect rules, use this command multiple times.
    To add a connect rule to an OCEAN session, you can either choose a built-in rule from the connectLib library (by specifying t_ruleName, t_libName and t_viewName) or one of your own compiled built-in connect rules (by specifying t_ruleName, t_libName and t_viewName).
    To add a user defined connect rule to an OCEAN session specify s_userDefined.
    To modify an existing built-in rule, you need to specify t_baseRule (the name of the built-in rule that needs be modified), specify a new name (by specifying t_ruleName, t_libName and t_viewName) and also specify one or more of the optional arguments.

    Args:
        rule_name: Name of the connect rule that you want to use in the current session
        lib_name:
            Name of the library that contains a list of user-compiled connect rules.
            If you do not specify this, the connect rules are assumed to be in the default location.
        view_name: Name of the view of the selected cell
        base_rule: Name of the connect rule that you want to modify
        module_info:
            Arguments that need to be updated for a specified connect rule.
            The arguments may include s_mode, s_direction1, s_direction2, s_discipline1 and s_discipline2.
            Valid values for s_mode are: null, split, merged.
            s_direction1 and s_direction2 work as a pair.
            Valid combinations are: both null, input/output, output/input, inout/inout.
            s_discipline1 and s_discipline2 also work as a pair.
            Either they should both be null or they should both have values.
        resolution_info:
            Names of disciplines that need to be resolved to another discipline.
            The value specified overwrites the l_resolutionInfo in the base rule or in the existing connect rule.
        common_param:
            One or more parameters that you want to modify for all modules or a set of modules.
            Although the same result can be achieved by using the l_moduleInfo argument, l_commonParam facilitates updating parameters for all modules in one go.
        user_defined:
            Name of the user defined connect rule that you want to use in the current session.
            Specify 3step as the value of s_userDefined and specify t_ruleName, t_libName and t_viewName to add a user defined connect rule for the Cellview-based netlister flow.
            Specify irun as the value of s_userDefined and specify t_ruleName, s_fileName or both to add a user defined connect rule for the OSS-based netlister with irun flow.
            Any other argument specified when adding a user defined connect rule will be ignored.
        tag: The option used to indicate that no connect rules are to be used for the current session

    Returns:
        t: Returns t if the specifed connect rules are set
        nil: Returns nil and prints an error message otherwise
    """
    raise NotImplementedError


def create_final_netlist():
    """Creates the final netlist for viewing purposes.

    The netlist also can be saved but is not required to run the simulator.

    Returns:
        t: Returns t if the final netlist is created
        nil: Returns nil and prints an error message otherwise
    """
    raise NotImplementedError


def create_netlist():
    """Creates the simulator input file.

    Args:
        g_recreate_all: Specifies if the netlist needs to be recreated or not
        display: Specifies if the netlist is to be displayed or not

    Returns:
        file_name: Returns the name of the simulator input file
        nil: Returns nil otherwise
    """
    raise NotImplementedError


def dc():
    """Specifies a DC sweep analysis with limited options.

    If other analysis options are needed, use the analysis command.

    Args:
        comp_name: Name of the source (or component, for the Spectre® circuit simulator) to sweep
        comp_param: For the Spectre® circuit simulator, the component parameter to be swept
        from_value: Starting value for the DC analysis
        to_value: Ending value
        by_value: The increment at which to step through the analysis

    Returns:
        undefined: The return value for this command/function is undefined
        nil: Returns nil and prints an error message if the analysis is not specified
    """
    raise NotImplementedError


def definition_file():
    """Specifies definitions files to be included in the simulator input file.

    Args:
        file_name: The name of the definition file that would typically contain functions or parameter statements

    Returns:
        file_names: A list of the file names specified; returned on success
        nil: Otherwise nil is returned
    """
    raise NotImplementedError


def delete():
    """Deletes all the information specified.

    Args:
        command:
            Command that was initially used to add the items that are now being deleted.
            Valid values: analysis, connectRules, discipline, globalSignal, desVar, path, save, ic, forcenode, nodeset.
        command_arg1: Argument corresponding to the specified command
        command_arg2: Additional argument corresponding to the specified command

    Returns:
        t: Returns t if the information is deleted
        nil: Returns nil if there is an error
    """
    raise NotImplementedError


def delete_op_point():
    """Deletes the specified operating point instance.

    Args:
        inst_name: Name of the operating point instance to be deleted
        rest: List of optional arguments that can be passed to this function

    Returns:
        t: Returns t when the function runs successfully
        nil: Otherwise, returns nil if there is an error
    """
    raise NotImplementedError


def design(*args):
    """Refer to the documentation of :func:`design_query()`, :func:`design_netlist()` and :func:`design_name()`.

    All function signatures can be used when calling :func:`design()`.

    Raises:
        TypeError: The wrong function signature is used.
    """
    if len(args) == 0:
        ret = design_query()
    if len(args) == 1:
        ret = design_netlist(*args)
    elif len(args) == 3:
        ret = design_name(*args)
    else:
        raise TypeError('The wrong function signature is used.')

    return ret


def design_query() -> str | tuple[Symbol, Symbol, Symbol]:
    """Queries the currently specified design.

    Returns:
        str | tuple:
            The name of the design, or a tuple (lib, cell, view), where lib, cell, and view represent the name of the view for an Virtuoso® Analog Design Environment design if successful.

    Raises:
        ValueError: The design has not been specified as yet.
    """
    ret = ws['design']()

    if ret is None:
        raise ValueError('The design has not been specified as yet.')

    if isinstance(ret, list):
        ret = tuple(ret)


def design_netlist(ckt_file: str) -> str:
    """Specifies the directory path to the netlist of a design to be simulated.

    Args:
        ckt_file (str):
            Directory path to the netlist followed by the name of the netlist file.
            Name of the netlist file must be netlist.
            The `netlistHeader` and `netlistFooter` files must be in the same directory.
            Otherwise, `ckt_file` is a pre-existing netlist file from another source.

    Returns:
        str:
            The name of the design if successful.

    Raises:
        ValueError: There is a problem using the specified design.
    """
    ret = ws['design'](ckt_file)

    if ret is None:
        raise ValueError('There is a problem using the specified design.')

    return ret


def design_name(lib: str, cell: str, view: str, mode: Mode = Mode.append) -> tuple[Symbol, Symbol, Symbol]:
    """Specifies the directory path to the netlist of a design or the name of a design to be simulated.

    Args:
        lib (str): Name of the library that contains the design
        cell (str): Name of the design
        view (str): View of the design (typically schematic)
        mode (Mode, optional):
            The mode in which the design should be opened.
            The value can be any member of :class:`Mode`.
            The default mode is :attr:`Mode.append`.
            Read-only designs can be netlisted only by direct netlisters, and not socket.
            The :attr:`Mode.write` mode should not be used as it overwrites the design.

    Returns:
        tuple:
            A tuple (lib, cell, view), where lib, cell, and view represent the name of the view for an Virtuoso® Analog Design Environment design if successful

    Raises:
        ValueError: There is a problem using the specified design.
    """
    ret = ws['design'](lib, cell, view, mode)

    if ret is None:
        raise ValueError('There is a problem using the specified design.')

    return tuple(ret)


def des_var(des_vars: dict = None) -> str | dict:
    """Sets the values of design variables used in your design.

    You can set the values for as many design variables as you want.

    Args:
        des_vars:
            Dictionary containing the name/value pairs of the design variables.

    Returns:
        str | dict: If no argument is passed, the current design variables are returned as a dictionary, else, the value of the last set variable is returned.

    Raises:
        ValueError: The assignment fails.
    """
    if des_vars is None:
        ret = ws['desVar']()

        if ret:
            return {y[0]: y[1] for y in ret}
        else:
            return {}
    else:
        # TODO: Make a helper function to do this.
        x = [None] * (2 * len(des_vars))
        x[0:: 2] = des_vars.keys()
        x[1:: 2] = des_vars.values()

        ret = ws['desVar'](*x)

        if ret is None:
            raise ValueError('The assignment fails.')

        return ret


def discipline():
    """Adds discrete disciplines to the existing set of disciplines for a given 'ams' OCEAN session.

    You can use delete('discipline) to delete one or more specified disciplines.
    You can use ocnDisplay('discipline) to view the currently active disciplines in an OCEAN session.

    Args:
        discipline1: Name of a discrete discipline to be added
        discipline2: Names of additional discrete disciplines to be added

    Returns:
        t: Returns t if the discipline is added
        nil: Returns nil or prints an error message otherwise
    """
    raise NotImplementedError


def display_netlist():
    """Displays the concatenated AMS complete design info file used in a given AMS OCEAN session.

    The concatenated file displays the cell-based netlisting of the cellviews used in the configuration along with the analog control file and the TCL file generated by AMS-ADE.
    This command is applicable for both solvers – Spectre and UltraSim.

    Returns:
        t: Returns t if the concatenated design information file
        nil: Returns nil or prints an error message otherwise
    """
    raise NotImplementedError


def env_option():
    """Sets environment options.

    Args:
        env_option1: Name of the first environment option to set
        value1: Value for the option
        env_option_n: Name of an additional environment option to set
        value_n: Value for the option

    Returns:
        undefined: The return value for this command/function is undefined
        nil: Returns nil if there are problems setting the option
    """
    raise NotImplementedError


def evcd_file():
    """Sets an EVCD file for a given UltraSim OCEAN session.

    You also need to specify an EVCD info file while using this command.
    You can specify only one EVCD file for a session.
    You may use ocnDisplay('evcdFile) to view the currently active EVCD file.

    Args:
        evcd_file_name: The name of the EVCD file to be used for session

    Returns:
        evcd_file_name: The EVCD file name is the output if the command is successful
        nil: Otherwise, nil is returned
    """
    raise NotImplementedError


def evcd_info_file():
    """Sets a EVCD info file for a given UltraSim OCEAN session.

    You also need to specify an EVCD file while using this command.
    You can specify only one EVCD info file for a session.
    You may use ocnDisplay('evcdInfoFile) to view the currently active EVCD info file.

    Args:
        evcd_info_file_name: The name of the EVCD info file to be included

    Returns:
        evcd_info_file_name: The EVCD info file name is the output if the command is successful
        nil: Otherwise, nil is returned
    """
    raise NotImplementedError


def forcenode():
    """Holds a node at a specified value.

    Args:
        net_name1: Name of the net
        value1: Voltage value for the net
        net_name_n: Name of an additional net
        value_n: Voltage value for the net

    Returns:
        undefined: The return value for this command/function is undefined
        nil: Returns nil and prints an error message
    """
    raise NotImplementedError


def global_sig_alias():
    """Removes all the previous signal aliases and creates the specified aliases.

    The signal names in each of the signal lists are marked as aliases of each other.
    Each of the signal lists is a set of signal names that are to be aliased.
    The signal names should match the names that were specified using the globalSignal command.
    To unalias all signal, pecify nil instead of signal lists.

    Args:
        signal_list(n): A list of signals that are to be marked as aliases of each other

    Returns:
        t: Returns t when previous signal aliases have been removed successfully and new aliases are created according to the signal lists provided
        nil: Returns nil and prints an error message if the function was unsuccessful
    """
    raise NotImplementedError


def global_signal():
    """Adds or modifies a global signal for a given AMS OCEAN session needed by the elaborator.

    If the global signal already exists in the session, the values are updated.
    If it does not exist, a global signal with the specified name is added.
    In case of a vector signal, the range information can be appended with the name of the signal.

    Args:
        name: The name of the global signal
        lang:
            The namespace within which the signal is entered.
            It is used to map the signal name to Verilog-AMS.
            Valid Values: CDBA, Spectre, Spice, Verilog-AMS

Default Value: CDBA.
        wire_type:
            Indicates the Verilog type of the signal declaration.
            Valid Values: wire, supply0, supply1, tri, tri0, tri1, triand, trior, trireg, wand, wor, wreal 

Default Value: wire.
        discipline: A string value to indicate the discipline of the signal
        ground: Valid Values: YES, NO 

Default Value: NO
        rest: List of optional arguments that can be passed to this function

    Returns:
        t: Returns t when a global signal has been successfully added or modified
        nil: Returns nil and prints an error message if the function was unsuccessful
    """
    raise NotImplementedError


def ic():
    """Sets initial conditions on nets in a transient analysis.

    Args:
        net_name1: Name of the net
        value1: Voltage value for the net
        net_name_n: Name of an additional net
        value_n: Voltage value for the net

    Returns:
        undefined: The return value for this command/function is undefined
        nil: Returns nil and prints an error message
    """
    raise NotImplementedError


def include_file():
    """Includes the specified file in the final netlist of the simulator for the current session.

    Args:
        file_name: Name of the file to include in the final netlist

    Returns:
        file_name: Returns the name of the file if successful
        nil: Returns nil and prints an error message otherwise
    """
    raise NotImplementedError


def model_file(*model_files: str | tuple[str, str] | list[str | tuple[str, str]]) -> list[tuple[str, str]]:
    """Specifies model files to be included in the simulator input file.

    Args:
        model_files:
            Can be a string to specify the name of the model file.
            Can also be a tuple of two strings to specify the name of the model file and the name of the section.
            Can also be a list of either of the above.

    Returns:
        list: A list of all the model file/section pairs

    Raises:
        ValueError:
            No file section pairs have been specified with the current call or a previous call of this command, or an error has been encountered.
    """
    ret = ws['modelFile'](*model_files)

    if ret is None:
        raise ValueError(
            'No file section pairs have been specified with the current call or a previous call of this command, or an error has been encountered.')

    return [tuple(i) for i in ret]


def nodeset():
    """Sets the initial estimate for nets in a DC analysis, or sets the initial condition calculation for a transient analysis.

    Args:
        net_name1: Name of the net
        value1: Voltage value for the net
        net_name_n: Name of an additional net
        value_n: Voltage value for the net

    Returns:
        undefined: The return value for this command/function is undefined
        nil: Returns nil and prints an error message otherwise
    """
    raise NotImplementedError


def noise():
    """Specifies a noise analysis.

    Args:
        output: Output node
        source: Input source

    Returns:
        undefined: The return value for this command/function is undefined
        nil: Returns nil and prints an error message If there is a problem specifying the analysis
    """
    raise NotImplementedError


def ocn_close_session():
    """Closes the current OCEAN session without saving any settings made during the session.

    The command has no effect if no session is currently active.

    Args:
        t: Returns t when the current session is successfully closed
        nil: Returns nil if there is a problem closing the active session
    """
    raise NotImplementedError


def ocn_display():
    """Displays all the information specified.

    Args:
        output:
            File in which to write the information.
            The ocnDisplay command opens the file, writes to the file, then closes the file.
            If you specify the filename without a path, the ocnDisplay command creates the file in the directory pointed to by your SKILL Path.
            To find out what your SKILL path is, type getSkillPath() at the OCEAN prompt.
        port:
            Port (previously opened with outfile) through which to append the information to a file.
            You are responsible for closing the port.
            See the outfile command for more information.
        command:
            Command that was initially used to add the items that are now being displayed.
            Valid values: Most simulation setup commands.
            The commands that are supported include design, analysis, tran, ac, dc, noise, resultsDir, temp, option, desVar, path, includeFile, modelFile, stimulusFile, definitionFile, saveOption, envOption, save, converge, ic, forcenode, nodeset, simulator, setup, restore, saveSubckt.
        command_arg1: Argument corresponding to the specified command
        command_arg2: Additional argument corresponding to the specified command

    Returns:
        t: Displays the information and returns t
        nil: Returns nil and prints an error message if there are problems displaying the information
    """
    raise NotImplementedError


def ocn_dspf_file():
    """Sets the parasitic (dspf, spf) files to be used in a Spectre OCEAN session.

    You can use this command to specify a list of parasitic files to be included in the control file.
    You can use ocnDisplay('dspfFile) to view the currently active parasitic (dspf, spf) files in an OCEAN session.

    Args:
        dspf_file: The name of the parasitic (dspf, spf) file to be included
        dspf_file1...t_dspf_file_n: The name of the additional parasitic (dspf, spf) files to be included

    Returns:
        dspf_file: Lists the names of the parasitic (dspf, spf) files
        nil: Returns nil if there are problems displaying the information
    """
    raise NotImplementedError


def ocn_spef_file():
    """Sets the parasitic (spef) files to be used in a Spectre OCEAN session.

    You can use this command to specify a list of parasitic files to be included in the control file.
    You can use ocnDisplay('SpefFile) to view the currently active parasitic (spef) files in an OCEAN session.

    Args:
        spef_file: The name of the parasitic (spef) file to be included
        spef_file1...t__spef_file_n: The name of the additional parasitic (spef) files to be included

    Returns:
        spef_file: Lists the names of the parasitic (spef) files
        nil: Returns nil if there are problems displaying the information
    """
    raise NotImplementedError


def ocn_pspice_file():
    """Sets the PSpice files to be used in  a Spectre OCEAN session.

    Use this command to specify a list of PSpice files to be included in the control file.

    Args:
        p_spice_file: The name of the PSpice file to be included
        p_spice_file1...t__p_spice_file_n: The name of the additional PSpice files to be included

    Returns:
        p_spice_file: Lists the names of the PSpice files
        nil: Returns nil if there are problems displaying the information
    """
    raise NotImplementedError


def ocn_get_adjusted_path():
    """Reduces the given hierarchical net path to the shortest hierarchical name that is equivalent to this net.

    Args:
        lib_name: Library name of the top cellview of the design
        cell_name: Cell name of the top cellview of the design
        view_name: View name of the top cellview of the design
        net_name: A single concatenated string for the instance hierarchy with "/" as the hierarchy separator in the string

    Returns:
        adjusted_path:
            The reduced net name.
            If the net is local to this cell view only, the reduced net name is the same as the provided net name.
        nil: Returns nil if there is a problem returning the adjusted path
    """
    raise NotImplementedError


def ocn_get_instances_model_name():
    """This function returns the model name used by the instance in opened simulation results.

    Args:
        instance: Name of the instance in the simulation result or the schematic

    Returns:
        instance: The list of instance names and models used by instance
        nil: Returns nil if no result is open
    """
    raise NotImplementedError


def off():
    """Turns off the specified information.

    Args:
        command:
            Command that was initially used to add the items that are now being turned off.
            Valid value: restore.
        command_arg1: Argument corresponding to the specified command
        command_arg2: Additional argument corresponding to the specified command

    Returns:
        t: Returns t if the information is turned off
        nil: Returns nil and prints an error message if there are problems turning off the information
    """
    raise NotImplementedError


def option():
    """Specifies the values for built-in simulator options.

    You can specify values for as many options as you want.

    Args:
        categ:
            Type of simulator to be used.
            Valid values: analog if the options are for an analog simulator, digital for a digital simulator, or mixed for a mixed-signal simulator

Default value: analog.
        option1: Name of the simulator option
        value1: Value for the option
        option2: Name of an additional simulator option
        value2: Value for the option

    Returns:
        undefined: The return value for this command/function is undefined
        nil: Returns nil and prints an error message if there are problems setting the option
    """
    raise NotImplementedError


def restore():
    """Tells the simulator to restore the state previously saved to a file with a store command.

    Args:
        analysis_type:
            Type of the analysis.
            Valid values: dc or tran.
        filename: Name of the file containing the saved state

    Returns:
        undefined: The return value for this command/function is undefined
        nil: Returns nil and prints an error message if there are problems restoring the information
    """
    raise NotImplementedError


def results_dir(dir_name: str = None) -> str:
    """Specifies the directory where the PSF files (results) are stored.

    If you do not specify a directory with this command, the PSF files are placed in `../psf` to the netlist directory.

    Note: The directory you specify with :func:`results_dir()` is also where the `simulator.out` file is created.

    Note:
        Some simulators are designed to always put their results in a specific location.
        For these simulators, :func:`results_dir()` has no effect.
        You might use this command when you want to run several simulations using the same design and want to store each set of results in a different location.
        If this command is not used, the results of an analysis are overwritten with each simulation run.

    Args:
        dir_name (str, optional): Directory where the PSF files are to be stored.

    Returns:
        str: The directory where the PSF files (results) are stored.

    Raises:
        ValueError: There is a problem with that directory.
    """
    if dir_name:
        ret = ws['resultsDir'](dir_name)
    else:
        ret = ws['resultsDir']()

    if ret is None:
        raise ValueError('There is a problem with that directory.')

    return ret


def run():
    """Starts the simulation or specifies a time after which an analysis should start.

    If distributed processing is not available on the system or is not enabled, the arguments specific to distributed processing (see Arguments section below for list of arguments specific to distributed processing) are ignored and the simulation runs locally.
    If distributed processing is available and is enabled, the environment default values are used if not specified in the run command arguments.
    The environmental default values are stored in the.
    cdsenv file.

    Args:
        analysis_list: List of analyses to be run with the run command
        analysis_type1: Name of a prespecified analysis to be simulated
        analysis_type_n: Name of another prespecified analysis to be simulated

    Returns:
        job_name:
            Returns the job name of the job submitted.
            The job name is based on the jobName argument.
            If the job name submitted is not unique, a unique identifier is appended to the job name.
            This value is returned for nonblocking distributed mode.
        dir_name:
            Returns the name of the directory in which the results are stored.
            This value is returned for local and blocking distributed modes.

    Raises:
        ValueError:
            There is an error in the simulation.
            In this case, look at the `yourSimulator.out` file for more information.
            (This file is typically located in the psf directory.).

    TODO: This function is far from complete.
    """
    ret = ws['run']()

    if ret is None:
        raise ValueError('There is an error in the simulation.')

    return ret


def save(save_type: SaveType = None, save_names: list[str] = None, categ: Categ = None) -> None:
    """Specifies the outputs to be saved and printed during simulation.

    Args:
        save_type:
            Type of outputs to be saved.
            The value can be any member of :class:`SaveType`.
            The default save type is :attr:`SaveType.allv`.
        save_names: List of nets, devices, or other objects
        categ:
            Type of simulator to be used.
            Valid values can be any member of :class:`Category`.
            The default category is :attr:`Category.analog`

            Note: :attr:`Category.digital` is not available.

    Returns:
        undefined: The return value for this command/function is undefined.

    Raises:
        ValueError: There is a problem saving the outputs.
    """
    args = []

    if categ is not None:
        args.append(Key('categ'))
        args.append(categ)

    if save_type is not None:
        args.append(save_type)

    if save_names is not None:
        args += save_names

    ret = ws['save'](*args)

    if ret is None:
        raise ValueError('There is a problem saving the outputs.')

    if isinstance(ret, list):
        if all(isinstance(x, Symbol) for x in ret):
            return [SaveType(x) for x in ret]
    else:
        if isinstance(ret, Symbol):
            return SaveType(ret)

    return ret


def save_op_point():
    """Specifies the operating point parameters to be saved for a given instance.

    Args:
        inst_name: Name of the instance for which the parameters are to be saved
        operating_points: List of the operating point parameters

    Returns:
        t: Returns t when the function runs successfully
        nil: Returns nil if there is an error
    """
    raise NotImplementedError


def save_option():
    """Specifies save options to be used by the simulator.

    Args:
        option1:
            Save option.
            The save options that are available depend on which simulator you use.
            (See the documentation for your simulator.
            ).
        option_value1: Value for the save option
        option_n:
            Any subsequent save option.
            The save options that are available depend on which simulator you use.
            (See the documentation for your simulator.
            ).
        option_value_n: Value for the save option

    Returns:
        undefined: The return value for this command/function is undefined
        nil: Returns nil if there are problems specifying options
    """
    raise NotImplementedError


def simulator(simulator: Simulator = None) -> Simulator:
    """Starts an OCEAN session and sets the simulator name for that session.

    The previous session (if any) is closed and all session information is cleared.

    Args:
        simulator (:obj:`Simulator`, optional): Name of the simulator

    Returns:
        :obj:`Simulator`: Returns the name of the simulator

    Raises:
        ValueError:
            The simulator is not registered with the Virtuoso® Analog Design Environment through OASIS.
            If the simulator is not registered, the simulator from the preceding session is retained.
    """
    ret = ws['simulator'](simulator)

    if ret is None:
        raise ValueError(
            'The simulator is not registered with the Virtuoso® Analog Design Environment through OASIS.')

    return Simulator(ret)


def solver():
    """Sets a solver for a given AMS OCEAN session.

    The valid values for solver are Spectre and UltraSim.
    You select Spectre if you want to use an accurate AMS-Spectre analog engine.
    You select UltraSim if you want to use the AMS-Ultrasim or FastSPICE(UltraSim) solver for a given AMS simulation.

    Args:
        solver: Name of the solver

    Returns:
        solver: Returns the name of the solver
        nil:
            Returns nil and prints an error message if the specified solver is not registered with the Virtuoso® Analog Design Environment through OASIS.
            If the solver is not registered, the solver from the preceding session is retained.
    """
    raise NotImplementedError


def stimulus_file():
    """Specifies stimulus files to be used by the simulator.

    Args:
        file_name: The name of the stimulus file to be included
        file_name2...t_file_name_n: The names of the additional stimulus files to be included
        xlate:
            If set to t, net and instance expressions are translated to simulator names.
            The default value of the g_xlate variable is t.

    Returns:
        file_names: A list of the stimulus file names is the output if the command is successful
        nil: Otherwise nil is returned
    """
    raise NotImplementedError


def store():
    """Requests that the simulator store its node voltages to a file.

    Args:
        analysis_type:
            Type of the analysis.
            Valid values: dc or tran.
        filename: Name of the file in which to store the simulator's node voltages

    Returns:
        filename: Returns the filename
        nil: Returns nil and prints an error message if there are problems storing the information to a file
    """
    raise NotImplementedError


def temp():
    """Specifies the circuit temperature.

    Args:
        temp_value: Temperature for the circuit

    Returns:
        temp_value: Returns the temperature specified
        nil: Returns nil and prints an error message if there are problems setting the temperature
    """
    raise NotImplementedError


def tran():
    """Specifies a transient analysis with limited options.

    If other analysis options are needed, use the analysis command.

    Args:
        from_value: Starting time for the analysis
        to_value: Ending time
        by_value: Increment at which to step through the analysis

    Returns:
        undefined: The return value for this command/function is undefined
        nil: Returns nil and prints an error message if the analysis is not specified
    """
    raise NotImplementedError


def vcd_file():
    """Sets a VCD file for a given AMS or UltraSim OCEAN session.

    You also need to specify a VCD info file while using this command.
    You can specify only one VCD file for a session.
    You may use ocnDisplay('vcdFile) to view the currently active VCD file.

    Args:
        vcd_file_name: The name of the VCD file to be used for session

    Returns:
        vcd_file_name: The VCD file name is the output if the command is successful
        nil: Otherwise, nil is returned
    """
    raise NotImplementedError


def vcd_info_file():
    """Sets a VCD info file for a given AMS or UltraSim OCEAN session when you have set UltraSim as the solver.

    You also need to specify a VCD file while using this command.
    You can specify only one VCD info file for a session.
    You may use ocnDisplay('vcdInfoFile) to view the currently active VCD info file.

    Args:
        vcd_info_file_name: The name of the VCD info file to be included

    Returns:
        vcd_info_file_name: The VCD info file name is the output if the command is successful
        nil: Otherwise, nil is returned
    """
    raise NotImplementedError


def vec_file():
    """Sets the vector files to be used in an AMS or UltraSim OCEAN session.

    You use the vecFile command to specify a list of vector files which go to control file.
    You may use ocnDisplay('vecFile) to view the currently active vector files in an OCEAN session.

    Args:
        vec_file: The name of the vector file to be included
        vec_file1...t_vec_file_n: The names of the additional vector files to be included

    Returns:
        vec_file: The names of the vector file(s) are listed if the command is successful
        nil: Otherwise, nil is returned
    """
    raise NotImplementedError


def hlcheck():
    """Sets or gets the value of the hlcheck option used in the vec_include statement in a netlist.

    You may use the ocnDisplay('hlcheck) command to view the current value of hlcheck in an OCEAN session associated with vector files.

    Args:
        value:
            Value to be set for the hlcheck option.
            Possible values include "off", "0", and "1".
            The value "off" disables the hlcheck option in the vec_include statement.

    Returns:
        t: Returns t if the hlcheck option is set with the value supplied as argument
        nil: Otherwise, returns nil and an error message is displayed
    """
    raise NotImplementedError


def ocn_ams_set_oss_netlister():
    """Sets the netlister mode to OSS-based for a given ams OCEAN session.

    Returns:
        t: Returns t if successful
        nil: Returns nil otherwise
    """
    raise NotImplementedError


def ocn_ams_set_unl_netlister():
    """Sets the netlister mode to AMS Unified Netlister for a given ams OCEAN session.

    Returns:
        t: Returns t if successful
        nil: Returns nil otherwise
    """
    raise NotImplementedError

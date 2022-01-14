from ocean.workspace import ws


def param_analysis(des_var: str, param_analysis_ret: None = None, **kwargs) -> None:
    """Sets up a parametric analysis.

    Args:
        des_var: Name of the design variable to be swept
        param_analysis_ret: Value returned from another :func:`param_analysis()` call used to achieve multidimensional parametric analysis
        start: Beginning value for the design variable
        stop: Final value for the design variable
        center: Center point for a range of values that you want to sweep
        span:
            Range of values that you want to sweep around the center point.
            For example, if `center` is 100 and `span` is 20 then the sweep range extends from 90 to 110.
        step:
            Increment by which the value of the design variable changes.
            For example, if `start` is 1.0, `stop` is 2.1, and f_step is 0.2, the parametric analyzer simulates at values 1.0, 1.2, 1.4, 1.6, 1.8, and 2.0.
        lin:
            The number of steps in the analysis.
            The parametric analyzer automatically assigns equal intervals between the steps.
            With this option, there is always a simulation at both `start` and `stop`.
            The value for the `lin` argument must be an integer greater than 0.
            For example, if `start` is 0.5, `stop` is 2.0, and `lin` is 4, the parametric analyzer simulates at values 0.5, 1.0, 1.5, and 2.0.
        log:
            The number of steps between the starting and stopping points at equal-ratio intervals using the following formula: log multiplier = `(stop / start)**(log - 1)`.
            The number of steps can be any positive number, such as 0.5, 2, or 6.25.
            Default value: 5

            For example, if `start` is 3, `stop` is 15, and `log` is 5, the parametric analyzer simulates at values 3, 4.48605, 6.7082, 10.0311, and 15.
            The ratios of consecutive values are equal, as shown below.
            3/4.48605 = 4.48605/6.7082 = 6.7082/10.0311 = 10.0311/15 = 0.67.
        dec:
            The number of steps between the starting and stopping points calculated using the following formula: decade multiplier = `10 ^ (1 / dec)`.
            The number of steps can be any positive number, such as 0.5, 2, or 6.25.
            Default value: 5

            For example, if `start` is 1, `stop` is 10, and `dec` is 5, the parametric analyzer simulates at values 1, 1.58489, 2.51189, 3.98107, 6.30957, and 10.
            The values are `10^0`, `10^0.2`, `10^0.4`, `10^0.6`, `10^0.8`, and `10^1`.
        oct:
            The number of steps between the starting and stopping points using the following formula: `octave?multiplier = 2 ^ (1 / oct)`.
            The number of steps can be any positive number, such as 0.5, 2, or 6.25.
            Default value: 5

            For example, if `start` is 2, `stop` is 4, and `oct` is 5, the parametric analyzer simulates at values 2, 2.2974, 2.63902, 3.03143, 3.4822, and 4.
            These values are `2^1`, `2^1.2`, `2^1.4`, `2^1.6`, `2^1.8`, and `2^2`.
        times:
            A multiplier.
            The parametric analyzer simulates at the points between `start` and `stop` that are consecutive multiples of `times`.

            For example, if `start` is 1, `stop` is 1000, and `times` is 2, the parametric analyzer simulates at values 1, 2, 4, 8, 16, 32, 64, 128, 256, and 512.
        span_percent:
            Range specified as a percentage of the center value.
            For example, if `center` is 100 and `span_percent` is 40, the sweep range extends from 80 to 120.
        sweep_type:
            Type of parametric analysis.

            Valid values are:
                paramset - Runs Parametric Set analysis, specific to Spectre.
                None - Runs Sweeps & Ranges type parametric analysis.
            Default value: None.
        values:
            List of values to be swept.
            You can use `values` by itself or in conjunction with `start`, `stop`, and `step` to specify the set of values to sweep.

    Returns:
        undefined: The return value for this command is undefined

    Raises:
        ValueError: There are problems setting the option.
    """
    if param_analysis_ret is None:
        ret = ws['paramAnalysis'](des_var, **kwargs)
    else:
        ret = ws['paramAnalysis'](des_var, param_analysis_ret, **kwargs)

    if ret is None:
        raise ValueError('There are problems setting the option.')

    return ret


def param_run(param_analysis_ret: None = None, **kwargs):
    """Runs the specified parametric analysis.

    If you do not specify a parametric analysis, all specified analyses are run.
    Distributed processing must be enabled using the hostmode command before parametric analyses can be run in distributed mode.

    When the :func:`param_run()` command finishes, the PSF directory contains a file named `runObjFile` that points to a family of data.
    To plot the family, use a normal plot command. 
    For example, you might use `plot(v("/out"))`.

    Args:
        param_analysis_ret: Parametric analysis
        job_name:
            Used as the basis of the job name.
            The value entered for t_jobName is used as the job name and return value if the run command is successful.
            If the name given is not unique, a number is appended to create a unique job name.
        host:
            Name of the host on which to run the analysis.
            If no host is specified, the system assigns the analysis to an available host.
        drms_cmd:
            A DRMS (Distributed Resource Management System) command, such as a bsub command for LSF or a qsub command for SGE (Sun Grid Engine) used to submit a job.
            When this argument is used, all other arguments, except ?jobName will be ignored.
            Moreover, it will not be possible to call the OCEAN function wait on the jobs submitted using this argument.
            To know more about the command option, refer to the section Submitting a Job in the chapter Using the Distributed Processing Option in the Analog Design Environment of the Virtuoso Analog Distributed Processing OptionUser Guide.
        queue:
            Name of the queue.
            If no queue is defined, the analysis is placed in the default queue (your home machine).
        start_time:
            Desired start time for the job.
            If dependencies are specified, the job does not start until all dependencies are satisfied.
        term_time:
            Termination time for job.
            If the job is not completed by t_termTime, the job is terminated.
        dependent_on:
            List of jobs on which the specified analysis is dependent.
            The analysis is not started until after dependent jobs are complete.
        mail: List of users to be notified by e-mail when the analysis is complete
        block:
            When s_block is not nil, the OCEAN script halts until the job is complete.
            Default value: nil.
        notify:
            When notifyFlag is not nil, a job completion message is echoed to the OCEAN interactive window.
            Default value: t.
        lsf_resouce_str:
            Specifies an LSF Resource Requirement string to submit a job.
            It is effective only in the LSF mode.

    Returns:
        bool: True, if successful

    Raises:
        ValueError: Unsuccessful run.
    """
    if param_analysis_ret is None:
        ret = ws['paramRun'](**kwargs)
    else:
        ret = ws['paramRun'](param_analysis_ret, **kwargs)

    if ret is None:
        raise ValueError('Unsuccessful run.')

    return ret

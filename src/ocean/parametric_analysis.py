def param_analysis():
    """Sets up a parametric analysis.

    Args:
        des_var: Name of the design variable to be swept
        start: Beginning value for the design variable
        stop: Final value for the design variable
        center: Center point for a range of values that you want to sweep
        span:
            Range of values that you want to sweep around the center point.
            For example, if n_center is 100 and n_span is 20 then the sweep range extends from 90 to 110.
        step:
            Increment by which the value of the design variable changes.
            For example, if n_start is 1.
            0, n_stop is 2.
            1, and f_step is 0.
            2, the parametric analyzer simulates at values 1.
            0, 1.
            2, 1.
            4, 1.
            6, 1.
            8, and 2.
            0.
        lin:
            The number of steps in the analysis.
            The parametric analyzer automatically assigns equal intervals between the steps.
            With this option, there is always a simulation at both n_start and n_stop.
            The value for the n_lin argument must be an integer greater than 0.
            For example, if n_start is 0.
            5, n_stop is 2.
            0, and n_lin is 4, the parametric analyzer simulates at values 0.
            5, 1.
            0, 1.
            5, and 2.
            0.
        log:
            The number of steps between the starting and stopping points at equal-ratio intervals using the following formula:

log multiplier = (n_stop/n_start)(n_log -1)The number of steps can be any positive number, such as 0.
            5, 2, or 6.
            25.
            Default value: 5

For example, if n_start is 3, n_stop is 15, and n_log is 5, the parametric analyzer simulates at values 3, 4.
            48605, 6.
            7082, 10.
            0311, and 15.
            The ratios of consecutive values are equal, as shown below.
            3/4.
            48605 = 4.
            48605/6.
            7082 = 6.
            7082/10.
            0311 = 10.
            0311/15 =.
            67.
        dec:
            The number of steps between the starting and stopping points calculated using the following formula:

decade multiplier = 10 1/n_dec

The number of steps can be any positive number, such as 0.
            5, 2, or 6.
            25.
            Default value: 5

For example, if n_start is 1, n_stop is 10, and n_dec is 5, the parametric analyzer simulates at values 1, 1.
            58489, 2.
            51189, 3.
            98107, 6.
            30957, and 10.
            The values are 100, 10.
            2, 10.
            4, 10.
            6, 10.
            8, and 101.
        oct:
            The number of steps between the starting and stopping points using the following formula:

The number of steps can be any positive number, such as 0.
            5, 2, or 6.
            25.
            Default value: 5

For example, if n_start is 2, n_stop is 4, and n_oct is 5, the parametric analyzer simulates at values 2, 2.
            2974, 2.
            63902, 3.
            03143, 3.
            4822, and 4.
            These values are 21, 21.
            2, 21.
            4, 21.
            6, 21.
            8, and 22.
        times:
            A multiplier.
            The parametric analyzer simulates at the points between n_start and n_stop that are consecutive multiples of n_times.
            For example, if n_start is 1, n_stop is 1000, and n_times is 2, the parametric analyzer simulates at values 1, 2, 4, 8, 16, 32, 64, 128, 256, and 512.
        span_percent:
            Range specified as a percentage of the center value.
            For example, if n_center is 100 and n_spanPercent is 40, the sweep range extends from 80 to 120.
        sweep_type:
            Type of parametric analysis.
            Valid values are:


paramset - Runs Parametric Set analysis, specific to Spectre.
            nil - Runs Sweeps & Ranges type parametric analysis.
            Default value: nil.
        values:
            List of values to be swept.
            You can use l_values by itself or in conjunction with n_start, n_stop, and f_step to specify the set of values to sweep.
        param_analysis: Value returned from another paramAnalysis call used to achieve multidimensional parametric analysis

    Returns:
        undefined: The return value for this command is undefined
        nil: Returns nil and prints an error message if there are problems setting the option
    """
    raise NotImplementedError


def param_run():
    """Runs the specified parametric analysis.

    Args:
        param_analysis: Parametric analysis
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
        t: Returned if successful
        nil: Returns nil and prints an error message if unsuccessful
    """
    raise NotImplementedError

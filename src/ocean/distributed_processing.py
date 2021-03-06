from ocean.workspace import ws
from ocean.symbol import *


def delete_job():
    """Removes a job or series of jobs from the text-based job monitor.

    Args:
        job_name: Name used to identify the job
        jobname2...t_jobname_n: Additional jobs that you want to delete

    Returns:
        t: Returns t if successful
        nil: Returns nil and prints an error message if unsuccessful
    """
    raise NotImplementedError


def digital_host_mode():
    """For mixed-signal simulation, specifies whether the digital simulator will run locally or on a remote host.

    Args:
        'local: Sets the simulation to run locally on the user's machine
        'remote:
            Sets the simulation to run on a remote host.
            If you use this argument, you must specify the host name by using the digitalHostName command.

    Returns:
        t: Returns t if successful
        nil: Returns nil and prints an error message if unsuccessful
    """
    raise NotImplementedError


def digital_host_name():
    """For mixed-signal simulation, specifies the name of the remote host for the digital simulator.

    Args:
        name: Name used to identify the host for the digital simulator

    Returns:
        t: Returns t if successful
        nil: Returns nil and prints an error message if unsuccessful
    """
    raise NotImplementedError


def host_mode(value):
    """Sets the simulation host mode.

    Args:
        `value` can be any member of :obj:`HostMode`.

    Returns:
        bool: True, if successful.

    Raises:
        ValueError: Unsuccessful.
    """
    ret = ws['hostMode'](value)

    if ret is None:
        raise ValueError('Unsuccessful.')

    return ret


def host_name():
    """Specifies the name of the remote host.

    Args:
        name: Name used to identify the remote host

    Returns:
        t: Returns t if successful
        nil: Returns nil and prints an error message if unsuccessful
    """
    raise NotImplementedError


def kill_job():
    """Stops processing of a job or a series of jobs.

    Args:
        job_name: Name used to identify the job
        jobname2...t_jobname_n: Additional jobs that you want to stop

    Returns:
        t: Returns t if successful
        nil: Returns nil and prints an error message if unsuccessful
    """
    raise NotImplementedError


def monitor():
    """Monitors the jobs submitted to the distributed system.

    Args:
        task_mode:
            When not nil, multitask jobs are expanded to show individual jobs.
            A multitask job is one that contains several related jobs.

    Returns:
        t: Returns t if successful
        nil: Returns nil and prints an error message if unsuccessful
    """
    raise NotImplementedError


def remote_dir():
    """Specifies the project directory on the remote host to be used for remote simulation.

    Args:
        path: Specifies the path to the project directory on the remote host to be used for remote simulation

    Returns:
        t: Returns t if successful
        nil: Returns nil and prints an error message if unsuccessful
    """
    raise NotImplementedError


def resume_job():
    """Resumes the processing of a previously suspended job or series of jobs.

    The resumeJob command applies only to jobs that are suspended.

    Args:
        job_name: Name used to identify the job
        job_name2...t_job_name_n: Additional jobs that you want to resume

    Returns:
        t: Returns t if successful
        nil: Returns nil and prints an error message if unsuccessful
    """
    raise NotImplementedError


def suspend_job():
    """Suspends the processing of a job or series of jobs.

    The suspendJob command applies only to jobs that are pending or running.

    Args:
        job_name: Name used to identify the job
        job_name2...t_jobname_n: Additional jobs that you want to suspend

    Returns:
        t: Returns t if successful
        nil: Returns nil and prints an error message if unsuccessful
    """
    raise NotImplementedError


def wait(job_names: str | list[str], queue: str = None) -> bool:
    """Postpones processing of a script until the specified jobs complete.

    This command is ignored if distributed processing is not available.

    The wait command is highly useful when you use the non-blocking mode of distributed processing and you want to do some post-processing,
    such as selecting and viewing results after a job is completed.
    The :func:`wait()` command is not required when you use the blocking mode of distributed processing.
    To know more abou tblocking and non-blocking modes of DP, refer to Virtuoso Analog Distributed Processing Option User Guide.

    Args:
        queue: The name of queue on which job launched by func:`wait()` is submitted.
        job_names (list):
            List of names used to identify the jobs.
            The job name is user defined or system generated, depending on how the user submitted the job.

    Returns:
        bool: True, if successful

    Raise:
        ValueError: Unsuccessful.
    """
    args = []

    if queue is not None:
        args += [Key('queue'), queue]

    args += list(job_names)

    ret = ws['wait'](*args)

    if ret is None:
        raise ValueError('Unsuccessful.')

    return ret

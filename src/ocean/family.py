from typing import Any
from ocean.waveform import *


class Family:
    """Family"""

    def __init__(self, family) -> None:
        self.family = family

    def __repr_skill__(self):
        return self.family.__repr_skill__()


def fam_is_family(arg: Any) -> bool:
    """Checks whether the argument specified is a family with at least one waveform.

    Args:
        arg (Any): Any expression.

    Returns:
        bool: True when `arg` is a family.
    """
    return ws['famIsFamily'](arg)


def fam_get_sweep_values(family: Family) -> list:
    """Returns the values of the sweep variable of the family specified.
    
    The returned list is sorted in increasing order.

    Args:
        family (Family): A family name.
    
    Returns:
        list: A list of values of the sweep variable.
    """
    return ws['famGetSweepValues'](family)


def fam_value(family: Family, sweep_value: float) -> Family | RemoteWaveform:
    """Returns the waveform whose `sweep_name` has the value specified using `sweep_value`.

    Args:
        family (Family): A family of waveforms.
        sweep_value (float): The value of sweep to retrieve. This must be an exact match with the value specified using :func:`fam_add_value`.

    Returns:
        Family | RemoteWaveform: The waveform or family whose sweep value was specified in the argument. 
    """
    ret = ws['famValue'](family, sweep_value)

    if fam_is_family(ret):
        return Family(ret)
    else:
        return RemoteWaveform(ret)

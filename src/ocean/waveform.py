from ocean.workspace import ws
from typing import Union
from enum import Enum
import numpy as np


class Prefix(Enum):
    Y = 1e24
    Z = 1e21
    E = 1e18
    P = 1e15
    T = 1e12
    G = 1e9
    M = 1e6
    k = 1e3
    h = 1e2
    da = 1e1
    d = 1e-1
    c = 1e-2
    m = 1e-3
    u = 1e-6
    n = 1e-9
    p = 1e-12
    f = 1e-15
    a = 1e-18
    z = 1e-21
    y = 1e-24


class Waveform:
    """Waveform"""
    pass


class LocalWaveform(Waveform):
    """Local waveform"""

    def __init__(self, x, y) -> None:
        self.x = np.array(x)
        self.y = np.array(y)

    def __iter__(self):
        return iter((self.x, self.y))

    def xprefix(self, prefix: Prefix) -> 'LocalWaveform':
        return LocalWaveform(self.x / prefix.value, self.y)

    def yprefix(self, prefix: Prefix) -> 'LocalWaveform':
        return LocalWaveform(self.x, self.y / prefix.value)


class RemoteWaveform(Waveform):
    """Remote waveform"""

    def __init__(self, waveform) -> None:
        self.waveform = waveform

    def __add__(self, other: Union[float, 'RemoteWaveform']) -> 'RemoteWaveform':
        return RemoteWaveform(ws['plus'](self, other))

    def __sub__(self, other: Union[float, 'RemoteWaveform']) -> 'RemoteWaveform':
        return RemoteWaveform(ws['plus'](self, ws['minus'](other)))

    def __truediv__(self, other: Union[float, 'RemoteWaveform']) -> 'RemoteWaveform':
        return RemoteWaveform(ws['quotient'](self, other))

    def __repr_skill__(self):
        return self.waveform.__repr_skill__()

    def pull(self) -> LocalWaveform:
        """Pull the waveform for further processing in the local environment.

        Args:
            waveform: The waveform to pull.

        Returns:
            Numpy array containing the x and y values of the waveform.
        """
        x, y = ws['abWaveToList'](self.waveform, transpose=True)

        return LocalWaveform(x, y)

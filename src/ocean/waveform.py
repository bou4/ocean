from ocean.workspace import ws
from typing import Union
import numpy as np


class Waveform:
    """Waveform"""

    def __init__(self, waveform) -> None:
        self.waveform = waveform

    def __add__(self, other: Union[float, 'Waveform']) -> 'Waveform':
        return Waveform(ws['plus'](self, other))

    def __sub__(self, other: Union[float, 'Waveform']) -> 'Waveform':
        return Waveform(ws['plus'](self, ws['minus'](other)))

    def __truediv__(self, other: Union[float, 'Waveform']) -> 'Waveform':
        return Waveform(ws['quotient'](self, other))

    def __repr_skill__(self):
        return self.waveform.__repr_skill__()

    def pull(self) -> np.ndarray:
        """Pull the waveform for further processing in the local environment.

        Args:
            waveform: The waveform to pull.

        Returns:
            Numpy array containing the x and y values of the waveform.
        """
        x, y = ws['abWaveToList'](self.waveform, transpose=True)

        return np.array((x, y))

from enum import Enum
from skillbridge import Symbol, Key

class SymbolEnum(Enum):
    def __repr_skill__(self):
        return self.value.__repr_skill__()

from dataclasses import dataclass
from typing import Literal

OptionKind = Literal["call", "put"]
OptionStyle = Literal["european"]  # keep simple for now

@dataclass(frozen=True)
class Option:
    kind: OptionKind
    style: OptionStyle
    K: float
    T: float

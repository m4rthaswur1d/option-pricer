from dataclasses import dataclass

@dataclass(frozen=True)
class Market:
    S0: float     # spot
    r: float      # risk-free rate
    q: float      # dividend yield
    sigma: float  # volatility

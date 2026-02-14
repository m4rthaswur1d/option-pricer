"""
Implementation of Finite Difference Algorithm

The finite difference pricer solves the Black–Scholes partial differential equation
numerically instead of using the closed form formula (already implemented in black-scholes.py.)
The stock price domain is discretized into a grid of stock values and time steps, and the option value is
computed backward in time starting from the terminal payoff at maturity. At each
time step, the spatial derivatives in the Black–Scholes equation are approximated
using central differences, which produces a tridiagonal linear system. The fully
implicit (Backward Euler) time scheme requires solving this linear system at every
time step using the Thomas algorithm. After stepping backward to time t=0, the
option price is obtained by interpolating the grid value at the current spot price.

"""

import math

import numpy as np

from option_pricer.instruments import Option
from option_pricer.market import Market


def payoff_function(mkt: Market, opt: Option, S: float) -> float:
    K = opt.K
    if opt.kind == "call":
        return max(0.0, S - K)
    elif opt.kind == "put":
        return max(0.0, K - S)
    else:
        raise ValueError(f"Unknown option kind: {opt.kind!r}")


def apply_boundaries()

def thomas_solve()

def implicit_fd_pricer()
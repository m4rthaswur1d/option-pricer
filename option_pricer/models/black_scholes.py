"""
Black–Scholes Analytic Pricer

The Black–Scholes pricer computes the value of a European option using the
closed form solution to the Black–Scholes partial differential equation.
The model assumes the underlying asset follows geometric Brownian motion
with constant volatility and interest rates, and that markets are
frictionless and arbitrage-free.

Under these assumptions, the option price can be expressed as a function
of the spot price, strike, time to maturity, risk-free rate, dividend
yield, and volatility through the normal cumulative distribution function.
This implementation evaluates the analytic formula directly, providing a
fast and precise benchmark price used to validate the numerical methods
in the library.
"""

import math
from option_pricer.instruments import Option
from option_pricer.market import Market

def N(x: float):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def bs_price(opt: Option, mkt: Market) -> float:
    S0, K, T = mkt.S0, opt.K, opt.T
    r, q, sigma = mkt.r, mkt.q, mkt.sigma

    if sigma <= 0.0:
        forward = S0 * math.exp((r - q) * T)
        disc_r = math.exp(-r * T)
        if opt.kind == "call":
            return disc_r * max(0.0, forward - K)
        else:
            return disc_r * max(0.0, K - forward)

    # expired option
    if T <= 0.0:
        if opt.kind == "call":
            return max(0.0, S0 - K)
        else:
            return max(0.0, K - S0)

    vol_sqrt_t = sigma * math.sqrt(T)
    d1 = (math.log(S0 / K) + (r - q + 0.5 * sigma ** 2) * T) / vol_sqrt_t
    d2 = d1 - vol_sqrt_t

    disc_q = math.exp(-q * T)
    disc_r = math.exp(-r * T)

    if opt.kind == "call":
        return S0 * disc_q * N(d1) - K * disc_r * N(d2)
    else:
        return K * disc_r * N(-d2) - S0 * disc_q * N(-d1)




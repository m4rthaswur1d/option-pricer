# test, greeks for Black-Scholes

import math
from option_pricer.instruments import Option
from option_pricer.market import Market
from option_pricer.models.black_scholes import bs_price

# standard normal distribution
def N(x: float):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def phi(x:float):
    return math.exp(x**2 / 2) / (math.sqrt(2*math.pi))

def test_bs_greeks_fd():
    # market parameters
    mkt = Market(S0=100.0, r=0.05, q=0.02, sigma=0.25)

    # option parameters
    K = 105.0
    T = 0.5

    call = bs_price(Option(kind="call", style="european", K=K, T=T), mkt)
    put = bs_price(Option(kind="put", style="european", K=K, T=T), mkt)

    vol_sqrt_t = mkt.sigma * math.sqrt(T)
    d1 = (math.log(mkt.S0 / K) + (mkt.r - mkt.q + 0.5 * mkt.sigma ** 2) * T) / vol_sqrt_t
    d2 = d1 - vol_sqrt_t

    discount_q = math.exp(mkt.q * T)
    r = mkt.r

    gamma = discount_q * phi(d1) / (mkt.S0 * mkt.sigma * math.sqrt(T))
    vega = discount_q * mkt.S0 * math.sqrt(T) * phi(d1)

    if call:
        delta_call = discount_q * N(d1)

        theta_call = (
                - (mkt.S0 * discount_q * phi(d1) * mkt.sigma) / (2 * math.sqrt(T))
                + mkt.q * mkt.S0 * discount_q * N(d1)
                - r * K * math.exp(-r * T) * N(d2)
        )

        rho_call = K * T * math.exp(-r * T) * N(d2)

    elif put:
        delta_put = discount_q * (N(d1) - 1)

        theta_put = (
                - (mkt.S0 * discount_q * phi(d1) * mkt.sigma) / (2 * math.sqrt(T))
                - mkt.q * mkt.S0 * discount_q * N(-d1)
                + r * K * math.exp(-r * T) * N(-d2)
        )

        rho_put = -K * T * math.exp(-r * T) * N(-d2)

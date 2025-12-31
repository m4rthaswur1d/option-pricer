import math

from option_pricer.instruments import Option
from option_pricer.market import Market
from option_pricer.models.black_scholes import bs_price

def test_put_call_parity():
    # sample market parameters
    mkt = Market(S0=100.0, r=0.05, q=0.02, sigma=0.25)

    # option parameters
    K = 105.0
    T = 0.5

    call = bs_price(Option(kind="call", style="european", K=K, T=T), mkt)
    put = bs_price(Option(kind="put",  style="european", K=K, T=T), mkt)

    # Put-call parity for continuous dividend yield q:
    # C - P = S0*e^{-qT} - K*e^{-rT}
    rhs = mkt.S0 * math.exp(-mkt.q * T) - K * math.exp(-mkt.r * T)

    assert abs((call - put) - rhs) < 1e-8

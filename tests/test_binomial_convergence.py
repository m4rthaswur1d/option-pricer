import math

from option_pricer.instruments import Option
from option_pricer.market import Market
from option_pricer.models.binomial import binomial_pricer, payoff_function
from option_pricer.models.black_scholes import bs_price


def test_binomial_error_shrinks_vs_black_scholes_call():
    mkt = Market(S0=100.0, r=0.05, q=0.0, sigma=0.2)
    opt = Option(kind="call", style="european", K=100.0, T=1.0)

    bs = bs_price(opt, mkt)

    Ns = [25, 50, 100, 200]
    errors = []
    for N in Ns:
        price = binomial_pricer(opt, mkt, N, payoff_function)
        assert math.isfinite(price)
        errors.append(abs(price - bs))

    assert errors[-1] < errors[0]
    assert errors[-1] < errors[-2]

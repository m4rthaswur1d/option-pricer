import math
from option_pricer.instruments import Option
from option_pricer.market import Market
from option_pricer.models.binomial import binomial_pricer, payoff_function


def test_binomial_price_is_finite_and_nonnegative():
    mkt = Market(S0=100.0, r=0.05, q=0.0, sigma=0.2)
    opt = Option(kind="call", style="european", K=100.0, T=1.0)

    price = binomial_pricer(opt, mkt, N=50, payoff_function=payoff_function)

    assert math.isfinite(price)
    assert price >= 0.0

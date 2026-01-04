import math
from option_pricer.instruments import Option
from option_pricer.market import Market
from option_pricer.models.binomial import binomial_pricer, payoff_function


def test_binomial_expired_call_equals_intrinsic():
    mkt = Market(S0=100.0, r=0.05, q=0.0, sigma=0.2)
    opt = Option(kind="call", style="european", K=90.0, T=0.0)

    price = binomial_pricer(opt, mkt, N=10, payoff_function=payoff_function)
    assert price == 10.0


def test_binomial_expired_put_equals_intrinsic():
    mkt = Market(S0=100.0, r=0.05, q=0.0, sigma=0.2)
    opt = Option(kind="put", style="european", K=110.0, T=0.0)

    price = binomial_pricer(opt, mkt, N=10, payoff_function=payoff_function)
    assert price == 10.0

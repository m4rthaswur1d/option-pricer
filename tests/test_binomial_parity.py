import math
from option_pricer.instruments import Option
from option_pricer.market import Market
from option_pricer.models.binomial import binomial_pricer, payoff_function


def test_binomial_put_call_parity():
    mkt = Market(S0=100.0, r=0.05, q=0.02, sigma=0.25)
    K = 105.0
    T = 0.5
    N = 200

    call = binomial_pricer(Option(kind="call", style="european", K=K, T=T), mkt, N, payoff_function)
    put = binomial_pricer(Option(kind="put",  style="european", K=K, T=T), mkt, N, payoff_function)

    rhs = mkt.S0 * math.exp(-mkt.q * T) - K * math.exp(-mkt.r * T)

    assert abs((call - put) - rhs) < 1e-2

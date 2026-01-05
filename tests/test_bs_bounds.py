# bounds test based on Put-Call Parity for Black-Scholes Pricing

import math
from option_pricer.instruments import Option
from option_pricer.market import Market
from option_pricer.models.black_scholes import bs_price

def test_bs_call_bounds():
    mkt = Market(S0=100.0, r=0.05, q=0.02, sigma=0.25)

    # option parameters
    K = 105.0
    T = 0.5

    r = mkt.r
    q = mkt.q

    call = bs_price(Option(kind="call", style="european", K=K, T=T), mkt)
    put = bs_price(Option(kind="put", style="european", K=K, T=T), mkt)

    if call or put:
        lower = max(0.0, mkt.S0 * math.exp(-q*T) - K * math.exp(-r*T))
        upper = mkt.S0 * math.exp(-q*T)

    assert lower <= call <= upper
    assert lower <= put <= upper

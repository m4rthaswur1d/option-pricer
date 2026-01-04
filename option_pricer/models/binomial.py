import math
from option_pricer.instruments import Option
from option_pricer.market import Market

def payoff_function(mkt: Market, opt: Option, S: float) -> float:
    S0, K, T = mkt.S0, opt.K, opt.T
    r, q, sigma = mkt.r, mkt.q, mkt.sigma
    if opt.kind == "call":
        return max(0.0, S - K)
    elif opt.kind == "put":
        return max(0.0, K - S)
    else:
        raise ValueError(f"Unknown option kind: {opt.kind!r}")

def binomial_pricer(opt: Option, mkt: Market, N, payoff_function) -> float:

    S0, K, T = mkt.S0, opt.K, opt.T
    r, q, sigma = mkt.r, mkt.q, mkt.sigma

    if T <= 0:
        return payoff_function(mkt, opt, S0)

    if N <= 0:
        raise ValueError("N must be a positive integer.")

    dt = T/N

    u = math.exp(sigma*dt**.5)
    d = math.exp(-sigma*dt**.5)

    if u - d <= 0.0:
        raise ValueError("u must be greater than d for binomial model to apply")

    # computer risk-neutral probability
    p = (math.exp((r-q)*dt) - d) / (u-d)

    if not (0.0<= p <= 1):
        raise ValueError(f"Risk-neutral probability out of bounds: p={p:.6f}.")
    ud = u/d
    S = S0 * (d ** N)

    payoffs = []
    # correpsonds only to the maturity layer, computes all the payoffs/option prices
    for _ in range(0, N+1, 1):
        payoff = payoff_function(mkt, opt, S)
        payoffs.append(payoff)
        S = S * ud

    for n in range(N, 0, -1):
        new_payoffs = []
        disc = math.exp(-r * dt)
        for i in range(n):
            option_price = disc * (p * payoffs[i + 1] + (1 - p) * payoffs[i])
            new_payoffs.append(option_price)
        payoffs = new_payoffs

    return float(payoffs[0])












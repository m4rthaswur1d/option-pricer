# Option Pricer

A modular Python library for pricing European options using Binomial Tree and Black–Scholes*models, with a strong emphasis on financial theory validation, numerical correctness, and test-driven development.

This project is designed as a reusable pricing engine rather than a one-off notebook, and includes extensive tests covering arbitrage bounds, parity relations, convergence, and Greeks.

---

## Features

- **Pricing models**
  - Cox–Ross–Rubinstein binomial tree
  - Black–Scholes closed-form solution

- **Financial instruments**
  - European calls and puts

- **Market abstraction**
  - Explicit handling of spot price, interest rate, volatility, and maturity

- **Greeks**
  - Finite-difference approximations for Black–Scholes Greeks

- **Extensive test suite**
  - No-arbitrage bounds
  - Put–call parity
  - Binomial convergence to Black–Scholes
  - Sanity and expiry behavior checks

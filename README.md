# `option-pricer`

A modular Python library for pricing European options using binomial tree, Black–Scholes, and finite-difference PDE methods, with an emphasis on financial theory validation, numerical correctness, and test-driven development.

---

## Features

### Pricing models

* Cox–Ross–Rubinstein binomial tree
* Black–Scholes closed-form solution
* Finite-difference Black–Scholes PDE solver *(in progress)*

### Financial instruments

* European calls and puts

### Market abstraction

Explicit representation of market inputs:

* Spot price $S_0$
* Risk-free rate $r$
* Dividend yield $q$
* Volatility $\sigma$
* Time to maturity $T$

### Greeks

* Analytic Black–Scholes Greeks
* Finite-difference approximations

### Numerical validation

The test suite verifies:

* No-arbitrage bounds
* Put–call parity
* Binomial convergence to Black–Scholes
* Expiry behavior and sanity checks
* PDE convergence to analytic solution (in progress)

---

## Project Structure

```
option_pricer/
│
├── instruments.py        # Option definitions
├── market.py             # Market data container
│
└── models/
    ├── black_scholes.py      # Closed-form analytic pricing
    ├── binomial.py           # Cox–Ross–Rubinstein tree
    └── finite_difference.py  # Black–Scholes PDE solver
```

Tests:

```
tests/
├── Black–Scholes validation tests
├── Binomial convergence tests
└── Finite-difference PDE tests
```

---

## Model Descriptions

### Black–Scholes

The Black–Scholes model prices a European option by assuming the underlying asset follows a geometric Brownian motion under the risk-neutral measure. The option value satisfies a parabolic partial differential equation which admits a closed-form analytic solution. This implementation serves as both a pricing method and the reference solution used to validate numerical schemes.

### Binomial Tree

The Cox–Ross–Rubinstein binomial model discretizes the underlying price process into a recombining tree. At each step the asset moves up or down by fixed factors, and the option value is computed by backward induction under the risk-neutral probability. As the number of time steps increases, the binomial price converges to the Black–Scholes price.

### Finite Difference (PDE)

The Black–Scholes equation can also be solved numerically by discretizing both time and asset price into a grid. The current implementation uses an implicit finite-difference time stepping scheme which requires solving a tridiagonal linear system at each time step. The solver is being validated by convergence tests against the analytic Black–Scholes solution. In progress.
---

## Mathematical Background

Under the risk-neutral measure, the option price $V(S,t)$ satisfies the Black–Scholes PDE:

$$
\frac{\partial V}{\partial t}

* (r - q)S \frac{\partial V}{\partial S}
* \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}

- rV = 0
  $$

with terminal condition:

$$
V(S,T) = \max(S-K,0) \quad \text{(call)}
$$

$$
V(S,T) = \max(K-S,0) \quad \text{(put)}
$$

The finite-difference solver approximates the spatial derivatives using central differences and advances the solution backward in time.

---

## Project Goals

This project demonstrates:

* numerical PDE methods in finance
* convergence analysis
* arbitrage-free validation
* software engineering practices (modular design and testing)

Rather than relying on a single pricing formula, the library compares independent pricing methodologies and verifies they agree under theoretical constraints.

---

## Future Work

* Complete finite-difference solver validation
* Crank–Nicolson scheme
* American options (free boundary problem)
* Implied volatility solver
* Monte Carlo pricing

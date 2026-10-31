# Quantitative Finance Projects

A collection of Python-based quantitative finance projects exploring derivatives pricing, stochastic modeling, portfolio optimization, Monte Carlo simulation, and statistical hypothesis testing.

## 1. European Options Pricing Model

### Project Overview
Developed a Python-based European call option pricing model using Monte Carlo simulation and the Black–Scholes analytical framework to estimate option values and evaluate pricing accuracy.

### Theory
The model simulates stock prices using Geometric Brownian Motion (GBM):

$$dS_t=(r-q)S_tdt+\sigma S_tdW_t$$

where \(r\) is the risk-free interest rate, \(q\) is the dividend yield, and \(\sigma\) is volatility.

European call options are valued by discounting their expected terminal payoff:

$$C=e^{-rT}\mathbb{E}[\max(S_T-K,0)]$$

### How It Was Built
Implemented vectorized Monte Carlo simulations in NumPy to generate 10,000 stock-price paths across 100 time steps using normally distributed random shocks. Calculated discounted terminal option payoffs and implemented an analytical Black–Scholes pricing function using SciPy's normal cumulative distribution function.

### Results
Generated 10,000 simulated stock-price paths to estimate European call option prices and compare Monte Carlo valuations against analytical Black–Scholes predictions. The comparison requires correcting the analytical function's `d1` calculation and incorporating the dividend yield to ensure consistent pricing assumptions.

---

## 2. Kelly Criterion Portfolio Position Sizing Strategy

### Project Overview
Developed a Python-based position-sizing strategy using the Kelly Criterion to optimize long-term compounded wealth growth and evaluate performance against under-sized and over-sized allocations.

### Theory
The Kelly Criterion determines the optimal fraction of capital to allocate to a binary investment by maximizing expected logarithmic wealth growth:

$$f^*=p-\frac{1-p}{b}$$

where \(p\) is the probability of winning and \(b\) is the ratio of profit on a win to loss on a loss.

Strategy performance is measured using average logarithmic growth:

$$g=\frac{1}{N}\ln\left(\frac{W_N}{W_0}\right)$$

### How It Was Built
Implemented 1,000 Monte Carlo trials of 99 investment outcomes using NumPy and SciPy Bernoulli distributions. Compared optimal Kelly allocations against strategies investing 20% and 200% of the Kelly fraction, applying identical investment outcomes across all strategies. Evaluated differences in path-level logarithmic wealth growth using paired Wilcoxon signed-rank tests, rank-biserial effect sizes, and median performance differences.

### Results
The Kelly strategy achieved 0.4258% average logarithmic wealth growth per round, outperforming under-sized allocations on 66.7% of simulated paths and over-sized allocations on 64.9%. Paired Wilcoxon tests demonstrated statistically significant performance differences (p < 10⁻²⁶), supporting the Kelly Criterion's effectiveness in maximizing long-term expected logarithmic wealth growth under the modeled assumptions.

---

## Technologies

Python, NumPy, SciPy, Matplotlib, Monte Carlo Simulation, Stochastic Processes, Statistical Hypothesis Testing, Black–Scholes, Portfolio Optimization.

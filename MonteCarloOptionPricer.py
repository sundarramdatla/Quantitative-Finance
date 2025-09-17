import yfinance as yf
import numpy as np
import math 
import matplotlib.pyplot as plt
import statistics
from scipy.stats import norm


def stock_paths(S, T, r, K, q, sigma, steps, N):
    dt = T / steps
    Z = np.log(S) + np.cumsum((r - q - ((sigma**2)/2)) * dt + sigma * np.sqrt(dt) * np.random.normal(size = (steps,N)), axis = 0 )
    return np.exp(Z)

S = 100
K = 110
T = 1/2
r = .05
q = .02
sigma = .25
steps = 100
N = 10000
paths = stock_paths(S, T, r, K, q, sigma, steps, N)

plt.plot(paths)
plt.xlabel("Time")
plt.ylabel('Stock price')
plt.show()


final_price = paths[-1]
payoffs = np.maximum(final_price - K, 0.0)
mean_payoff = np.mean(payoffs)
option_price = mean_payoff * np.exp(-r * T)




def black_scholes(S, K, r, T, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T ) / sigma * np.sqrt(T)
    d2 = d1 - sigma * np.sqrt(T)
    C = norm.cdf(d1) * S - norm.cdf(d2) * K * np.exp(-r * T)
    return C
print(option_price)
print(black_scholes(S,K,r,T,sigma))

import numpy as np
import pandas as pd

# Optional: Set a random seed for consistent results
np.random.seed(42)

# Step 1: Input data

df = pd.read_excel("C:/Users/anand/Desktop/Maatra Algo Trading/Stock Beta Variance.xlsx")

# Step 2: Simulation setup
n_stocks = 20
n_simulations = 10000
Rf = 0.02               # Risk-free rate
mu_market = 0.15        # Mean market return
sigma_market = 0.0004   # Std dev of market return (small for higher noise influence)

# Step 3: Monte Carlo simulation
portfolio_returns = []

for _ in range(n_simulations):
    Rm = np.random.normal(mu_market, np.sqrt(sigma_market))  # Simulate market return

    stock_returns = []
    for i in range(n_stocks):
        beta = df.loc[i, 'BETA']
        sigma_e = np.sqrt(df.loc[i, 'Variance of Error Term (σ²)'])
        epsilon = np.random.normal(0, sigma_e)
        Ri = Rf + beta * (Rm - Rf) + epsilon  # CAPM formula
        stock_returns.append(Ri)

    Rp = np.mean(stock_returns)  # Equal-weighted portfolio return
    portfolio_returns.append(Rp)

# Step 4: Final Results
portfolio_returns = np.array(portfolio_returns)
expected_return = np.mean(portfolio_returns)
portfolio_std = np.std(portfolio_returns)
portfolio_variance = np.var(portfolio_returns)

# Step 5: Print results
print(f"Number of portfolios: {n_simulations}")
print(f"Simulated Expected Portfolio Return (E[Rp]): {expected_return:.4f}")
print(f"Simulated Portfolio Standard Deviation (σp): {portfolio_std:.4f}")
print(f"Simulated Portfolio Variance (σ²p): {portfolio_variance:.4f}")

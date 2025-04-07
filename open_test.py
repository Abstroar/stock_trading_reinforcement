import numpy as np

portfolio_values = np.load('rl_trader_rewards/test.npy')
print(portfolio_values)
print(f"Average portfolio value: {np.mean(portfolio_values)}")
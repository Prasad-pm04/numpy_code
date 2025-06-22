import numpy as np
import matplotlib.pyplot as plt

# Simulate 30 days of stock prices (e.g., TCS)
np.random.seed(42)
price_start = 1500
daily_returns = np.random.normal(0.001, 0.02, 30)  # mean, std, days
prices = price_start * np.cumprod(1 + daily_returns)

# Calculate statistics
average_price = np.mean(prices)
std_dev = np.std(prices)
daily_change = np.diff(prices)  # day-to-day changes
moving_avg = np.convolve(prices, np.ones(5)/5, mode='valid')

# Print key metrics
print("📊 Stock Analysis:")
print(f"Average Price over 30 days: ₹{average_price:.2f}")
print(f"Standard Deviation (Volatility): ₹{std_dev:.2f}")
print(f"Max Daily Change: ₹{np.max(daily_change):.2f}")
print(f"Min Daily Change: ₹{np.min(daily_change):.2f}")

# Plot the data
plt.plot(prices, label="Stock Price")
plt.plot(range(4, len(moving_avg)+4), moving_avg, label="5-Day Moving Avg", linestyle='--')
plt.title("Simulated Stock Prices")
plt.xlabel("Day")
plt.ylabel("Price (₹)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

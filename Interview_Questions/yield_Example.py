"""
Financial Data Generator with Yield: Stock Price Simulator
    This example uses a generator function with yield to simulate random stock price movements over a specified period.
"""

import random

def generate_stock_prices(initial_price, volatility, num_days):
  """
  Generates random stock prices for a given period.

  Args:
      initial_price: The initial price of the stock.
      volatility: A value representing the daily price fluctuation (higher = more volatile).
      num_days: The number of days for the simulation.

  Yields:
      The stock price for each day in the simulation period.
  """
  current_price = initial_price
  for _ in range(num_days):
    daily_change = random.uniform(-volatility, volatility)  # Random change between -volatility and +volatility
    current_price += current_price * daily_change
    yield current_price  # Pause and yield the current price after each day's change

# Example usage
initial_price = 100
volatility = 0.02  # 2% daily volatility
num_days = 20

stock_prices = generate_stock_prices(initial_price, volatility, num_days)

# Iterate through the generator and print daily prices
for day, price in enumerate(stock_prices):
    print(f"Day {day+1}: ${price:.2f}")


"""
Explanation:

    1. The generate_stock_prices function is a generator.
    2. It takes initial_price, volatility, and num_days as arguments.
    3. It uses a loop to simulate num_days of price changes.
    4. Inside the loop, daily_change is a random value representing the price fluctuation for a day (between -volatility and +volatility).
    5. The current price is updated based on the daily change.
    6. The yield keyword pauses the generator and returns the current price after each day's simulation.
    7. In the example usage, we create a generator object for stock prices.
    8. The for loop iterates over the generator, receiving the day (index) and the stock price for each day.

This example demonstrates how a generator function can be used to simulate and yield financial data (stock prices) one day at a time, promoting memory efficiency compared to storing all prices in a list upfront.

Note: This is a simplified simulation and doesn't represent actual stock market behavior.    
"""
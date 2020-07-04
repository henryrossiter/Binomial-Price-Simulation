import utils
from portfolio import portfolio
import visualizations

# Simulate a price series over 50 intervals
returns = utils.getPositionReturnSeries(portfolio[0], 50)
# Create a gif of the price series
visualizations.getPriceSeriesAnimation(returns)

# Simulate 100 price series' over 100 intervals
returns_arr = [utils.getPositionReturnSeries(portfolio[0], 100) for _ in range(100)]
# Create a gif of the series of price series
visualizations.getMultiplePriceSeriesAnimation(returns_arr)


# Simulate return of entire portfolio over 10 intervals
num_intervals = 10
simulated_portfolio = utils.simulatePortfolioReturn(portfolio, num_intervals)
performance = utils.getPortfolioPerformance(simulated_portfolio)
print('after simulating {} intervals, portfolio value is {} times initial value'.format(num_intervals, performance))
import random
import copy
import visualizations

# Simulate an asset value that either rises by 'upside_delta' with probability 'probability_of_upside'
# or falls by 'downside_delta' with probability 1 - 'probability_of_upside' in each period.
# The simulation is run for 'num_periods' periods
def simulateBinomialPrice(probability_of_upside, upside_delta, downside_delta, num_periods, initial_price = 1, returnSeries=False):
    # Get result of a single pseudo-random bernoulli trial
    # Returns 1 with probability p and 0 with probability 1 - p
    def getBernoulliTrial(p):
        return int(random.random() < p)
    value = initial_price
    values = []
    for _ in range(num_periods):
        value *= (1 + upside_delta) if getBernoulliTrial(probability_of_upside) else (1 - downside_delta)
        values.append(value)
    return values if returnSeries else value

def isValidPosition(position):
    return 'name' in position and 'initial_value' in position and 'probability_of_upside' in position and 'upside_delta' in position and 'downside_delta' in position

def simulatePositionReturn(position, num_periods):
    if not isValidPosition(position):
        print('Invalid position')
        return
    position = copy.deepcopy(position)
    initial_value = position['initial_value']
    final_value = initial_value * simulateBinomialPrice(
        position['probability_of_upside'],
        position['upside_delta'],
        position['downside_delta'],
        num_periods,
    )
    position['final_value'] = final_value
    return position

def getPositionReturnSeries(position, num_periods):
    if not isValidPosition(position):
        print('Invalid position')
        return
    return simulateBinomialPrice(
        position['probability_of_upside'],
        position['upside_delta'],
        position['downside_delta'],
        num_periods,
        initial_price = position['initial_value'],
        returnSeries = True,
    )


def isValidPortfolio(portfolio):
    return all([isValidPosition(position) for position in portfolio])

def simulatePortfolioReturn(portfolio, num_periods):
    if not isValidPortfolio(portfolio):
        print('Invalid portfolio')
        return
    portfolio = copy.deepcopy(portfolio)
    for position in portfolio:
        name = position['name']
        initial_value = position['initial_value']
        final_value = initial_value * simulateBinomialPrice(
            position['probability_of_upside'],
            position['upside_delta'],
            position['downside_delta'],
            num_periods,
        )
        position['final_value'] = final_value
    return portfolio

def getPositionPerformance(position):
    if 'final_value' not in position or 'initial_value' not in position:
        print('Invalid position')
        return
    return position['final_value'] / position['initial_value']

def getPortfolioPerformance(portfolio):
    if not isValidPortfolio(portfolio):
        print('Invalid Portfolio')
        return
    if not all(['final_value' in position for position in portfolio]):
        print('Final portfolio values must be calculated before computing performance')
        return
    initial_portfolio_value = 0
    final_portfolio_value = 0
    for position in portfolio:
        initial_portfolio_value += position['initial_value']
        final_portfolio_value += position['final_value']
    return final_portfolio_value / initial_portfolio_value

def simulatePositionReturnMonteCarlo(position, number_of_simulations=1000, num_periods=12):
    rets = []
    for _ in range(number_of_simulations):
        single_performance = getPositionPerformance(simulatePositionReturn(position, num_periods))
        rets.append(single_performance)
    return rets

def simulatePortfolioReturnMonteCarlo(portfolio, number_of_simulations=1000, num_periods=12):
    rets = []
    for _ in range(number_of_simulations):
        single_performance = getPortfolioPerformance(simulatePortfolioReturn(portfolio, num_periods))
        rets.append(single_performance)
    return rets
 
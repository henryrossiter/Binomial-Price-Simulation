import random
import copy

# Simulate an asset value that either rises by 'upside_delta' with probability 'probability_of_upside'
# or falls by 'downside_delta' with probability 1 - 'probability_of_upside' in each period.
# The simulation is run for 'num_periods' periods
def simulateBinomialPrice(probability_of_upside, upside_delta, downside_delta, num_periods):
    # Get result of a single pseudo-random bernoulli trial
    # Returns 1 with probability p and 0 with probability 1 - p
    def getBernoulliTrial(p):
        return int(random.random() < p)
    value = 1
    for _ in range(num_periods):
        value *= 1 + upside_delta if getBernoulliTrial(probability_of_upside) else 1 - downside_delta
    return value


portfolio = [
    {
        'name': 'TSLA',
        'initial_value': 100,
        'probability_of_upside': 0.5,
        'upside_delta': 0.2,
        'downside_delta': 0.1,
    },
    {
        'name': 'Gold',
        'initial_value': 200,
        'probability_of_upside': 0.5,
        'upside_delta': 0.2,
        'downside_delta': 0.3,
    },
    {
        'name': 'Silver',
        'initial_value': 300,
        'probability_of_upside': 0.8,
        'upside_delta': 0.1,
        'downside_delta': 0.1,
    },
]


def isValidPortfolio(portfolio):
    return all([
        'name' in position
        and 'initial_value' in position
        and 'probability_of_upside' in position
        and 'upside_delta' in position
        and 'downside_delta' in position
        for position in portfolio
    ])

def simulatePortfolioReturn(portfolio, num_periods):
    if not isValidPortfolio(portfolio):
        print('Invalid Portfolio')
        return
    initial_portfolio_value = 0
    final_portfolio_value = 0
    for position in portfolio:
        name = position['name']
        initial_value = position['initial_value']
        final_value = initial_value * simulateBinomialPrice(
            position['probability_of_upside'],
            position['upside_delta'],
            position['downside_delta'],
            num_periods,
        )
        print(name + ' initial value: ' + str(initial_value))
        print(name + ' final value: ' + str(final_value))
        initial_portfolio_value += initial_value
        final_portfolio_value += final_value

    return portfolio
      
simulatePortfolio(portfolio, 1000)

        


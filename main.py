import random

# Get result of a single pseudo-random bernoulli trial
# Returns 1 with probability p and 0 with probability 1 - p
def getBernoulliTrial(p):
    return int(random.random() < p)

# Simulate an asset value that either rises by 'upside_delta' with probability 'probability_of_upside'
# or falls by 'downside_delta' with probability 1 - 'probability_of_upside' in each period.
# The simulation is run for 'num_periods' periods
def simulateBinomialPrice(probability_of_upside, upside_delta, downside_delta, num_periods):
    value = 1
    for _ in range(num_periods):
        value *= 1 + upside_delta if getBernoulliTrial(probability_of_upside) else 1 - downside_delta
    return value


portfolio = [
    {
        'name': 'TSLA',
        'stake': 100,
        'probability_of_upside': 0.5,
        'upside_delta': 0.2,
        'downside_delta': 0.1,
    },
    {
        'name': 'Gold',
        'stake': 200,
        'probability_of_upside': 0.5,
        'upside_delta': 0.2,
        'downside_delta': 0.3,
    },
    {
        'name': 'Silver',
        'stake': 300,
        'probability_of_upside': 0.8,
        'upside_delta': 0.1,
        'downside_delta': 0.1,
    },
]

def simulatePortfolio(portfolio, num_periods):
    initial_portfolio_value = 0
    final_portfolio_value = 0
    for position in portfolio:
        initial_value = position['stake']
        final_value = initial_value * simulateBinomialPrice(
            position['probability_of_upside'],
            position['upside_delta'],
            position['downside_delta'],
            num_periods,
        )
        initial_portfolio_value += initial_value
        final_portfolio_value += final_value
        print(position['name'] + ' initial value: ' + str(initial_value))
        print(position['name'] + ' final value: ' + str(final_value))

    return final_portfolio_value
        
simulatePortfolio(portfolio, 1000)

        


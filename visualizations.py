import matplotlib.pyplot as plt
from matplotlib import animation, rc


def plotReturnDistribution(returns):
    min_return, max_return = min(returns), max(returns)
    print('min return: ' + str(min_return))
    print('max return: ' + str(max_return))

    plt.hist(
        returns,
        bins=list(range(int(min_return // 1), int(max_return // 1 + 1), 1))
    )
    plt.title('Return Distribution ({} Simulations)'.format(len(returns)))
    plt.ylabel('Frequency')
    plt.xlabel('Return')
    plt.show()

def plotSinglePrice(prices, interval):
    plt.plot(prices)
    plt.title('Market Price over Time')
    plt.ylabel('Price')
    plt.xlabel('Interval')
    plt.xlim(0,10)
    plt.show()

def plotPriceSeries(prices, interval):
    for i in range(len(prices)):
        next_plot = plotSinglePrice(prices[:i], interal)

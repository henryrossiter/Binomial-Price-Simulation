import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

def getPriceSeriesAnimation(prices, save = False):
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)

    print('fig size: {0} DPI, size in inches {1}'.format(
        fig.get_dpi(), fig.get_size_inches()))

    line, = ax.plot(prices)
    max_abs_delta = max(
        abs(max(prices) - prices[0]),
        abs(prices[0] - min(prices)),
    )

    ax.set_ylim(
        prices[0] - max_abs_delta,
        prices[0] + max_abs_delta
    )

    ax.set_xlabel('Interval')
    ax.set_ylabel('Price')
    ax.set_title('Binomial Price Simulation')

    def update(i):
        # Update the line and the axes
        line.set_xdata(list(range(i)))
        line.set_ydata(prices[:i])
        return line, ax
    total_intervals = len(prices)
    anim = FuncAnimation(fig, update, frames=np.arange(0, total_intervals), interval=80)
    if save:
        anim.save('prices.gif', dpi=80, writer='imagemagick')
    else:
        # plt.show() will just loop the animation forever.
        plt.show()

def getMultiplePriceSeriesAnimation(prices, save = False):

    highest_price = max([max(price_list) for price_list in prices])

    y_lim = (0, highest_price)
    
    x_lim = (0, len(prices[0]))

    fig = plt.figure()
    ax1 = plt.axes(xlim=x_lim, ylim=y_lim)
    line, = ax1.plot([], [], lw=2)
    
    plt.xlabel('Interval')
    plt.ylabel('Price')
    plt.title('Monte Carlo Price Simulation')

    lines = []
    for _ in range(len(prices)):
        line, = ax1.plot([],[],lw=2)
        lines.append(line)

    def init():
        for line in lines:
            line.set_data([],[])
        return lines

    def update(i):
        # Update the line and the axes
        for ind in range(i):
            lines[ind].set_data(list(range(len(prices[0]))), prices[ind])
        for ind in range(i, len(prices)):
            lines[ind].set_data([],[])
        
        return lines
    total_intervals = len(prices)
    anim = FuncAnimation(fig, update, init_func=init, frames=np.arange(0, total_intervals), interval=50, blit=True)
    if save:
        anim.save('prices.gif', dpi=80, writer='imagemagick')
    else:
        # plt.show() will just loop the animation forever.
        plt.show()

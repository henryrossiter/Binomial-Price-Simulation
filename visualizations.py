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

    # Query the figure's on-screen size and DPI. Note that when saving the figure to
    # a file, we need to provide a DPI for that separately.
    print('fig size: {0} DPI, size in inches {1}'.format(
        fig.get_dpi(), fig.get_size_inches()))

    # Plot a scatter that persists (isn't redrawn) and the initial line.
    # x = np.arange(0, 20, 0.1)
    # ax.scatter(x, x + np.random.normal(0, 3.0, len(x)))

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

        # Update the line and the axes (with a new xlabel). Return a tuple of
        # "artists" that have to be redrawn for this frame.
        line.set_xdata(list(range(i)))
        line.set_ydata(prices[:i])
        return line, ax

    # FuncAnimation will call the 'update' function for each frame; here
    # animating over 10 frames, with an interval of 200ms between frames.
    anim = FuncAnimation(fig, update, frames=np.arange(0, len(prices)), interval=100)
    if save:
        anim.save('prices.gif', dpi=80, writer='imagemagick')
    else:
        # plt.show() will just loop the animation forever.
        plt.show()

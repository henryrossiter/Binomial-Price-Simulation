import utils
from portfolio import portfolio
import livePriceVisualization

returns = utils.getPositionReturnSeries(portfolio[0], 12)
livePriceVisualization.getPriceSeriesAnimation(returns)
        


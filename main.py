import utils
from portfolio import portfolio
import visualizations

returns = utils.getPositionReturnSeries(portfolio[0], 50)
visualizations.getPriceSeriesAnimation(returns, save=True)
        


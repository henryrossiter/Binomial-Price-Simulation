import utils
from portfolio import portfolio
import visualizations

returns = utils.getPositionReturnSeries(portfolio[0], 50)

returns_arr = [utils.getPositionReturnSeries(portfolio[0], 100) for _ in range(100)]    
visualizations.getMultiplePriceSeriesAnimation(returns_arr, save=True)
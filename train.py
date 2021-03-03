
from pandas import read_csv
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARIMAResults
 
def main(N=1):
	# monkey patch around bug in ARIMA class
	def __getnewargs__(self):
		return ((self.endog),(self.k_lags, self.k_diff, self.k_ma))
	ARIMA.__getnewargs__ = __getnewargs__
	 
	# load data
	level_one = read_csv("ABC_Level_One_Tick_Data.csv", index_col='Time_Hour', parse_dates=['Time_Hour'])
	series = level_one['VWAP']

	# fit model with pre-defined parameters
	model = ARIMA(series, order=(1,1,6))
	model_fit = model.fit()

	forecast = model_fit.forecast(steps=N)
	return(forecast)

if __name__ == "__main__":
    main()
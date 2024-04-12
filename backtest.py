import yfinance as yf
import numpy as np


class Backtester():
    def __init__(self, strategy, ticker, interval):
        self.strategy = strategy
        self.ticker = ticker
        self.interval = interval
    
    def get_data(self, period=None, start_date=None, end_date=None):
        if not period == None:
            ticker_data = self.ticker.history(
                period=period,
                interval=self.interval
            )
        else:
            ticker_data = self.ticker.history(
                start=start_date,
                end=end_date,
                interval=self.interval
            )
        
        return ticker_data
    
    def start_test(self, period=None, start_date=None, end_date=None):
        ticker_data = self.get_data(period, start_date, end_date)
        
        print('Starting backtest...')
        equity_curve = np.zeros(len(ticker_data) - 1)
        
        for i in range(len(ticker_data)):
            pass
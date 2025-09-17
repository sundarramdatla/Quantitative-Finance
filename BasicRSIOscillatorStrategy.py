from backtesting import Backtest, Strategy
from backtesting.test import GOOG
import matplotlib.pyplot as plt

from backtesting.lib import crossover, plot_heatmaps, resample_apply
import talib
import seaborn as sns


def custom_optimization_func(s):
    trades = int(s.get('# Trades', 0))
    if trades < 10:
        return -1e9  # strong penalty

    expo = float(s.get('Exposure Time [%]', 0.0)) or 1e-9  # avoid div-by-zero
    return float(s['Equity Final [$]']) / expo


class RsiOscillator(Strategy):
    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    def init(self):
        self.daily_rsi = self.I(talib.RSI, self.data.Close, self.rsi_window)
        self.weekly_rsi = resample_apply("W-FRI", talib.RSI, self.data.Close, self.rsi_window)
        pass
    def next(self):
        if (crossover(self.daily_rsi, self.upper_bound) and self.weekly_rsi[-1] > self.upper_bound):
            self.position.close()
        elif (crossover(self.lower_bound, self.daily_rsi) and self.weekly_rsi[-1] < self.lower_bound):
            self.buy()
        pass


bt = Backtest(GOOG, RsiOscillator,cash = 10_000)

stats = bt.run()
bt.plot()

print(stats)

bt.plot()
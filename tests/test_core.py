import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from quotes_fetcher.core import Symbols



def test_connection():
    symbols = ['AAPL', 'GOOG', 'KO', 'TSLA']
    assert Symbols(' '.join(symbols)).quotes.columns.levels[0].to_list() == symbols

def test_close_price():
    period = {'period_start': '2018-12-15',
              'period_end':'2019-01-28'}
    close_price = [49.34000015258789, 48.33000183105469, 48.31999969482422, 47.900001525878906, 47.540000915527344,
                   47.56999969482422, 45.959999084472656, 46.939998626708984, 47.529998779296875, 47.20000076293945,
                   47.349998474121094, 46.93000030517578, 46.63999938964844, 47.56999969482422, 46.95000076293945,
                   47.47999954223633, 46.56999969482422, 47.06999969482422, 47.34000015258789, 47.150001525878906,
                   47.56999969482422, 46.91999816894531, 47.060001373291016, 47.61000061035156, 47.720001220703125,
                   48.27000045776367, 47.689998626708984, 47.369998931884766]
    assert Symbols('KO', **period).quotes['Close'].to_list() == close_price

def test_close_price_many_symbols():
    symbols = 'AAPL GOOG KO TSLA'
    period = {'period_start': '2018-12-15',
              'period_end':'2019-01-28'}
    close_price = [165.47999572753906, 163.94000244140625, 166.07000732421875, 160.88999938964844, 156.8300018310547,
                   150.72999572753906, 146.8300018310547, 157.1699981689453, 156.14999389648438, 156.22999572753906,
                   157.74000549316406, 157.9199981689453, 142.19000244140625, 148.25999450683594, 147.92999267578125,
                   150.75, 153.30999755859375, 153.8000030517578, 152.2899932861328, 150.0, 153.07000732421875,
                   154.94000244140625, 155.86000061035156, 156.82000732421875, 153.3000030517578, 153.9199981689453,
                   152.6999969482422, 157.75999450683594]
    assert Symbols(symbols, **period).quotes['AAPL']['Close'].to_list() == close_price

def test_open_price_t():
    period = {'period_start': '2018-12-15',
              'period_end': '2019-01-08'}
    open_price = [1049.97998046875, 1037.510009765625, 1026.0899658203125, 1033.989990234375, 1018.1300048828125,
                   1015.2999877929688, 973.9000244140625, 989.010009765625, 1017.1500244140625, 1049.6199951171875,
                   1050.9599609375, 1016.5700073242188, 1041.0, 1032.5899658203125, 1071.5]
    assert Symbols('GOOG', **period).quotes_t.loc['Open'].to_list() == open_price

def test_open_price_many_symbols_t():
    symbols = 'YNDX MSFT BAC'
    period = {'period_start': '2018-12-15',
              'period_end': '2019-01-08'}
    open_price = [108.25, 105.41000366210938, 103.75, 103.6500015258789, 103.05000305175781, 101.62999725341797,
                  97.68000030517578, 95.13999938964844, 99.30000305175781, 102.08999633789062, 101.29000091552734,
                  99.55000305175781, 100.0999984741211, 99.72000122070312, 101.63999938964844]
    assert Symbols(symbols, **period).quotes_t.loc['MSFT'].loc['Open'].to_list() == open_price

def test_metric_avg_close():
    symbols = 'KO TSLA AAPL'
    period = {'period_start': '2018-12-15',
              'period_end': '2019-01-08'}
    assert Symbols(symbols, **period).metrics.loc['AAPL']['Average Close'] == 155.6239990234375

def test_metric_avg_vol():
    symbols = 'KO TSLA AAPL'
    period = {'period_start': '2018-12-15',
              'period_end': '2019-01-08'}
    assert Symbols(symbols, **period).metrics.loc['KO']['Average Vol'] == 15793360.0

def test_metric_avg_dollar_vol():
    symbols = 'KO TSLA AAPL'
    period = {'period_start': '2018-12-15',
              'period_end': '2019-01-08'}
    assert Symbols(symbols, **period).metrics.loc['TSLA']['Avg Day Dollar Trd Vol'] == 2569302854.552053

def test_metric_beta():
    symbols = 'KO TSLA AAPL'
    period = {'period_start': '2018-12-15',
              'period_end': '2019-01-08'}
    assert Symbols(symbols, **period).metrics.loc['KO']['Beta'] == 0.5699910264767483

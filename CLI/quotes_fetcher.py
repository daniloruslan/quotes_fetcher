from quotes_fetcher import Symbols
import argparse
import sys
import os
import pandas as pd

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

def get_args():
    parser = argparse.ArgumentParser(description="This library will allow you to fetch market data for specified list of symbols and time interval. \
                                    The result will be available in two view mode. You will also be able to calculate some metrics for the fetched data. \
                                    Export option will help to save the result to a file.")
    parser.add_argument('-s', '--symbols', type=str, required=True, help='Symbol set to be fetched. Example:"AAPL TSLA IBM"', dest='symbols')
    parser.add_argument('-p', '--period', type=str, help='Period that the data should be fetched for. Valid periods: \
                        1d, 5d, 1mo, 3mo, 1y, 2y, 5y, 10y, ytd, etc', dest='period', default='1mo')
    parser.add_argument('-ps', '--period_start', type=str, help='Start of period that the data should be fetched for. Format: "YYYY-MM-DD". \
                        Used together with --period_end instead of --period', dest='period_start')
    parser.add_argument('-pe', '--period_end', type=str, help='End of period that the data should be fetched for. Format: "YYYY-MM-DD. \
                            Used together with --period_start instead of --period', dest='period_end')
    parser.add_argument('-t', '--transpose', type=str2bool, help='Bool Flag: Transpose quotes table', dest='transpose',
                        default=False)
    parser.add_argument('-m', '--metrics', type=str2bool, help='Bool Flag: Calculate the following metrics: Average Close Price,  \
                            Average Volume, Average Daily Dollar Trade Volume (addtv), Beta-coefficient',
                        dest='metrics', default=False)
    parser.add_argument('-o', '--output', type=str, help='Export data to a csv file',
                        dest='output')

    args = parser.parse_args()
    return args


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def choice(obj, args):
    if args.metrics:
        return obj.metrics
    elif args.transpose:
        return obj.quotes_t
    else:
        return obj.quotes


def export_data(df, output):
    dest_dir = 'quotes_output'
    if dest_dir not in os.listdir():
        os.makedirs(dest_dir)
    dest_path = os.path.join(dest_dir, output)
    df.to_csv(dest_path, decimal='.', sep='|',
              float_format='%.2f', index=True)
    print("The data has been exported to {}".format(dest_path))


def main():
    args = get_args()

    if args.metrics and args.transpose:
        sys.exit("So, metrics or transposed quotes table? Please choose one option.")
    else:
        quotes = Symbols(args.symbols, period=args.period, period_start=args.period_start,
                         period_end=args.period_end)
        result = choice(quotes, args)
        print(result)

    if args.output:
        export_data(result, args.output)


if __name__ == '__main__':
    main()

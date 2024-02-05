import warnings
# Suppress yfinance TimedeltaIndex warning
warnings.simplefilter(action='ignore', category=FutureWarning)

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import mplcursors


def get_nifty_50_symbols():
    # List of Nifty 50 symbols
    nifty_50_symbols = ['ADANIPORTS.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJFINANCE.NS',
                        'BAJAJFINSV.NS',
                        'BHARTIARTL.NS', 'BPCL.NS', 'CIPLA.NS', 'COALINDIA.NS', 'DIVISLAB.NS', 'DRREDDY.NS',
                        'EICHERMOT.NS',
                        'GRASIM.NS', 'HCLTECH.NS', 'HDFC.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS',
                        'HINDALCO.NS',
                        'HINDUNILVR.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 'INFY.NS', 'IOC.NS', 'ITC.NS', 'JSWSTEEL.NS',
                        'KOTAKBANK.NS', 'LT.NS', 'M&M.NS', 'MARUTI.NS', 'NESTLEIND.NS', 'NTPC.NS', 'ONGC.NS',
                        'POWERGRID.NS',
                        'RELIANCE.NS', 'SBILIFE.NS', 'SBIN.NS', 'SHREECEM.NS', 'SUNPHARMA.NS', 'TATACONSUM.NS',
                        'TATAMOTORS.NS',
                        'TATASTEEL.NS', 'TCS.NS', 'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS', 'UPL.NS', 'WIPRO.NS',
                        'JSWSTEEL.NS']

    return nifty_50_symbols


def get_stock_data(symbol, start_date, end_date):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None


def plot_stock_prices(data, symbol):
    if data is None:
        return

    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot Close Price
    ax.plot(data['Close'], label=symbol + ' Close Price')

    # Find and plot 52-Week Low within the specified date range
    if not data.empty:
        low_price_date = data['Low'].idxmin()
        low_price_value = data['Low'][low_price_date]

        # Add a red circle at the point of the 52-week low
        ax.scatter(low_price_date, low_price_value, color='red', label=symbol + ' 52-Week Low')

        # Draw a horizontal line for comparison
        ax.axhline(y=low_price_value, linestyle='dashed', color='red', label=symbol + ' 52-Week Low')

        # Annotate the point with the exact date
        ax.annotate(f"{low_price_date.strftime('%Y-%m-%d')}", xy=(low_price_date, low_price_value),
                    xytext=(10, 10), textcoords='offset points',
                    arrowprops=dict(facecolor='red', arrowstyle='wedge,tail_width=0.7'), color='red')

    ax.set_title(symbol + ' Stock Prices (Feb 2023 to Feb 2024)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Stock Price (INR)')
    ax.legend()

    # Add cursor functionality
    mplcursors.cursor(hover=True)

    plt.show()


def find_stocks_closest_to_low(nifty_50_symbols, start_date, end_date):
    closest_to_low = []

    for symbol in nifty_50_symbols:
        data = get_stock_data(symbol, start_date, end_date)
        if data is not None and not data.empty:
            current_price = data['Close'][-1]
            low_price = data['Low'].min()
            low_price_date = data['Low'].idxmin()

            closest_to_low.append((symbol, current_price, low_price, low_price_date))

    # Sort the list by the difference between the current price and 52-week low
    closest_to_low.sort(key=lambda x: abs(x[1] - x[2]))

    return closest_to_low[:10]


if __name__ == "__main__":
    nifty_50_symbols = get_nifty_50_symbols()
    start_date = '2023-02-01'
    end_date = '2024-02-01'

    closest_to_low = find_stocks_closest_to_low(nifty_50_symbols, start_date, end_date)

    print("Top 10 stocks closest to their 52-week low in Feb 2024:")
    for stock in closest_to_low:
        print(
            f"{stock[0]} - Current Price: {stock[1]}, 52-Week Low: {stock[2]} (Date: {stock[3].strftime('%Y-%m-%d')})")
        data = get_stock_data(stock[0], start_date, end_date)
        plot_stock_prices(data, stock[0])

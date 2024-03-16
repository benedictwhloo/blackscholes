import math
import scipy
from scipy.stats import norm
import yfinance as yf
import numpy as np
import pandas_datareader.data as web

def black_scholes(S, K, T, r, sigma, option_type):
    """
    Calculates the theoretical option price using the Black-Scholes model.
    
    Args:
        S (float): The current stock price
        K (float): The strike price
        T (float): The time to maturity (in years)
        r (float): The risk-free interest rate
        sigma (float): The volatility of the underlying asset
        option_type (str): Either 'call' or 'put'
        
    Returns:
        float: The theoretical option price
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    if option_type.lower() == 'call':
        price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type.lower() == 'put':
        price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Option type must be 'call' or 'put'")
    
    return price

def calculate_volatility(ticker, period='1y'):
    """
    Calculates the annualized volatility of a stock based on daily log returns.
    
    Args:
        ticker (str): The stock ticker symbol
        period (str): The period for which historical data should be fetched (e.g., '1y', '6m', '1d')
        
    Returns:
        float: The annualized volatility
    """
    stock = yf.Ticker(ticker)
    historical_data = stock.history(period=period)
    daily_log_returns = np.log(historical_data['Close'] / historical_data['Close'].shift(1))
    volatility = daily_log_returns.std() * np.sqrt(252)  # Annualized volatility
    return volatility

def get_treasury_rate():
    """
    Fetches the current 3-month US Treasury Bill rate.
    
    Returns:
        float: The 3-month US Treasury Bill rate
    """
    treasury_data = web.DataReader('DTB3', 'fred', start='2023-03-01', end='2023-03-16')
    treasury_rate = treasury_data.iloc[-1]['DTB3'] / 100  # Convert from percentage to decimal
    return treasury_rate

# Example usage
ticker = input("Enter the stock ticker symbol: ")
stock = yf.Ticker(ticker)

# Get the current stock price
try:
    S = stock.info['regularMarketPrice']
except KeyError:
    S = stock.info['currentPrice']

# Prompt the user for the remaining variables
K = float(input("Enter the strike price: "))
T = float(input("Enter the time to maturity (in years): "))
option_type = input("Enter the option type ('call' or 'put'): ")

# Calculate the volatility using historical data
sigma = calculate_volatility(ticker)

# Get the 3-month US Treasury Bill rate
r = get_treasury_rate()

option_price = black_scholes(S, K, T, r, sigma, option_type)
print(f"The theoretical option price for {ticker} is: {option_price:.2f}")
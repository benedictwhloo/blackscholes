<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">   
</head>
<body>
    <h1>Black-Scholes Option Pricing Model (NOT FINANCIAL ADVICE)</h1>
    <p>This Python script implements the Black-Scholes model for calculating the theoretical price of European-style options. The Black-Scholes model is a widely used mathematical model for pricing options, taking into account factors such as the current stock price, strike price, time to expiration, risk-free interest rate, and volatility of the underlying asset.</p>
    <h2>Features</h2>
    <ul>
        <li>Calculates the theoretical option price for both call and put options</li>
        <li>Automatically retrieves the current stock price and volatility from Yahoo Finance</li>
        <li>Fetches the 3-month US Treasury Bill rate as the risk-free interest rate</li>
        <li>User-friendly interface for entering required variables</li>
    </ul>
    <h2>Prerequisites</h2>
    <ul>
        <li>Python 3.x</li>
        <li>The following Python libraries:
            <ul>
                <li><code>yfinance</code></li>
                <li><code>numpy</code></li>
                <li><code>scipy</code></li>
                <li><code>pandas-datareader</code></li>
            </ul>
        </li>
    </ul>
    <p>You can install the required libraries using pip:</p>
    <pre><code>pip install yfinance numpy scipy pandas-datareader</code></pre>
    <h2>Usage</h2>
    <ol>
        <li>Run the Python script: <code>blackscholes.py</code></li>
        <li>Enter the stock ticker symbol when prompted.</li>
        <li>Enter the strike price.</li>
        <li>Enter the time to maturity (in years).</li>
        <li>Enter the option type ('call' or 'put').</li>
    </ol>
    <p>The script will automatically fetch the current stock price, calculate the volatility based on historical data, and retrieve the 3-month US Treasury Bill rate as the risk-free interest rate.</p>
    <p>After providing the required inputs, the script will output the theoretical option price using the Black-Scholes model.</p>
    <h2>Function Descriptions</h2>
    <h3><code>black_scholes(S, K, T, r, sigma, option_type)</code></h3>
    <p>This function calculates the theoretical option price using the Black-Scholes model.</p>
    <ul>
        <li><code>S</code> (float): The current stock price</li>
        <li><code>K</code> (float): The strike price</li>
        <li><code>T</code> (float): The time to maturity (in years)</li>
        <li><code>r</code> (float): The risk-free interest rate</li>
        <li><code>sigma</code> (float): The volatility of the underlying asset</li>
        <li><code>option_type</code> (str): Either 'call' or 'put'</li>
    </ul>
    <p>Returns the theoretical option price as a float.</p>
    <h3><code>calculate_volatility(ticker, period='1y')</code></h3>
    <p>This function calculates the annualized volatility of a stock based on daily log returns.</p>
    <ul>
        <li><code>ticker</code> (str): The stock ticker symbol</li>
        <li><code>period</code> (str): The period for which historical data should be fetched (e.g., '1y', '6m', '1d')</li>
    </ul>
    <p>Returns the annualized volatility as a float.</p>
    <h3><code>get_treasury_rate()</code></h3>
    <p>This function fetches the current 3-month US Treasury Bill rate from the Federal Reserve Economic Data (FRED) database.</p>
    <p>Returns the 3-month US Treasury Bill rate as a float.</p>
    <h2>License</h2>
    <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
    <h2>Contributing</h2>
    <p>Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.</p>
</body>

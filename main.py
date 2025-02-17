'''
Name: Churong'David'Wei
Class: INF601_VA
Project: miniproject1
'''


'''
INF601 - Programming in Python
Assignment # mini project 1
I,     Churong'David'Wei    , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''


# import required libraries
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import os

# Define stock tickers
tickers = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"]

# Collect stock data
data = {}
for ticker in tickers:
    stock = yf.Ticker(ticker)
    history = stock.history(period="10d")
    data[ticker] = history["Close"].values  # Store closing prices

# Convert to NumPy array
stock_array = np.array([data[t] for t in tickers])

# Ensure the 'charts' directory exists, if not, create it
os.makedirs("charts", exist_ok=True)

# Plot and save graphs to the designated path
for i, ticker in enumerate(tickers):
    plt.figure(figsize=(8, 5))
    x= range(1,11)
    plt.plot(x, stock_array[i], marker="o", linestyle="-", label=ticker)
    plt.xticks(x, x[::1])
    plt.xlabel("Days")
    plt.ylabel("Closing Price (USD)")
    plt.title(f"Stock Prices of {ticker}")
    plt.legend()
    plt.grid()

    plt.savefig(f"charts/{ticker}.png")
    plt.close()

print("Graphs saved in 'charts/' directory.")

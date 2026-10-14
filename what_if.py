import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

MONTHLY = 100
START = "2015-01-01"
TICKER = "IWDA.AS"

prices = yf.download(TICKER, start=START, interval="1mo", auto_adjust=True)["Close"]
prices = prices.squeeze().dropna()

units_bought = MONTHLY / prices
total_units = units_bought.cumsum()
portfolio_value = total_units * prices

invested = pd.Series(range(1, len(prices) + 1), index=prices.index) * MONTHLY

print(f"Μήνες αποταμίευσης: {len(prices)}")
print(f"Έβαλες από την τσέπη σου: {invested.iloc[-1]:,.0f}€")
print(f"Αξία επένδυσης σήμερα: {portfolio_value.iloc[-1]:,.0f}€")

plt.plot(invested, label="Στο στρώμα")
plt.plot(portfolio_value, label="Σε παγκόσμιο ETF")
plt.title(f"{MONTHLY}€ τον μήνα από το {START[:4]}")
plt.ylabel("€")
plt.legend()
plt.show()
import yfinance as yf

spy = yf.Ticker("SPY")
df = spy.history(start="2026-01-01", auto_adjust=True)

df_prices = df.drop(columns=["Dividends", "Stock Splits", "Capital Gains"], errors="ignore")

print(df_prices.head(10))

averages = df_prices.mean().to_frame(name="Average").T
print("\nColumn Averages:")
print(averages)
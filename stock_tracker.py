"""
Stock Portfolio Tracker for Datheon Python Internship.
Task 2: Hardcoded stock prices using standard library.
"""

STOCK_PRICES = {
    "AAPL": 180.50,
    "TSLA": 240.20,
    "MSFT": 410.00,
    "GOOGL": 175.30,
    "AMZN": 185.00,
    "NVDA": 120.80
}

def display_portfolio(portfolio: dict) -> float:
    print("\n" + "=" * 50)
    print(f"{'Stock':<10} {'Shares':<10} {'Price ($)':<12} {'Total Value ($)':<12}")
    print("=" * 50)
    
    total_portfolio_value = 0.0
    for symbol, shares in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = shares * price
        total_portfolio_value += value
        print(f"{symbol:<10} {shares:<10} {price:<12.2f} {value:<12.2f}")
        
    print("=" * 50)
    print(f"Total Portfolio Value: ${total_portfolio_value:,.2f}")
    print("=" * 50 + "\n")
    return total_portfolio_value

def main() -> None:
    print("=== Stock Portfolio Tracker ===")
    print("Available Tickers:", ", ".join(STOCK_PRICES.keys()))
    portfolio = {}
    
    while True:
        symbol = input("\nEnter Stock Ticker (or 'done' to finish): ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print(f"Invalid ticker! Select from: {', '.join(STOCK_PRICES.keys())}")
            continue
            
        try:
            shares = float(input(f"Enter number of shares for {symbol}: "))
            if shares <= 0:
                print("Shares must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        portfolio[symbol] = portfolio.get(symbol, 0.0) + shares
        print(f"Added {shares} shares of {symbol}.")
        
    if portfolio:
        display_portfolio(portfolio)
    else:
        print("\nNo stocks added.")

if __name__ == "__main__":
    main()

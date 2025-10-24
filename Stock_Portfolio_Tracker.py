import csv

def stock_portfolio_tracker():
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 130, "AMZN": 140, "MSFT": 320}
    portfolio = []
    total_value = 0

    print("📈 Stock Portfolio Tracker\n")
    while True:
        stock = input("Enter stock symbol (AAPL/TSLA/GOOGL/AMZN/MSFT or 'done'): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("❌ Invalid stock symbol.")
            continue

        qty = int(input("Enter quantity: "))
        value = stock_prices[stock] * qty
        total_value += value
        portfolio.append([stock, qty, value])

    print("\nYour Portfolio:")
    for stock, qty, value in portfolio:
        print(f"{stock} - Qty: {qty}, Value: ${value}")

    print(f"\n💵 Total Investment Value: ${total_value}")

    save = input("\nSave results to CSV? (y/n): ").lower()
    if save == 'y':
        with open("portfolio.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Value"])
            writer.writerows(portfolio)
            writer.writerow(["Total", "", total_value])
        print("✅ Saved to portfolio.csv")

if __name__ == "__main__":
    stock_portfolio_tracker()

import requests

# Coin mapping
SYMBOL_MAP = {
    "ethereum": "ETH",
    "bitcoin": "BTC"
}

def get_oracle_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[coin]["usd"]

def get_market_price(coin):
    symbol = SYMBOL_MAP[coin]
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
    response = requests.get(url)
    data = response.json()
    return float(data["price"])

def calculate_risk(oracle, market):
    difference = abs(oracle - market) / oracle * 100

    if difference > 5:
        risk = "🔴 High Risk (Possible Manipulation)"
    elif difference > 2:
        risk = "🟠 Medium Risk (Suspicious)"
    else:
        risk = "🟢 Low Risk (Normal)"

    return round(difference, 2), risk

def main():
    print("\n🔍 Kee3 - DeFi Oracle Risk Scanner\n")

    coin = input("Enter coin (ethereum/bitcoin): ").lower()

    if coin not in SYMBOL_MAP:
        print("❌ Unsupported coin")
        return

    try:
        oracle_price = get_oracle_price(coin)
        market_price = get_market_price(coin)

        difference, risk = calculate_risk(oracle_price, market_price)

        print("\n📊 Analysis Result")
        print(f"Coin: {coin.upper()}")
        print(f"Oracle Price (CoinGecko): ${oracle_price}")
        print(f"Market Price (Binance): ${round(market_price, 2)}")
        print(f"Difference: {difference}%")
        print(f"Status: {risk}")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
 # 🚀 Kee3 
 # DeFi Oracle Risk Scanner

## 📌 Introduction

In modern decentralized finance (DeFi), smart contracts rely heavily on external data such as asset prices. This data is provided through oracles, which connect blockchain systems with real-world information.

However, improper handling of price data and flawed business logic can lead to critical vulnerabilities.

---

## 🪙 What is Cryptocurrency?

Cryptocurrency is a digital currency that operates on blockchain technology. Unlike traditional systems, it is:

- Decentralized (no central authority)
- Transparent
- Secure through cryptography

Examples:

- Bitcoin (BTC)
- Ethereum (ETH)

---

## 🔐 OWASP Top 10 (Blockchain Context)

This project is inspired by common smart contract vulnerabilities similar to OWASP risks.

🔹 Price Oracle Manipulation

A vulnerability where attackers manipulate the price feed used by smart contracts.

👉 Example:

- Attacker changes price on a low-liquidity exchange
- Oracle picks the manipulated price
- Smart contract uses incorrect value → leads to loss

---

##🔹 Business Logic Errors

These occur when the application logic is flawed.

👉 Example:

- Incorrect loan calculation
- Improper validation of collateral
- Missing checks in smart contracts

---

## ⚠️ Problem Statement

Smart contracts trust external price feeds.
If the price data is manipulated, the system may:

- Issue incorrect loans
- Allow unfair trades
- Lose funds

---

## 🛠️ About Kee3

Kee3 is a Python-based security tool that detects potential price manipulation risks by comparing:

- Oracle Price (CoinGecko)
- Market Price (Binance)

---

## ⚙️ How It Works

1. User inputs a cryptocurrency (e.g., Ethereum)
2. Tool fetches:
   - Oracle price from CoinGecko
   - Market price from Binance
3. It calculates the percentage difference
4. Based on deviation, it assigns a risk level:

Difference| Risk Level
0–2%| Low Risk ✅
2–5%| Medium Risk ⚠️
>5%| High Risk 🚨

---

## 📊 Example Output

Coin: ETHEREUM
Oracle Price: $2341
Market Price: $2335
Difference: 0.25%
Status: Low Risk

---

## 👥 Who Can Use This Tool?

- 🧑‍💻 DeFi Developers
- 🔍 Security Researchers
- 💰 Bug Bounty Hunters
- 📈 Crypto Traders
- 🛡️ Smart Contract Auditors

---

## 🎯 Use Cases

- Detect oracle manipulation risks
- Analyze price inconsistencies
- Identify arbitrage opportunities
- Assist in smart contract audits

---

## 💡 Benefits

- Simple and easy to use
- Real-time price comparison
- Helps detect critical vulnerabilities
- Useful for learning blockchain security
- Beginner-friendly yet powerful

---

## 🧪 Tech Stack

- Python
- CoinGecko API
- Binance API

---

## 🚀 Future Improvements

- Integration with DEX (Uniswap)
- Flash loan detection
- Web dashboard (UI)
- Real-time alerts

---

## 🏁 Conclusion

Kee3 is a foundational step towards building advanced DeFi security tools.
It demonstrates how simple comparisons can help identify complex vulnerabilities in blockchain systems.

---

## 👨‍💻 Author

Developed by Manasvi  
Cybersecurity & Blockchain Enthusiast


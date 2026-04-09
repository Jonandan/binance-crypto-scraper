import requests
import csv

url="https://api.binance.com/api/v3/ticker/24hr"

response = requests.get(url)

data=response.json()

with open("data.csv","w",newline="",encoding="utf-8") as file:
    writer=csv.writer(file)

    writer.writerow(["Symbol","Price","Volume"])

    for coin in data:
        writer.writerow([
            coin["symbol"],
            coin["lastPrice"],
            coin["volume"]
        ])

print("Data saved in data.csv")
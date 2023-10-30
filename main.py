import time
import csv
from web3 import Web3

scroll = {"rpc": "https://scroll.blockpi.network/v1/rpc/public",
          "scan": "https://scrollscan.com/tx",
          "token": "ETH", "chain_id": 534352}

w3 = Web3(Web3.HTTPProvider(scroll['rpc']))

with open("wallets.txt", "r") as file:
    key = [row.strip() for row in file]

def tx_cheker(privatekey):
    account = w3.eth.account.from_key(privatekey)
    wallet = Web3.to_checksum_address(account.address)
    nonce = w3.eth.get_transaction_count(wallet)
    return wallet, nonce

def write_to_csv(results):
    with open("result.csv", "w", newline='') as csvfile:
        fieldnames = ["Wallet", "Nonce"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in results:
            writer.writerow({"Wallet": result[0], "Nonce": result[1]})

def main():
    results = []
    for privatekey in key:
        result = tx_cheker(privatekey)
        results.append(result)
        print(f"Wallet: {result[0]}, Nonce: {result[1]}")
        time.sleep(1)

    write_to_csv(results)

if __name__ == "__main__":
    main()

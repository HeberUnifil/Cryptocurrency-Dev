from blockchain import *
from time import time
import pprint

pp = pprint.PrettyPrinter(indent=4)

Blockchain = Blockchain()
key = Blockchain.generateKeys()

# print(key)
# print("")

print(len(Blockchain.pendingTransactions))

# Blockchain.minePendingTransactions("Ariel")
Blockchain.addTransaction("Heber", "Lenhador", 50, 10, key, key)
print(len(Blockchain.pendingTransactions))

Blockchain.minePendingTransactions("Ariel")
print(Blockchain.getBalance("Heber"))

Blockchain.addTransaction("Heber", "Lenhador", 20, 5, key, key)
Blockchain.addTransaction("Heber", "Lenhador", 10, 5, key, key)

Blockchain.minePendingTransactions("Ariel")

print(len(Blockchain.pendingTransactions))

# print(Blockchain.chain)

pp.pprint(Blockchain.chainJSONencode())
# print("Length: ", len(Blockchain.chain))


# print(Blockchain.pendingTransactions)
# pp.pprint(Blockchain.pendingTransactions)

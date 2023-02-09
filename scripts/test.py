from blockchain import *
from time import time
import pprint

pp = pprint.PrettyPrinter(indent=4)

Blockchain = Blockchain()
key = Blockchain.generateKeys()

# print(key)
# print("")


print(Blockchain.pendingTransactions)

# Blockchain.minePendingTransactions("Ariel")
Blockchain.addTransaction("Heber", "Lenhador", 20, key, key)
Blockchain.minePendingTransactions("Ariel")

Blockchain.addTransaction("Heber", "Lenhador", 100, key, key)


# print(Blockchain.chain)

pp.pprint(Blockchain.chainJSONencode())
print("Length: ", len(Blockchain.chain))


print(Blockchain.getBalance("Heber"))
# print(Blockchain.pendingTransactions)

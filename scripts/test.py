from blockchain import *
from time import time
import pprint

pp = pprint.PrettyPrinter(indent=4)

Blockchain = Blockchain()
key = Blockchain.generateKeys()

print(key)
print("")

Blockchain.addTransaction("Heber", "Lenhador", 10, key, key)
# Blockchain.pendingTransactions.append(transaction)

Blockchain.minePendingTransactions("Ariel")


# transactions = []

# block = Block(transactions, time(), 0)
# Blockchain.addBlock(block)

# block = Block(transactions, time(), 1)
# Blockchain.addBlock(block)

# block = Block(transactions, time(), 2)
# Blockchain.addBlock(block)

pp.pprint(Blockchain.chainJSONencode())
print("Length: ", len(Blockchain.chain))

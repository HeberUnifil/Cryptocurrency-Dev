from blockchain import *
from time import time
import pprint

pp = pprint.PrettyPrinter(indent=4)

Blockchain = Blockchain()
key = Blockchain.generateKeys()

# print(key)
# print("")

# print(len(Blockchain.pendingTransactions))
Blockchain.addTransaction("Heber", "Lenhador", 50, 1, key, key)
Blockchain.addTransaction("Heber", "Lenhador", 48, 1, key, key)
Blockchain.addTransaction("Heber", "Lenhador", 5, 1, key, key)

Blockchain.minePendingTransactions("Ariel")

print("Balanço Heber: ", Blockchain.getBalance("Heber"))
print("Balanço Lenhador: ", Blockchain.getBalance("Lenhador"))
print(
    "Balanço Ariel: ",
    Blockchain.getBalance(
        "Ariel",
    ),
    "\n#############",
)
# print(Blockchain.pendingTransactions)

pp.pprint(Blockchain.chainJSONencode())
print(Blockchain.getLastBlock().hash)
# pp.pprint(Blockchain.pendingTransactions)

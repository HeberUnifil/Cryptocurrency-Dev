from blockchain import *
from time import time
import pprint

pp = pprint.PrettyPrinter(indent=4)

Blockchain = Blockchain()
transactions = []

# block = Block(transactions, time(), 0)
# Blockchain.addBlock(block)

# block = Block(transactions, time(), 1)
# Blockchain.addBlock(block)

# block = Block(transactions, time(), 2)
# Blockchain.addBlock(block)

pp.pprint(Blockchain.chainJSONencode())
print("Length: ", len(Blockchain.chain))

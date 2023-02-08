import hashlib
import json
from textwrap import dedent
from uuid import uuid4
import jsonpickle
from flask import Flask
from urllib.parse import urlparse
from Crypto.PublicKey import RSA
from Crypto.Signature import *
from time import time
from datetime import datetime
import requests


class Blockchain(object):
    # Inicializa a blockchain
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
        # Blockchains possuem suas transações organizadas em fila, é necessário inicializar uma lista
        self.difficulty = 2
        self.minerRewards = 50
        # Transação como recompensa de por mineração
        self.blockSize = 10
        self.nodes = set()

    def minePendingTransactions(self, miner):
        lenPT = len(self.pendingTransactions)
        # if(lenPT <= 1):
        #     print("Not enough transactions to mine! (Must be > 1)")
        #     return False;
        # else:
        for i in range(0, lenPT, self.blockSize):
            end = i + self.blockSize
            if i >= lenPT:
                end = lenPT

            transactionSlice = self.pendingTransactions[i:end]

            newBlock = Block(
                transactionSlice,
                datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                len(self.chain),
            )
            # print(type(self.getLastBlock()));

            hashVal = self.getLastBlock().hash
            newBlock.prev = hashVal
            newBlock.mineBlock(self.difficulty)
            self.chain.append(newBlock)
        print("Mining Transactions Success!")

        payMiner = Transaction("Miner Rewards", miner, self.minerRewards)
        self.pendingTransactions = [payMiner]
        return True

    # Busca pelo bloco anterior da cadeia
    def getLastBlock(self):
        return self.chain[-1]

    # Cria um novo bloco na cadeia, se baseando no bloco anterior, caso não haja um, sinaliza como bloco anterior vazio
    def addBlock(self, block):
        if len(self.chain) > 0:
            block.prev = self.getLastBlock().hash
        else:
            block.prev = "none"
        self.chain.append(block)

    # Monta um arquivo JSON do estado da blockchain
    def chainJSONencode(self):
        blockArrJSON = []
        for block in self.chain:
            blockJSON = {}
            blockJSON["hash"] = block.hash
            blockJSON["index"] = block.index
            blockJSON["prev"] = block.prev
            blockJSON["time"] = block.time
            # blockJSON['nonse'] = block.nonse;

            transactionsJSON = []
            tJSON = {}
            for transaction in block.transactions:
                tJSON["time"] = transaction.time
                tJSON["sender"] = transaction.sender
                tJSON["reciever"] = transaction.reciever
                tJSON["amt"] = transaction.amt
                tJSON["hash"] = transaction.hash
                transactionsJSON.append(tJSON)

            blockJSON["transactions"] = transactionsJSON

            blockArrJSON.append(blockJSON)

        return blockArrJSON


class Block(object):
    def __init__(self, transactions, time, index):
        self.index = index  # Número do Bloco
        self.transactions = transactions  # Lista de transações
        self.time = time  # Tempo da criação do bloco
        self.prev = ""  # Hash do bloco anterior
        self.hash = self.calculateHash()  # Hash do bloco atual
        self.nonce = 0  # Nonce do bloco. Nonce é o número/hash que é utilizado na prova de trabalho do bloco

    def calculateHash(self):
        hashTransactions = ""
        for transaction in self.transactions:
            hashTransactions += transaction.hash
        # VVVV Cria uma String contentdo o tempo na qual o hash será criado, o hash da transação que criou esse bloco, o núnumero do hash do bloco anterior e o index desse bloco
        hashString = (
            str(self.time)
            + hashTransactions
            + self.prev
            + str(self.index)
            + str(self.nonce)
        )
        # VVVV formata a String anterior como JSON
        hashEncoded = json.dumps(hashString, sort_keys=True).encode()
        # VVVV Retorna o JSON anterior criptografado em SHA256 -> mesma criptografia do Bitcoin
        return hashlib.sha256(hashEncoded).hexdigest()

    def mineBlock(self, difficulty):
        arr = []
        for i in range(0, difficulty):
            arr.append(i)

        # compute until the beginning of the hash = 0123..difficulty
        arrStr = map(str, arr)
        hashPuzzle = "".join(arrStr)
        # print(len(hashPuzzle));
        while self.hash[0:difficulty] != hashPuzzle:
            self.nonse += 1
            self.hash = self.calculateHash()
            # print(len(hashPuzzle));
            # print(self.hash[0:difficulty]);
        print("Block Mined!")
        return True


class Transaction(object):
    # Inicialização da classe de Transaction
    def __init__(self, sender, reciever, amt):
        # Define o remetente da transação
        self.sender = sender
        # Define o destinatário da transação
        self.reciever = reciever
        # Define a quantidade de tokens a ser transferida
        self.amt = amt
        # Define a data da transação
        self.time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        # Define o Hash de identificação da transação
        self.hash = self.calculateHash()

    def calculateHash(self):
        hashString = self.sender + self.reciever + str(self.amt) + str(self.time)
        hashEncoded = json.dumps(hashString, sort_keys=True).encode()
        return hashlib.sha256(hashEncoded).hexdigest()

    def isValidTransaction(self):
        if self.hash != self.calculateHash():
            return False
        if self.sender == self.reciever:
            return False
        if self.sender == "Miner Rewards":
            # security : unfinished
            return True
        if not self.signature or len(self.signature) == 0:
            print("No Signature!")
            return False
        return True
        # needs work!

    def signTransaction(self, key, senderKey):
        if self.hash != self.calculateHash():
            print("transaction tampered error")
            return False
        # print(str(key.publickey().export_key()));
        # print(self.sender);
        if str(key.publickey().export_key()) != str(senderKey.publickey().export_key()):
            print("Transaction attempt to be signed from another wallet")
            return False

        # h = MD5.new(self.hash).digest();

        pkcs1_15.new(key)

        self.signature = "made"
        # print(key.sign(self.hash, ""));
        print("made signature!")
        return True

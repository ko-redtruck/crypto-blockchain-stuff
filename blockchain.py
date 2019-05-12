import hashlib, json
import random
import pprint
import time

pp = pprint.PrettyPrinter(indent=4)

def sha256(block):
    return hashlib.sha256(json.dumps(block, sort_keys=True).encode("utf-8")).hexdigest()

def createblock(prev_block,nonce):
    return {
        "prev_block": prev_block,
        "transactions": [1],
        "nonce": nonce
    }

def findblock(prev_block):
    #fest
    prev_block = sha256(prev_block)
    counter = 0

    while counter<difficulty:
        block = createblock(prev_block,random.randint(0,10000000))
        block_hash = sha256(block)
        counter = 0
        for i in range(difficulty):
            if block_hash[i] == "0":
                counter += 1
    return block

block_genesis = {
    "prev_block": None,
    "transactions": [2,1]
}
blockchain = []
difficulty = 4
blockchain.append(block_genesis)

for i in range(0,5):
    #blockchain[i]--> previous block
    blockchain.append(findblock(blockchain[i]))
    pp.pprint(blockchain[i+1])

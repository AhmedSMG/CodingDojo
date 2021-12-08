from block import Block
from transaction import Transaction

from typing import List, Set, Dict, Tuple, Optional

import time
import json
import hashlib

class BlockChain:
    
    def __init__(self) -> None:
        self.transactions: List[Transaction] = []
        self.chain: List[Block] = []
        self.difficulty = 2
        # Append Gensis Block
        self.chain.append(Block.create_gensis_block())
        
    def proof_of_work(self, block:Block) -> Block:
        t1 = time.time()
        while True:
            if block.compute_hash()[:self.difficulty] == "0" * self.difficulty:
                t2 = time.time()
                print(f"Proof of Work: {t2 - t1:.2f}s")
                return block
            block.nonce += 1
        
    def validate_block(self, block:Block) -> bool:
        last_block = self.chain[-1]
        
        if block.previous_hash != last_block.compute_hash():
            print("Hash conflict!")
            return False
        
        if block.compute_hash()[:self.difficulty] == "0" * self.difficulty:
            print("Hash Incorrect!")
            return False
        
        self.chain.append(block)
        print("Block added successfully to chain")
        return True
    
    def add_transaction(self, transactions) -> None:
        self.transactions.append(transactions)
    
    def mine(self) -> bool:
        if len(self.transactions) < 1:
            print("No transaction/s found")
            return False
        
        last_block = self.chain[-1]
        new_block = Block(transactions=self.transactions,
                          pervious_hash=last_block.compute_hash())
        
        self.proof_of_work(new_block)
        
        if not self.validate_block(new_block):
            print("Error Block NOT Valid")
            return False
        
        self.transactions = []
        return True
    
    def to_json(self) -> str:
        out = []
        for index, block in enumerate(self.chain):
            print(block)
            temp = {"hash": block.compute_hash(),
                    "height": index}
            temp.update(block.__dict__)
        return json.dumps(out)

def main():
    bitcoins = BlockChain()
    
    t1 = Transaction(from_address="1234", 
                     to_address="9876",
                     amount=0.123)
    
    t2 = Transaction(from_address="5456", 
                     to_address="85643",
                     amount=34562.21)
    
    t3 = Transaction(from_address="1234", 
                     to_address="9393",
                     amount=10.3)
    
    print(bitcoins.to_json())
    
    bitcoins.add_transaction([t1, t2, t3])
    bitcoins.mine()
    
    print(bitcoins.to_json())

if __name__ == "__main__":
    main()
    
        
        
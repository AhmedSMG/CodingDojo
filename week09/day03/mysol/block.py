from transaction import Transaction

from typing import List, Set, Dict, Tuple, Optional
import time
import json
import hashlib

class Block:
    """
    
    Version: A version number to track software/protocol upgrades
    Previous Block Hash: A reference to the hash of the previous (parent) block in the chain
    Timestamp: The approximate creation time of this block (seconds from Unix Epoch)
    Difficulty Target: The proof-of-work algorithm difficulty target for this block
    Nonce: A counter used for the proof-of-work algorithm
    Transactions: Lisst of transaction
    
    """
    
    def __init__(self,
                 previous_hash: str,
                 difficulty: int=2,
                 nonce: int=0,
                 transactions: List[Transaction]=[],
                 version: str="1",) -> None:
        
        # Block Header
        self.version = version
        self.previous_hash = previous_hash
        self.timestamp = int(time.time())
        self.difficulty = difficulty
        self.nonce = nonce
        # Block Body
        self.transactions = transactions
        
    def compute_hash(self) -> str:
        header_keys = ["version", "previous_hash", "timestamp", "difficulty", "nonce"]
        block_header = str({k: self.__dict__[k] for k in header_keys})
        
        # Hash Twice the header
        temp_hash = hashlib.sha256(block_header.encode()).hexdigest()
        return hashlib.sha256(temp_hash.encode()).hexdigest()
    
    def to_json(self) -> str:
        return json.dumps(self.__dict__)
    
    
    def __repr__(self) -> str:
        return "Block(" +\
            f"version={self.version}, " +\
            f"timestamp={self.timestamp}, " +\
            f"difficulty={self.difficulty}, " +\
            f"nonce={self.nonce}, " +\
            f"transactions={self.transactions}" +\
            ")" 
            
    @staticmethod
    def create_gensis_block():
        return Block(previous_hash="0")
    
def main():
    gen = Block.create_gensis_block()
    print(gen)
    print(gen.to_json())
    x = gen.compute_hash()
    print(x)

if __name__ == "__main__":
    main()
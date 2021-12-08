from transaction import Transaction


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
        
    def compute_hash(self):
        block_header = " ".join([self.previous_hash,
                                 self.difficulty,
                                 self.nonce,
                                 self.version])
        # Hash Twice the header
        return hashlib.sha256(hashlib.sha256(block_header.encode).hexdigest()).hexdigest()
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def create_gensis_block():
        return Block(previous_hash="0")
    
def main():
    pass
if __name__ == "__main__":
    main()
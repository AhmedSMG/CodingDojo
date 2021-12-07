import json
import datetime as dt
import hashlib


class Block:

    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):

        # Advanced or adventurous students: feel free to change the
        # above parameters and default arguments.
        # Todo for students, implement the initialization of the properties for this class.

        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = nonce
        self.previous_hash = previous_hash,
        self.current_hash = compute_hash()

    def compute_hash(self, x=7) -> str:
        while True:
            _hash = hashlib.sha256(str(self.nonce).encode()).hexdigest()
        if _hash[:x] == "0" * x:
            return _hash
        else:
            self.nonce += 1

    def to_json(self):
        return json.dumps(self.__dict__, sort_keys=True)
        # todo for students: Use what you learned from your last assignment implement
        # a sha256 solution to return the hex digest of the block_string, and return it.

    def mining(self):
        while True:
            _hash = hashlib.sha256(str(nonce).encode()).hexdigest()
        if _hash[:x] == "0" * x:
            t2 = dt.datetime.now()
            break
        else:
            nonce += 1

class Blockchain:

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

   # todo define get_last_block(self) -> Block, hint: consider an index to the last element in your chain property.
   #
   # todo define proof_of_work(self, block:Block) -> str, 
      # hint consider something similar to:
      # computed_hash = how do we get the hash from a Block object?
      # while not computed_hash.startswith('0' * Blockchain.difficulty):
      #         block.nonce += 1
      #         computed_hash = block.compute_hash()
      # Don't forget to return the hash. 
   #
   # todo define is_valid_proof(self, block:Block, block_hash:str) -> bool
      # hint, we want to return true if block_hash.startswith('0' * Blockchain.difficulty)
      # AND if block_hash is in fact the hash of our block (maybe use block.compute_hash())
   #
   # todo define add_block(self, block:Block, proof:str) -> bool
      # hints, we probably want to get the previous hash from get_last_block()
      # Check if the previous hash matches the previous hash in the block argument. 
      # Make use of is_valid_proof for block and proof to check if someone is trying to do something sneaky. 
      # for both of the above, let's return False early and return control the calling function if the block is not valid.
      # If we make it this far, we're in the clear. So let's add the hash to our block, append it to the chain, 
      # and return True. 
   #
   #
   # todo, define add_new_transaction(self, transaction:dict) -> None
      # Hint how do we append to a list? How do we do this for a property of our object (self). Ease one line function.    
   #
   # todo, define mine(self) -> int:
      # Hints: do we need to continue if our mempool is empty? Maybe return -1 if so. 
      # consider retrieving the last block to a local variable make life easy. 
      # Let's make sure we use our Block constructor to create a new block with all the transactions we want to mine 
      # (all of them are fine)
      # hint: Block(index=last_block.index + 1,
      #                    transactions=self.unconfirmed_transactions,
      #                    timestamp=time.time(),
      #                    previous_hash=last_block.hash)
      #
      # Finally, let's be sure to use our handy proof_of_work function, add_block function, and to remember to reset our
      # unconfirmed_transactions (our mem-pool), before returning our new block index;
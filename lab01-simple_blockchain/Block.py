from hashlib import sha256


class Block:
    def __init__(self, transactions, previous_hash, difficulty = 4):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.generate_hash()
        self.mine_block()
        
    def generate_hash(self):
        block_contents = str([transaction.string for transaction in self.transactions]) + str(self.previous_hash) + str(self.nonce)
        return sha256(block_contents.encode()).hexdigest()
    
    def mine_block(self):
        self.nonce = 0
        while self.hash[:self.difficulty] != "0" * self.difficulty:
            self.nonce += 1
            self.hash = self.generate_hash()
        print("Block mined:", self.hash, "Nonce:", self.nonce)

    def __str__(self):
        return f"Block(transactions={self.transactions}, previous_hash={self.previous_hash}, nonce={self.nonce}, hash={self.hash})"

    def __repr__(self):
        return str(self)
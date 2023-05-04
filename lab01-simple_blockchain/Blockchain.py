from Block import Block


class Blockchain:
    def __init__(self, difficulty):
        self.chain = [Block([], "oooo", difficulty)]
        self.difficulty = difficulty
        
    def add_transaction(self, transaction):
        current_block = self.chain[-1]
        if len(current_block.transactions) < 3:
            current_block.transactions.append(transaction)
            current_block.mine_block()
        else:
            new_block = Block([transaction], current_block.hash, self.difficulty)
            self.chain.append(new_block)
 
    def print_blockchain(self):
        for block in self.chain:
            print("Block hash:", block.hash)
            for transaction in block.transactions:
                print(transaction)
            print("---------------")

    def print_blockchain_detailed(self):
        for i, block in enumerate(self.chain):
            print(f"Block {i}:".center(80, "-"))
            print(f"Block hash: {block.hash}")
            print(f"Previous hash: {block.previous_hash}")
            print(f"Number of transactions: {len(block.transactions)}")
            print(f"Transactions:")
            for j, transaction in enumerate(block.transactions):
                print(f"  Transaction {j}:")
                print(f"    Transaction ID: {transaction.transaction_id}")
                print(f"    Sender: {transaction.sender}")
                print(f"    Recipient: {transaction.recipient}")
                print(f"    Amount: {transaction.amount}")
                print(f"    String: {transaction.string}")
                print(f"    Hash: {transaction.hash}")
        print("-" * 80)

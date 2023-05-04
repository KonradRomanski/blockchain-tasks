from lab01 import Lab01
from Transaction import Transaction
from Blockchain import Blockchain


def main():
    table = [
        [1, 'A', 'N', 3],
        [2, 'M', 'O', 5],
        [3, 'O', 'K', 4],
        [4, 'R', 'J', 1],
        [5, 'Y', 'A', 0],
        [6, 'Z', 'L', 0],
        [7, 'I', 'O', 1],
        [8, 'N', 'K', 4],
        [9, 'O', 'I', 4],
        [10, 'P', 'M', 1]
    ]
    transactions = [Transaction(*row) for row in table]

    lab01 = Lab01()
    string = "4RJ1"
    print("String:", string)

    print("Task2 - Caesar Cipher")
    print(lab01.caesar_encrypt(string, 5))

    print("Task3 - SHA256 Hash")
    print(lab01.sha256_hash(string))
    print()
    
    print("Adding transactions to blockchain...")
    difficulty = 4
    blockchain = Blockchain(difficulty)
    for transaction in transactions:
        print(" Adding transaction:", transaction)
        blockchain.add_transaction(transaction)
    blockchain.print_blockchain_detailed()


if __name__ == "__main__":
    main()

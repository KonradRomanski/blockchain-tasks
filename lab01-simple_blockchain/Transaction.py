from hashlib import sha256


class Transaction:
    def __init__(self, transaction_id, sender, recipient, amount):
        self.transaction_id = transaction_id
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.string = f"{self.transaction_id}{self.sender}{self.recipient}{self.amount}"
        self.hash = sha256(self.string.encode()).hexdigest()
        
    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Sender: {self.sender}, Recipient: {self.recipient}, Amount: {self.amount}, String: {self.string}, Hash: {self.hash}"

    def __repr__(self):
        return f"Transaction({self.transaction_id!r}, {self.sender!r}, {self.recipient!r}, {self.amount!r}, {self.string!r}, {self.hash!r})"


from flask import Flask, jsonify, request
import time
import hashlib

app = Flask(__name__)


class Block:
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def to_dict(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
            'hash': self.hash
        }


class Blockchain:
    def __init__(self, difficulty=3):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(0, ["Genesis Block"], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self):
        if not self.pending_transactions:
            return None

        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=self.get_latest_block().hash
        )

        self.proof_of_work(new_block)
        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block

    def proof_of_work(self, block):
        while not block.hash.startswith('0' * self.difficulty):
            block.nonce += 1
            block.hash = block.calculate_hash()

    def to_dict(self):
        return [block.to_dict() for block in self.chain]


# Flask API


blockchain = Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify(blockchain.to_dict()), 200

@app.route('/transaction', methods=['POST'])
def add_transaction():
    data = request.get_json()
    if not data or 'transaction' not in data:
        return jsonify({'error': 'Transaction data required'}), 400
    blockchain.add_transaction(data['transaction'])
    return jsonify({'message': 'Transaction added'}), 201

@app.route('/mine', methods=['POST'])
def mine_block():
    new_block = blockchain.mine_pending_transactions()
    if new_block:
        return jsonify(new_block.to_dict()), 201
    else:
        return jsonify({'message': 'No transactions to mine'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
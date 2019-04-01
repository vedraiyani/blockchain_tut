from client import Client
from transaction import Transaction
from block import Block

if __name__ == "__main__":
    
    Dinesh = Client()

    t0 = Transaction (
    "Genesis",
    Dinesh.identity,
    500.0
    )

    block0 = Block()
    
    block0.previous_block_hash = None
    Nonce = None

    block0.verified_transactions.append (t0)

    digest = hash (block0)
    last_block_hash = digest
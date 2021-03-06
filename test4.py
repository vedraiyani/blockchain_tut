from client import Client
from transaction import Transaction
from block import Block

def display_transaction(transaction):
    #for transaction in transactions:
    dict = transaction.to_dict()
    print ("sender: " + dict['sender'])
    print ('-----')
    print ("recipient: " + dict['recipient'])
    print ('-----')
    print ("value: " + str(dict['value']))
    print ('-----')
    print ("time: " + str(dict['time']))
    print ('-----')
    
def dump_blockchain (self):
    print ("Number of blocks in the chain: " + str(len (self)))
    for x in range (len(TPCoins)):
        block_temp = TPCoins[x]
        print ("block # " + str(x))
        for transaction in block_temp.verified_transactions:
            display_transaction (transaction)
            print ('--------------')
        print ('=====================================')

if __name__ == "__main__":
    
    TPCoins = []

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

    TPCoins.append (block0)

    dump_blockchain(TPCoins)
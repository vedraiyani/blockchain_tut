from client import Client
from transaction import Transaction

if __name__ == "__main__":
    Dinesh = Client()
    Ramesh = Client()
    t = Transaction(
    Dinesh,
    Ramesh.identity,
    5.0
    )
    signature = t.sign_transaction()
    print (signature) 
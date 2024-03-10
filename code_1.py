from web3 import Account, Web3

# Create a new private key and address
private_key = Account.create().privateKey.hex()
address = Web3.toChecksumAddress(Account.privateKeyToAccount(private_key).address)

print("Private Key:", private_key)
print("Address:", address)


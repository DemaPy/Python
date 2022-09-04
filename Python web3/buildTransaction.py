from web3 import Web3

def buy(web3, amount, yourWallet, secret_key):
    abi = '[{"inputs": [{"internalType": "uint256","name": "tablePrice","type": "uint256"},{"internalType": "address","name": "referrer","type": "address"}],"name": "buy","outputs": [],"stateMutability": "payable","type": "function"}]'
    contract_instance = web3.eth.contract(address=Web3.toChecksumAddress('0xa1B941c10c24338B5cAAFd90D083bF679c453218'),abi=abi)
    transaction = {
        'gas': 200000,
        'gasPrice': web3.toWei(50,'gwei'),
        'nonce': web3.eth.get_transaction_count(yourWallet),
    }
    tx = contract_instance.functions.buy(amount, '0x127484eCCBD20DdAe54DeA69985a4D252228D006').buildTransaction(transaction)
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=secret_key)
    tx_token = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("https://bscscan.com/tx/" + (web3.toHex(tx_token)))


if __name__== '__main__':
    provider="https://bsc-dataseed.binance.org/"
    web3 = Web3(Web3.HTTPProvider(provider)) #Нода bsc (сеть)
    amount = int(input('Price: ').strip())
    yourWallet = Web3.toChecksumAddress(input('Your wallet: ')).strip()
    secret_key = input('Key: ').strip()
    buy(web3, amount, yourWallet, secret_key)

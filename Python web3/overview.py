from eth_utils import to_wei
from web3 import Web3
from words import slovar
import json
import re

def connectTo(provider="https://bsc-dataseed.binance.org/"):
    connect = Web3(Web3.HTTPProvider(provider))
    where = re.search('binance', provider).group()
    if connect.isConnected():
        print(f'{slovar[1]}{where}!')
        whatNext(connect)
    else:
        print(slovar[0])

def checkLenInput(content):
    while True:
        content
        if len(content) == 0:
            print('Write correct address!')
            continue
        else:
            break

def whatNext(c):
    print(slovar[2])
    choose = input(slovar[6]).strip()
    if choose == '1':
        getBlock(c)
    elif choose == '2':
        a = input(slovar[3]).strip()
        getBalance(c,a)
    elif choose == '3':
        a = input(slovar[8]).strip()
        getTransaction(c,a)
    elif choose == '4':
        key = input(slovar[9]).strip()
        sendTransaction(c,key)
    elif choose == '5':
        while True:
            first = input('Первый токен: ').strip()
            if len(first) == 0:
                print('Write correct address!')
                continue
            else:
                break
        # checkLenInput(first)
        while True:
            second = input('Второй токен: ').strip()
            if len(second) == 0:
                print('Write correct address!')
                continue
            else:
                break
        getPair(c,first,second)
    else:
        print(slovar[4])
        
def getBlock(c):
    print(c.eth.block_number)

def getBalance(c, acc):
    to_eth = c.eth.get_balance(acc)
    res = c.fromWei(to_eth, 'ether')
    print(res)

def getTransaction(c,hash):
    t = c.eth.get_transaction(hash)
    print(t)

def sendTransaction(c,key):
    nonce = input('Your address: ').strip()
    to_add = input('To address: ').strip()
    amount = float(input('Amount: ').strip())
    
    tx = {
        'nonce': c.eth.getTransactionCount(nonce),
        'to': to_add,
        'value': c.toWei(amount, 'ether'),
        'gas': 30000,
        'gasPrice': c.toWei(50,'gwei'),
    }
    signed_txn = c.eth.account.signTransaction(tx, key)
    txn_hash = c.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(txn_hash)

def getPair(c, first, second):
    factory = '0xca143ce32fe78f1f7019d7d551a6402fc5350c73'
    contract = c.eth.contract(address=Web3.toChecksumAddress(factory), abi=json.loads('[{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]'))
    print(f'Contract liqudity is: {contract.functions.getPair(first, second).call()}')

if __name__ == '__main__':
    q = input(slovar[7])
    if q == 'Y':
        p = input(slovar[5]).strip()
        connectTo(p)
    else:
        connectTo()

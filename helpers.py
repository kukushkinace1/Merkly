from const import DATA, ERC20_ABI
from config import MAX_GWEI

import time
from loguru import logger
from web3 import Web3
import random
from tqdm import tqdm

max_time_check_tx_status = 360
w3_eth = Web3(Web3.HTTPProvider(random.choice(DATA['ethereum']['rpc'])))


def sign_tx(web3, contract_txn, privatkey):
    signed_tx = web3.eth.account.sign_transaction(contract_txn, privatkey)
    raw_tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = web3.to_hex(raw_tx_hash)

    return tx_hash


def cheker_gwei():
    try:
        max_gwei = MAX_GWEI * 10 ** 9
        if w3_eth.eth.gas_price > max_gwei:
            logger.info('Газ большой, пойду спать')
            while w3_eth.eth.gas_price > max_gwei:
                time.sleep(60)
            logger.info('Газ в норме. Продолжаю работу')
    except:
        w3_eth = random.choice(DATA['ethereum']['rpc'])
        cheker_gwei()


def check_data_token(chain, token_address):
    try:

        web3 = Web3(Web3.HTTPProvider(DATA[chain]['rpc']))
        token_contract = web3.eth.contract(address=Web3.to_checksum_address(token_address), abi=ERC20_ABI)
        decimals = token_contract.functions.decimals().call()
        symbol = token_contract.functions.symbol().call()

        return token_contract, decimals, symbol

    except Exception as error:
        logger.error(error)


def check_status_tx(chain, tx_hash):
    start_time_stamp = int(time.time())

    while True:
        try:
            rpc_chain = random.choice(DATA[chain]['rpc'])
            web3 = Web3(Web3.HTTPProvider(rpc_chain))
            status_ = web3.eth.get_transaction_receipt(tx_hash)
            status = status_["status"]

            if status in [0, 1]:
                return status

        except:
            time_stamp = int(time.time())
            if time_stamp - start_time_stamp > max_time_check_tx_status:
                logger.info(f'не получили tx_status за {max_time_check_tx_status} sec, думаем что tx is success')
                return 1
            time.sleep(1)


def add_gas_limit(web3, contract_txn):
    value = contract_txn['value']
    contract_txn['value'] = 0
    pluser = [1.02, 1.05]
    gasLimit = web3.eth.estimate_gas(contract_txn)
    contract_txn['gas'] = int(gasLimit * random.uniform(pluser[0], pluser[1]))

    contract_txn['value'] = value
    return contract_txn


def add_gas_limit_layerzero(web3, contract_txn):
    pluser = [1.05, 1.07]
    gasLimit = web3.eth.estimate_gas(contract_txn)
    contract_txn['gas'] = int(gasLimit * random.uniform(pluser[0], pluser[1]))
    return contract_txn


def add_gas_price(web3, contract_txn):
    gas_price = web3.eth.gas_price
    contract_txn['gasPrice'] = int(gas_price * random.uniform(1.01, 1.02))
    return contract_txn


def check_allowance(chain, token_address, wallet, spender):
    try:
        web3 = Web3(Web3.HTTPProvider(random.choice(DATA[chain]['rpc'])))
        contract = web3.eth.contract(address=Web3.to_checksum_address(token_address), abi=ERC20_ABI)
        amount_approved = contract.functions.allowance(wallet, spender).call()
        return amount_approved
    except Exception as error:
        logger.error(error)


def get_web3(chain):
    rpc = random.choice(DATA[chain]['rpc'])
    web3 = Web3(Web3.HTTPProvider(rpc))
    return web3


def intToDecimal(qty, decimal):
    return int(qty * int("".join(["1"] + ["0"] * decimal)))


def sleeping(from_sleep, to_sleep):
    x = random.randint(from_sleep, to_sleep)
    for i in tqdm(range(x), desc='sleep ', bar_format='{desc}: {n_fmt}/{total_fmt}'):
        time.sleep(1)

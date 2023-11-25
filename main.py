from const import DATA
from const import MERKLY_CONTRACTS, LAYERZERO_CHAINS_ID
from config import SLEEP_FROM, SLEEP_TO, RANDOM_WALLETS, COUNT_TX, FROM_CHAINS, TO_CHAINS, COUNT_NATIV, MIN_NATIV
from helpers import get_web3, add_gas_price, sign_tx, add_gas_limit_layerzero, check_status_tx, intToDecimal, sleeping, cheker_gwei

from loguru import logger
from web3 import Web3
from sys import stderr
import random
from eth_abi import encode

logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <3}</level> | <level>{message}</level>")

ABI_MERKLY_REFUEL = '[{"inputs":[{"internalType":"uint256","name":"_minGasToTransfer","type":"uint256"},{"internalType":"address","name":"_layerZeroEndpoint","type":"address"},{"internalType":"uint256","name":"_startMintId","type":"uint256"},{"internalType":"uint256","name":"_endMintId","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes32","name":"_hashedPayload","type":"bytes32"}],"name":"CreditCleared","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes32","name":"_hashedPayload","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"CreditStored","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"indexed":false,"internalType":"uint64","name":"_nonce","type":"uint64"},{"indexed":false,"internalType":"bytes","name":"_payload","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"_reason","type":"bytes"}],"name":"MessageFailed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"indexed":true,"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"indexed":true,"internalType":"address","name":"_toAddress","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"}],"name":"ReceiveFromChain","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"indexed":false,"internalType":"uint64","name":"_nonce","type":"uint64"},{"indexed":false,"internalType":"bytes32","name":"_payloadHash","type":"bytes32"}],"name":"RetryMessageSuccess","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":true,"internalType":"bytes","name":"_toAddress","type":"bytes"},{"indexed":false,"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"}],"name":"SendToChain","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"indexed":false,"internalType":"uint256","name":"_dstChainIdToBatchLimit","type":"uint256"}],"name":"SetDstChainIdToBatchLimit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"indexed":false,"internalType":"uint256","name":"_dstChainIdToTransferGas","type":"uint256"}],"name":"SetDstChainIdToTransferGas","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"indexed":false,"internalType":"uint16","name":"_type","type":"uint16"},{"indexed":false,"internalType":"uint256","name":"_minDstGas","type":"uint256"}],"name":"SetMinDstGas","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_minGasToTransferAndStore","type":"uint256"}],"name":"SetMinGasToTransferAndStore","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"precrime","type":"address"}],"name":"SetPrecrime","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_path","type":"bytes"}],"name":"SetTrustedRemote","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"_remoteAddress","type":"bytes"}],"name":"SetTrustedRemoteAddress","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DEFAULT_PAYLOAD_SIZE_LIMIT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"FUNCTION_TYPE_SEND","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"address","name":"_zroPaymentAddress","type":"address"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"bridgeGas","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"clearCredits","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"dstChainIdToBatchLimit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"dstChainIdToTransferGas","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bool","name":"_useZro","type":"bool"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"estimateGasBridgeFee","outputs":[{"internalType":"uint256","name":"nativeFee","type":"uint256"},{"internalType":"uint256","name":"zroFee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bytes","name":"_toAddress","type":"bytes"},{"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"},{"internalType":"bool","name":"_useZro","type":"bool"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"estimateSendBatchFee","outputs":[{"internalType":"uint256","name":"nativeFee","type":"uint256"},{"internalType":"uint256","name":"zroFee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bytes","name":"_toAddress","type":"bytes"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"bool","name":"_useZro","type":"bool"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"estimateSendFee","outputs":[{"internalType":"uint256","name":"nativeFee","type":"uint256"},{"internalType":"uint256","name":"zroFee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"bytes","name":"","type":"bytes"},{"internalType":"uint64","name":"","type":"uint64"}],"name":"failedMessages","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"}],"name":"forceResumeReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"_configType","type":"uint256"}],"name":"getConfig","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_remoteChainId","type":"uint16"}],"name":"getTrustedRemoteAddress","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"}],"name":"isTrustedRemote","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lzEndpoint","outputs":[{"internalType":"contract ILayerZeroEndpoint","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"lzReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"maxMintId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"uint16","name":"","type":"uint16"}],"name":"minDstGasLookup","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minGasToTransferAndStore","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mint","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nextMintId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"nonblockingLzReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"payloadSizeLimitLookup","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"precrime","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"_nonce","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"retryMessage","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bytes","name":"_toAddress","type":"bytes"},{"internalType":"uint256[]","name":"_tokenIds","type":"uint256[]"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"internalType":"address","name":"_zroPaymentAddress","type":"address"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"sendBatchFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bytes","name":"_toAddress","type":"bytes"},{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"internalType":"address","name":"_zroPaymentAddress","type":"address"},{"internalType":"bytes","name":"_adapterParams","type":"bytes"}],"name":"sendFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"uint256","name":"_configType","type":"uint256"},{"internalType":"bytes","name":"_config","type":"bytes"}],"name":"setConfig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_dstChainIdToBatchLimit","type":"uint256"}],"name":"setDstChainIdToBatchLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_dstChainIdToTransferGas","type":"uint256"}],"name":"setDstChainIdToTransferGas","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_fee","type":"uint256"}],"name":"setFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint16","name":"_packetType","type":"uint16"},{"internalType":"uint256","name":"_minGas","type":"uint256"}],"name":"setMinDstGas","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_minGasToTransferAndStore","type":"uint256"}],"name":"setMinGasToTransferAndStore","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_size","type":"uint256"}],"name":"setPayloadSizeLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_precrime","type":"address"}],"name":"setPrecrime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"}],"name":"setReceiveVersion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"}],"name":"setSendVersion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"internalType":"bytes","name":"_path","type":"bytes"}],"name":"setTrustedRemote","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_remoteChainId","type":"uint16"},{"internalType":"bytes","name":"_remoteAddress","type":"bytes"}],"name":"setTrustedRemoteAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"storedCredits","outputs":[{"internalType":"uint16","name":"srcChainId","type":"uint16"},{"internalType":"address","name":"toAddress","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"},{"internalType":"bool","name":"creditsRemain","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"trustedRemoteLookup","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"payable","type":"function"}]'


def get_adapterParams(gaslimit: int, amount: int):
    return Web3.to_hex(encode(["uint16", "uint64", "uint256"], [2, gaslimit, amount])[30:])


def merkly_refuel(from_chain, to_chain, amount_from, amount_to, private_key, current_account, accounts, number=0):
    global module_str

    try:
        amount = round(random.uniform(amount_from, amount_to), 8)

        web3 = get_web3(from_chain)
        account = web3.eth.account.from_key(private_key)
        wallet = account.address

        module_str = f'{from_chain} => {to_chain}'
        logger.info(f'[{current_account}/{accounts}][{wallet}] {module_str}')

        contract = web3.eth.contract(address=Web3.to_checksum_address(
            MERKLY_CONTRACTS[from_chain]), abi=ABI_MERKLY_REFUEL)

        value = intToDecimal(amount, 18)
        adapterParams = get_adapterParams(250000, value) + wallet[2:].lower()
        send_value = contract.functions.estimateGasBridgeFee(LAYERZERO_CHAINS_ID[to_chain], False, adapterParams).call()

        contract_txn = contract.functions.bridgeGas(
            LAYERZERO_CHAINS_ID[to_chain],
            '0x0000000000000000000000000000000000000000',  # _zroPaymentAddress
            adapterParams
        ).build_transaction(
            {
                "from": wallet,
                "value": send_value[0],
                "nonce": web3.eth.get_transaction_count(wallet),
                'gasPrice': 0,
                'gas': 0,
            }
        )

        if amount > 0:
            if from_chain == 'bsc':
                # специально ставим 1.2 гвей, так транза будет дешевле
                contract_txn['gasPrice'] = 1200000000
            else:
                contract_txn = add_gas_price(web3, contract_txn)

            contract_txn = add_gas_limit_layerzero(web3, contract_txn)

            tx_hash = sign_tx(web3, contract_txn, private_key)
            tx_link = f'{DATA[from_chain]["scan"]}/{tx_hash}'

            status = check_status_tx(from_chain, tx_hash)
            if status == 1:
                logger.success(f'tx: {tx_link}')
                return "success"

        else:
            logger.error(f"{module_str} : баланс равен 0")

    except Exception as error:
        if 'execution reverted' in str(error) and not 'gas' in str(error):#скорее неверный контракт попробуем другой приемник
            number += 1
            if number < len(TO_CHAINS) and from_chain == TO_CHAINS[number]:
                number += 1
            if number < len(TO_CHAINS):
                logger.info('Выпала неподходящая сеть приемника, пробую другую....')
                merkly_refuel(from_chain, TO_CHAINS[number], amount_from, amount_to, private_key, current_account, accounts, number)
            else:
                logger.info('Выпала неподходящая сеть приемника, а других нет. Пропускаем кошелек')
        else:
            logger.error(f'{module_str} | {error}')


def from_chain_balance(account):

    FROM_CHAINS_RETURN = []
    for chain in FROM_CHAINS:
        min_nativ = MIN_NATIV[chain] * 10 ** 18
        w3 = Web3(Web3.HTTPProvider(DATA[chain]['rpc']))
        balance = w3.eth.get_balance(account.address)
        if balance > min_nativ:
            FROM_CHAINS_RETURN.append(chain)

    return FROM_CHAINS_RETURN


if __name__ == '__main__':
    with open("keys.txt", "r") as file:
        keys = [line.strip() for line in file.readlines()]

    if RANDOM_WALLETS:
        random.shuffle(keys)

    for current_tranz in range(0, COUNT_TX[1]):
        logger.info(f'Транзакция: {current_tranz + 1}/{COUNT_TX[1]}')
        for current_account, key in enumerate(keys):
            min_count = COUNT_NATIV[0]
            max_count = COUNT_NATIV[1]

            web3 = get_web3('ethereum')
            account = web3.eth.account.from_key(key)
            FROM_CHAINS_S_BALANCE = from_chain_balance(account)
            if len(FROM_CHAINS_S_BALANCE) > 0:
                from_chain = random.choice(FROM_CHAINS_S_BALANCE)
            else:
                logger.warning(f'[{account.address}] Нет сетей с минимальным балансом, пропускаю кошелек....')
                continue
            random.shuffle(TO_CHAINS)
            to_chain = TO_CHAINS[0]

            if (current_tranz+1) > random.randint(COUNT_TX[0], COUNT_TX[1]):#проверка на кол-во
                continue
            cheker_gwei()
            merkly_refuel(from_chain, to_chain, min_count, max_count, key, current_account+1, len(keys))
            sleeping(SLEEP_FROM, SLEEP_TO)

    print("Скрипт закончил работу.")


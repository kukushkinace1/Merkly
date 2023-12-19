# от скольки до скольки спим между кошельками (секунды) :
SLEEP_FROM = 10
SLEEP_TO   = 30

# нужно ли перемешивать кошельки. True = да. False = нет
RANDOM_WALLETS = True # True / False

MAX_GWEI = 35 # gas в gwei

COUNT_TX = [0, 1] #от 1 до 2 транзакций

FROM_CHAINS = ['arbitrum', 'optimism', 'bsc', 'polygon', 'celo', 'nova', 'zksync', 'fantom', 'gnosis'] #['arbitrum', 'optimism', 'bsc', 'polygon', 'celo', 'nova', 'zksync', 'fantom', 'gnosis']
TO_CHAINS = ['kava', 'nova', 'opbnb', 'klaytn', 'moonbeam'] #['base', 'kava', 'klaytn', 'opbnb', 'nova', 'linea', 'zora', 'scroll', 'conflux', 'gnosis', 'celo', 'bsc']
COUNT_NATIV = [0.00001, 0.00002] #от 0.0001 до 0.0002 нативного токена приемника


MIN_NATIV = {
    'arbitrum'  : 0.00012, #0.25$
    'bsc'       :  0.0008, #0.2$
    'optimism'  : 0.00008, #0.17$
    'polygon'   :  0.0009, #0.2$
    'celo'      :  0.0008, #0.2$
    'nova'      : 0.0001,
    'zksync'      : 0.0001,
    'fantom'      : 0.2,
    'gnosis'      : 0.07,
}





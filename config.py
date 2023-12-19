# от скольки до скольки спим между кошельками (секунды) :
SLEEP_FROM = 10
SLEEP_TO   = 30

# нужно ли перемешивать кошельки. True = да. False = нет
RANDOM_WALLETS = True # True / False

MAX_GWEI = 150 # gas в gwei

COUNT_TX = [1, 1] #от 1 до 2 транзакций

FROM_CHAINS = ['optimism', 'bsc', 'arbitrum', 'polygon', 'celo', 'gnosis', 'zksync', 'nova', 'moonbeam', 'fantom'] #['optimism','bsc','arbitrum','polygon','celo','gnosis','zksync','nova','moonbeam','fantom']
COUNT_NATIV = [0.0001, 0.0002] #от 0.0001 до 0.0002 нативного токена приемника

MERKLY_REFUEL_LIST = {
    'optimism':     ['core', 'kava', 'conflux', 'astar', 'fuse', 'celo', 'moonbeam', 'gnosis', 'harmony'],
    'bsc':          ['core', 'kava', 'conflux', 'astar', 'fuse', 'celo', 'moonbeam', 'gnosis', 'harmony'],
    'arbitrum':     ['core', 'kava', 'conflux', 'astar', 'fuse', 'celo', 'moonbeam', 'gnosis', 'harmony'],
    'polygon':      ['core', 'kava', 'conflux', 'astar', 'fuse', 'celo', 'moonbeam', 'gnosis', 'harmony'],
    'celo':         ['gnosis', 'conflux', 'fuse'],
    'gnosis':       ['celo', 'moonbeam', 'klaytn'],
    'zksync':       ['klaytn', 'nova', 'kava', 'fantom', 'opbnb'],
    'nova':         ['moonbeam', 'fantom', 'kava'],
    'moonbeam':     ['nova', 'gnosis', 'fantom', 'dfk'],
    'fantom':       ['celo', 'moonbeam', 'kava', 'gnosis', 'dfk']
}

MIN_NATIV = {
    'optimism':     0.00008,
    'bsc':          0.0008,
    'arbitrum':     0.00012,
    'polygon':      0.0009,
    'celo':         0.0008,
    'gnosis':       0.07,
    'zksync':       0.0001,
    'nova':         0.0001,
    'moonbeam':     0.2,
    'fantom':       0.2,
}


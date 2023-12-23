# от скольки до скольки спим между кошельками (секунды) :
SLEEP_FROM = 10
SLEEP_TO   = 30

# нужно ли перемешивать кошельки. True = да. False = нет
RANDOM_WALLETS = True # True / False

MAX_GWEI = 60 # gas в gwei

COUNT_TX = [5, 10] #от 1 до 2 транзакций

FROM_CHAINS = ['optimism', 'bsc', 'moonbeam', 'celo', 'klaytn', 'harmony'] #['optimism','bsc','arbitrum','polygon','fantom','gnosis','zksync','nova','moonbeam','celo','klaytn','harmony']
COUNT_NATIV = [0.001, 0.002] #от 0.0001 до 0.0002 нативного токена приемника

MERKLY_REFUEL_LIST = {
    'optimism':     ['core', 'kava', 'conflux', 'astar', 'fuse', 'celo', 'moonbeam', 'gnosis', 'harmony'],
    'bsc':          ['core', 'kava', 'conflux', 'astar', 'fuse', 'celo', 'moonbeam', 'gnosis', 'harmony'],
    'arbitrum':     ['core', 'kava', 'conflux', 'astar', 'fuse', 'celo', 'moonbeam', 'gnosis', 'harmony'],
    'polygon':      ['core', 'kava', 'conflux', 'astar', 'fuse', 'celo', 'moonbeam', 'gnosis', 'harmony'],
    'gnosis':       ['celo', 'moonbeam', 'klaytn'],
    'zksync':       ['klaytn', 'nova', 'kava', 'opbnb'],
    'nova':         ['moonbeam', 'kava'],
    'fantom':       ['celo', 'moonbeam', 'kava', 'gnosis', 'dfk'],
    'moonbeam':     ['celo', 'dfk', 'harmony'],#10
    'celo':         ['gnosis', 'moonbeam', 'fuse'],#10
    'klaytn':       ['dfk', 'fuse', 'gnosis'],#10
    'harmony':      ['dfk', 'moonbeam'],#10
}

MIN_NATIV = {
    'optimism':     0.00008,
    'bsc':          0.0008,
    'arbitrum':     0.00012,
    'polygon':      0.0009,
    'gnosis':       0.07,
    'zksync':       0.0001,
    'nova':         0.0001,
    'fantom':       0.2,
    'moonbeam':     0.3,
    'celo':         0.1,
    'klaytn':       0.3,
    'harmony':      6,
}


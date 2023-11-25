# от скольки до скольки спим между кошельками (секунды) :
SLEEP_FROM = 10
SLEEP_TO   = 30

# нужно ли перемешивать кошельки. True = да. False = нет
RANDOM_WALLETS = True # True / False

MAX_GWEI = 30 # gas в gwei

COUNT_TX = [1, 1] #от 1 до 2 транзакций

FROM_CHAINS = ['gnosis'] #['arbitrum', 'optimism', 'bsc', 'polygon','celo']
TO_CHAINS = ['celo'] #['base', 'kava', 'linea', 'zora', 'scroll', 'conflux', 'gnosis', 'celo', 'bsc']
COUNT_NATIV = [0.00001, 0.00002] #от 0.0001 до 0.0002 нативного токена приемника

#тестил при газе 20 в сеть СЕLO
MIN_NATIV = {
    'arbitrum'  : 0.00012, #0.25$
    'bsc'       :  0.0008, #0.2$
    'optimism'  : 0.00008, #0.17$
    'polygon'   :  0.0009, #0.2$
    'celo'      :  0.0008, #0.2$
}





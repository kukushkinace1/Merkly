ERC20_ABI = '[{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"}]'

LAYERZERO_CHAINS_ID = {
    'kava'      : 177,
    'linea'     : 183,
    'base'      : 184,
    'zora'      : 195,
    'scroll'    : 214,
    'conflux'   : 212,
    'celo'      : 125,
    'gnosis'    : 145,
    'bsc'       : 102,
}

MERKLY_CONTRACTS = {
    'optimism'      : '0xa2c203d7ef78ed80810da8404090f926d67cd892',
    'bsc'           : '0xfdc9018af0e37abf89233554c937eb5068127080',
    'arbitrum'      : '0xaa58e77238f0e4a565343a89a79b4addd744d649',
    'polygon'       : '0xa184998ec58dc1da77a1f9f1e361541257a50cf4',
    'celo'          : '0xe33519c400b8f040e73aeda2f45dfdd4634a7ca0',
    'gnosis'        : '0x556f119c7433b2232294fb3de267747745a1dab4',
}

# меняем рпс на свои
DATA = {
    'ethereum'      : {'rpc': 'https://rpc.ankr.com/eth',       'scan': 'https://etherscan.io/tx',              'token': 'ETH', 'chain_id': 1},
    'optimism'      : {'rpc': 'https://rpc.ankr.com/optimism',  'scan': 'https://optimistic.etherscan.io/tx',   'token': 'ETH', 'chain_id': 10},
    'bsc'           : {'rpc': 'https://rpc.ankr.com/bsc',       'scan': 'https://bscscan.com/tx',               'token': 'BNB', 'chain_id': 56},
    'polygon'       : {'rpc': 'https://rpc.ankr.com/polygon',   'scan': 'https://polygonscan.com/tx',           'token': 'MATIC','chain_id': 137},
    'polygon_zkevm' : {'rpc': 'https://zkevm-rpc.com',          'scan': 'https://zkevm.polygonscan.com/tx',     'token': 'ETH', 'chain_id': 1101},
    'arbitrum'      : {'rpc': 'https://rpc.ankr.com/arbitrum',  'scan': 'https://arbiscan.io/tx',               'token': 'ETH', 'chain_id': 42161},
    'avalanche'     : {'rpc': 'https://rpc.ankr.com/avalanche', 'scan': 'https://snowtrace.io/tx',              'token': 'AVAX','chain_id': 43114},
    'fantom'        : {'rpc': 'https://rpc.ankr.com/fantom',    'scan': 'https://ftmscan.com/tx',               'token': 'FTM', 'chain_id': 250},
    'nova'          : {'rpc': 'https://nova.arbitrum.io/rpc',   'scan': 'https://nova.arbiscan.io/tx',          'token': 'ETH', 'chain_id': 42170},
    'zksync'        : {'rpc': 'https://mainnet.era.zksync.io',  'scan': 'https://explorer.zksync.io/tx',        'token': 'ETH', 'chain_id': 324},
    'celo'          : {'rpc': 'https://1rpc.io/celo',           'scan': 'https://celoscan.io/tx',               'token': 'CELO','chain_id': 42220},
    'gnosis'        : {'rpc': 'https://1rpc.io/gnosis',         'scan': 'https://gnosisscan.io/tx',             'token': 'xDAI','chain_id': 100},
    'core'          : {'rpc': 'https://rpc.coredao.org',        'scan': 'https://scan.coredao.org/tx',          'token': 'CORE','chain_id': 1116},
    'harmony'       : {'rpc': 'https://api.harmony.one',        'scan': 'https://explorer.harmony.one/tx',      'token': 'ONE', 'chain_id': 1666600000},
    'moonbeam'      : {'rpc': 'https://rpc.ankr.com/moonbeam',  'scan': 'https://moonscan.io/tx',               'token': 'GLMR','chain_id': 1284},
    'moonriver'     : {'rpc': 'https://moonriver.public.blastapi.io','scan': 'https://moonriver.moonscan.io/tx','token': 'MOVR','chain_id': 1285},
    'linea'         : {'rpc': 'https://rpc.linea.build',        'scan': 'https://lineascan.build/tx',           'token': 'ETH', 'chain_id': 59144},
    'base'          : {'rpc': 'https://mainnet.base.org',       'scan': 'https://basescan.org/tx',              'token': 'ETH', 'chain_id': 8453},
}

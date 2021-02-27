import requests
import os
import sys
from database import db, cursor

wallet_address = os.getenv('WALLET_ADDRESS')
provider = os.getenv('PROVIDER')
deposit = os.getenv('DEPOSIT')
if (wallet_address == None or provider == None):
    sys.exit('No wallet address or provider given, canceling..')

print('Getting data for address', wallet_address)

url = "https://yieldwatch.net/api/all/" + wallet_address + \
    "?platforms=beefy,pancake,auto,acryptos,venus"

headers = {
    'Host': 'yieldwatch.net',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Mobile Safari/537.36',
    'Sec-GPC': 1,
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://yieldwatch.net/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'If-None-Match': 'W/"ec9-niQ47U5RJujSs6VwouhQAR8Nk2k"',
}

req = requests.get(url, headers)

response = req.json()

provider_data = response['result'][provider]

lp_staked = provider_data['LPStaking']['totalUSDValues']
lp_staked_vaults = provider_data['LPStaking']['vaults']

staked = provider_data['staking']['totalUSDValues']
staked_vaults = provider_data['staking']['vaults']

wallet_balance = response['result']['walletBalance']['totalUSDValue']


def get_staked_tokens(staked_tokens, staked_vaults):
    print("Deposit: " + "{:.2f}USD".format(staked_tokens['deposit']) + ", Yield: " + "{:.2f}USD".format(
        staked_tokens['yield']) + ", Total: " + "{:.2f}USD".format(staked_tokens['total']))
    for stake in staked_vaults:
        print("{:.2f}".format(
            stake['depositedTokens']) + " - " + stake['depositToken'] + " deposited")
        print(stake['depositToken'] + " per USD: " +
              "{:.2f}".format(stake['priceInUSDDepositToken']))
        print("Total USD value: " +
              "{:.2f}".format(stake['depositedTokens'] * stake['priceInUSDDepositToken']))
        print("Total yield: " + "{:.2f}".format(stake['totalRewards']))
        print("********")
        sql = "INSERT INTO yield_history (pool, deposit, yield) VALUES (%s, %s, %s)"
        cursor.execute(sql, (stake['depositToken'], (stake['depositedTokens']
                                                     * stake['priceInUSDDepositToken']), stake['totalRewards']))
        db.commit()


def get_lp_tokens(lp_staked, lp_staked_vaults):
    print("Deposit: " + "{:.2f}USD".format(lp_staked['deposit']) + ", Yield: " + "{:.2f}USD".format(
        lp_staked['yield']) + ", Total: " + "{:.2f}USD".format(lp_staked['total']))
    for stake in lp_staked_vaults:
        print("{:.2f}".format(
            stake['LPInfo']['currentToken0'] * stake['LPInfo']['priceInUSDToken0'] + stake['LPInfo']['currentToken1'] * stake['LPInfo']['priceInUSDToken1']) + "USD - " + stake['name'] + " deposited")
        print("Total yield: " + "{:.2f}".format(stake['totalRewards']))
        sql = "INSERT INTO lp_yield_history (pool, deposit, yield) VALUES (%s, %s, %s)"
        cursor.execute(sql, (stake['name'], (stake['LPInfo']['currentToken0'] * stake['LPInfo']['priceInUSDToken0'] +
                                             stake['LPInfo']['currentToken1'] * stake['LPInfo']['priceInUSDToken1']), stake['totalRewards']))
        db.commit()


print("Initial deposit: " + str(deposit))
print("\nToken Stake")
get_staked_tokens(staked, staked_vaults)
print("\nLP Stake")
get_lp_tokens(lp_staked, lp_staked_vaults)
print("\nTotal amount: " +
      "{:.2f}".format(lp_staked['total'] + staked['total']))
print("Total yield: " + "{:.2f}".format(lp_staked['yield'] + staked['yield']))

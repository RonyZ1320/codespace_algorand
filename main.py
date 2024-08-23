from algokit_utils.algorand_client import (
    AlgorandClient
    AssetCreateParams,
    AssetOptInParams,
    PayParams,

)


# Client to connect to the local net
algorand = AlgorandClient.default_local_net()

dispenser = algorand.account.dispenser()
#print("Dispenser:",dispenser.address)

# Generate Creator Wallet
Creator = algorand.account.random()
#print("Creator:", creator.address)
#print(algorand.account.get_information(creator.address))

# Fund creator address with algo
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        reciever=creator.address,
        amount=10_000_00 # 10 algos
    )
)

#print(algorand.account.get_information(creator.address))

sent_txn = algorand.send.asset_create(
    AssetCreateParams(
        sender= creator.address,
        total= 100,
        asset_name="Edu4teen",
        unit_name="E4T",
    )
)

asset_id = sent_txn("confirmation")("asset-index")
#print("Asset ID:", asset_id)

reciever_acct = algorand.account.random()

algorand.send.payment(
    PayParams(
    sender=dispenser.address,
    reciever=reciever_acct.address,
    amount=10_000_00 # 10 algos
    )
)

print(algorand.account.get_information(reciever_acct.address)

# create a group txn
group_txn = algorand.new_group()

group_txn.add_asset_opt_in(
    AssetOptInParams(
        sender=receiver_acct.address,
        asset_id=asset_id
    )
)

group_txn.add_payment(
    PayParams(
        sender=receiver_acct.address,
        receiver=creator.address,
        amount=10_000_000 # 10 algo
    )
)

group_txn.add_asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=receiver_acct.address,
        asset_id=asset_id,
        amount=10
    )
)

group_txn.execute()

print("Efo -> Receiver Account Asset Balance:", algorand.account.get_information(receiver_acct.address)['assets'][0]['amount'])
print("Efo -> Creator Account Asset Balance:", algorand.account.get_information(creator.address)['assets'][0]['amount'])

import os
from web3 import Web3
from src.configs import logger


def deploy_contract(contract_data):
    try:
        w3 = Web3(Web3.HTTPProvider(os.getenv("BCH_PROVIDER_URL")))

        # make contract from compiled code
        NeoFundContract = w3.eth.contract(
            abi=contract_data["build"]["abi"],
            bytecode=contract_data["build"]["bytecode"],
        )
        nonce = w3.eth.get_transaction_count(os.getenv("PUB_ADDR"))
        transaction = NeoFundContract.constructor().buildTransaction(
            {
                "chainId": int(os.getenv("BCH_PROVIDER_CHAIN_ID")),
                "from": os.getenv("PUB_ADDR"),
                "nonce": nonce,
                "gasPrice": w3.eth.gas_price,
            }
        )

        signed_tx = w3.eth.account.sign_transaction(
            transaction, private_key=os.getenv("PRIV_KEY")
        )

        logger.info("Sending contract creation TX...")
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        logger.info("Sending contract creation TX. DONE!")
        logger.info(f"Contract creation TX hash: {tx_hash.hex()}")

        logger.info("Waiting for Block confirmation...")
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        logger.info("Block confirmation. DONE!")
        logger.info(f"Contract address {tx_receipt.contractAddress}")

        return {
            "success": True,
            "data": {"w3": w3, "tx_hash": tx_hash, "tx_receipt": tx_receipt},
        }

    except:
        logger.exception(f"Error white deploying contract {contract_data['name']}")
        return {"success": False}

from web3.contract import Contract
from dotenv import load_dotenv
from pytest import fixture

from src.scripts.deploy import deploy_contract


@fixture()
def setup():
    load_dotenv(".env.test", override=True)


@fixture()
def test_contract_data():
    return {
        "name": "TestContract",
        "build": {
            "abi": [
                {
                    "inputs": [],
                    "name": "hi",
                    "outputs": [
                        {"internalType": "string", "name": "", "type": "string"}
                    ],
                    "stateMutability": "view",
                    "type": "function",
                }
            ],
            "bytecode": "608060405234801561001057600080fd5b50610123806100206000396000f3fe6080604052348015600f57600080fd5b506004361060285760003560e01c8063a99dca3f14602d575b600080fd5b603360ab565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101560715780820151818401526020810190506058565b50505050905090810190601f168015609d5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b60606040518060600160405280602281526020016100cc6022913990509056fe7468697320697320612074657374207665727920736d61727420636f6e7472616374a2646970667358221220870d1a0e627c92fdc396fd2aeeb55d21d68093c9e2e15ee9b7e0705e0bb0149564736f6c63430007060033",
        },
    }


@fixture()
def deployed_contract():
    NEO_FUND_CONTRACT_DATA = {
        "name": "NeoFund",
        "build": {
            "abi": [
                {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
                {
                    "inputs": [],
                    "name": "fund",
                    "outputs": [],
                    "stateMutability": "payable",
                    "type": "function",
                },
                {
                    "inputs": [
                        {"internalType": "uint256", "name": "", "type": "uint256"}
                    ],
                    "name": "funders",
                    "outputs": [
                        {"internalType": "address", "name": "", "type": "address"}
                    ],
                    "stateMutability": "view",
                    "type": "function",
                },
                {
                    "inputs": [
                        {"internalType": "address", "name": "", "type": "address"}
                    ],
                    "name": "funders_amount",
                    "outputs": [
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {"internalType": "bool", "name": "exists", "type": "bool"},
                    ],
                    "stateMutability": "view",
                    "type": "function",
                },
                {
                    "inputs": [],
                    "name": "get_contract_balance",
                    "outputs": [
                        {"internalType": "uint256", "name": "", "type": "uint256"}
                    ],
                    "stateMutability": "view",
                    "type": "function",
                },
                {
                    "inputs": [],
                    "name": "owner",
                    "outputs": [
                        {"internalType": "address", "name": "", "type": "address"}
                    ],
                    "stateMutability": "view",
                    "type": "function",
                },
                {
                    "inputs": [
                        {
                            "internalType": "uint256",
                            "name": "withdraw_amount",
                            "type": "uint256",
                        }
                    ],
                    "name": "withdraw",
                    "outputs": [],
                    "stateMutability": "payable",
                    "type": "function",
                },
            ],
            "bytecode": "608060405234801561001057600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550610757806100606000396000f3fe6080604052600436106100555760003560e01c80632e1a7d4d1461005a5780638da5cb5b14610088578063b60d4288146100c9578063c22f63cc146100d3578063dc0d3dff14610141578063f0bc153a146101a6575b600080fd5b6100866004803603602081101561007057600080fd5b81019080803590602001909291905050506101d1565b005b34801561009457600080fd5b5061009d610491565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6100d16104b5565b005b3480156100df57600080fd5b50610122600480360360208110156100f657600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610649565b6040518083815260200182151581526020019250505060405180910390f35b34801561014d57600080fd5b5061017a6004803603602081101561016457600080fd5b810190808035906020019092919050505061067a565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b3480156101b257600080fd5b506101bb6106b9565b6040518082815260200191505060405180910390f35b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614610275576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252602a8152602001806106f8602a913960400191505060405180910390fd5b478111156102ce576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260368152602001806106c26036913960400191505060405180910390fd5b60008060005b838310806102ea57506001805490508261ffff16115b1561044457600060018361ffff168154811061030257fe5b9060005260206000200160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1690506000600260008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060000154905060008114156103865750506102d4565b85818601111561039a5784860392506103e0565b600260008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000015492505b828501945082600260008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060000160008282540392505081905550838060010194505050506102d4565b3373ffffffffffffffffffffffffffffffffffffffff166108fc859081150290604051600060405180830381858888f1935050505015801561048a573d6000803e3d6000fd5b5050505050565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060010160009054906101000a900460ff161561055f5734600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060000160008282540192505081905550610647565b604051806040016040528034815260200160011515815250600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000820151816000015560208201518160010160006101000a81548160ff0219169083151502179055509050506001339080600181540180825580915050600190039060005260206000200160009091909190916101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505b565b60026020528060005260406000206000915090508060000154908060010160009054906101000a900460ff16905082565b6001818154811061068a57600080fd5b906000526020600020016000915054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60004790509056fe416d6f756e7420746f2077697468647261772069732067726561746572207468616e207468652061637475616c2062616c616e63652e4f6e6c792061646d696e2063616e2077697468647261772066726f6d2074686520636f6e74726163742ea264697066735822122015c8860345171215784ece09e7024ec4110caf1c96620ef43adde5769a4a4eb164736f6c63430007060033",
        },
    }

    result = deploy_contract(NEO_FUND_CONTRACT_DATA)
    if not result["success"]:
        raise Exception("Error while making deployed_contract fixture")

    neo_fund_contract: Contract = result["data"]["w3"].eth.contract(
        address=result["data"]["tx_receipt"].contractAddress,
        abi=NEO_FUND_CONTRACT_DATA["build"]["abi"],
    )

    return {"contract": neo_fund_contract, **result["data"], **NEO_FUND_CONTRACT_DATA}

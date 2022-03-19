import json
import os
from src.configs import logger
from solcx import compile_standard, install_solc


def compile_contract(sol_file_name, contract_name):
    try:
        logger.info(f"Installign solidity version {os.getenv('SOLIDITY_VER')}")
        install_solc(os.getenv("SOLIDITY_VER"))
        logger.info(f"Installign solidity version {os.getenv('SOLIDITY_VER')}. Done!")

        with open(f"src/contracts/{sol_file_name}") as f:
            sol_code = f.read()

        compiled_sol = compile_standard(
            {
                "language": "Solidity",
                "sources": {sol_file_name: {"content": sol_code}},
                "settings": {
                    "outputSelection": {
                        "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                    }
                },
            },
            solc_version=os.getenv("SOLIDITY_VER"),
        )

        with open(f"build/{sol_file_name}.compiled.json", "w") as f:
            json.dump(compiled_sol, f, indent=3)

        return {
            "success": True,
            "data": {
                "name": contract_name,
                "build": {
                    "abi": compiled_sol["contracts"][sol_file_name][contract_name][
                        "abi"
                    ],
                    "bytecode": compiled_sol["contracts"][sol_file_name][contract_name][
                        "evm"
                    ]["bytecode"]["object"],
                },
            },
        }

    except:
        logger.exception(f"Error while compiling contract {contract_name}")
        return {"success": False}

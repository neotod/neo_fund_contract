import os
import pytest
from web3 import exceptions


def test_contract_state_vars(setup, deployed_contract):
    # test contract state variables at the beginging

    contract_balance = (
        deployed_contract["contract"].functions.get_contract_balance().call()
    )
    assert contract_balance == 0

    result = (
        deployed_contract["contract"]
        .functions.funders_amount(os.getenv("PUB_ADDR"))
        .call()
    )
    amount, funder_exists = result

    assert amount == 0
    assert funder_exists == False


def test_contract_fund_and_withdraw(setup, deployed_contract):
    # test contract fund and withdraw functions

    AMOUNT_TO_WITHDRAW = 50
    FUNDING_AMOUNT = 100

    # fund FUNDER_AMOUNT Wei to contract and expecting added balance
    deployed_contract["contract"].functions.fund().transact(
        {"from": os.getenv("PUB_ADDR"), "value": FUNDING_AMOUNT}
    )

    # get contract_balance and expecting it to get increased to FUNDING_AMOUNt
    contract_balance = (
        deployed_contract["contract"].functions.get_contract_balance().call()
    )
    assert contract_balance == FUNDING_AMOUNT

    # get funded amount (wei) with fudned address and expecting to be equal to FUNDING_AMOUNt
    result = (
        deployed_contract["contract"]
        .functions.funders_amount(os.getenv("PUB_ADDR"))
        .call()
    )
    amount, funder_exists = result

    assert amount == FUNDING_AMOUNT
    assert funder_exists == True

    # get first funder and expecting to be PUB_ADDR
    funder_address = deployed_contract["contract"].functions.funders(0).call()
    assert funder_address == os.getenv("PUB_ADDR")

    # test withdraw function of contract
    deployed_contract["contract"].functions.withdraw(AMOUNT_TO_WITHDRAW).transact(
        {"from": os.getenv("PUB_ADDR")}
    )

    # get contract_balance and expecting it to get decreased by AMOUNT_TO_WITHDRAW
    contract_balance = (
        deployed_contract["contract"].functions.get_contract_balance().call()
    )
    assert contract_balance == FUNDING_AMOUNT - AMOUNT_TO_WITHDRAW

    # get funded amount (wei) by PUB_ADDR address and expecting to be equal to FUNDING_AMOUNT - AMOUNT_TO_WITHDRAW
    result = (
        deployed_contract["contract"]
        .functions.funders_amount(os.getenv("PUB_ADDR"))
        .call()
    )
    amount, funder_exists = result

    assert amount == FUNDING_AMOUNT - AMOUNT_TO_WITHDRAW
    assert funder_exists == True

    # widthrawing a value more than contract balance and epxecting to fail (Revert)

    with pytest.raises(
        exceptions.ContractLogicError,
        match=".* Amount to withdraw is greater than the actual balance.$",
    ):
        deployed_contract["contract"].functions.withdraw(FUNDING_AMOUNT + 100).transact(
            {"from": os.getenv("PUB_ADDR")}
        )

    # calling widthraw from another address and epxecting to fail (Revert) because only admin can withdraw!
    with pytest.raises(
        exceptions.ContractLogicError,
        match=".* Only admin can withdraw from the contract.$",
    ):
        SOME_ADDRESS = "0x7Ac8Fd69dEeeD24821333917f636E516EC70219E"
        deployed_contract["contract"].functions.withdraw(FUNDING_AMOUNT + 100).transact(
            {"from": SOME_ADDRESS}
        )

from src.scripts.deploy import deploy_contract


def test_deploy_success(setup, test_contract_data):
    # test deploy contract funtion and expecting success result
    result = deploy_contract(test_contract_data)

    assert result != None

    try:
        assert result["success"] == True
    except:
        assert False, "success key is missing"

    try:
        assert result["data"] != None
    except:
        assert False, "data key is missing"

    try:
        assert result["data"]["w3"] != None
    except:
        assert False, "data.w3 key is missing"

    try:
        assert result["data"]["tx_hash"] != None
    except:
        assert False, "data.tx_hash key is missing"

    try:
        assert result["data"]["tx_receipt"] != None
    except:
        assert False, "data.tx_receipt key is missing"

    assert result["data"]["tx_hash"] == result["data"]["tx_receipt"].transactionHash

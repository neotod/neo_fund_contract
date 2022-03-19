from src.scripts.compile import compile_contract


def test_compile_success(setup):
    # test compile contract funtion and expecting success result

    CONTRACT_FILE_NAME = "neo_fund.sol"
    CONTRACT_NAME = "NeoFund"

    result = compile_contract(CONTRACT_FILE_NAME, CONTRACT_NAME)
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
        assert result["data"]["name"] != None
    except:
        assert False, "data.name key is missing"

    assert result["data"]["name"] == CONTRACT_NAME

    try:
        assert result["data"]["build"] != None
    except:
        assert False, "data.build key is missing"

    try:
        assert result["data"]["build"]["abi"] != None
    except:
        assert False, "data.build.abi key is missing"

    try:
        assert result["data"]["build"]["bytecode"] != None
    except:
        assert False, "data.build.bytecode key is missing"


def test_compile_fail(setup):
    # test compile contract funtion and expecting failed result

    # bad contract file name
    CONTRACT_FILE_NAME = "bad_contract_file_name.sol"
    CONTRACT_NAME = "NeoFund"

    result = compile_contract(CONTRACT_FILE_NAME, CONTRACT_NAME)
    assert result != None

    try:
        assert result["success"] == False
    except:
        assert False, "success key is missing"

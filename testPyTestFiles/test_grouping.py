import pytest
@pytest.mark.sanity
def test_LoginByEmail():
    print("test_LoginByEmail is running")
    assert True
@pytest.mark.sanity
def test_LoginByFacebook():
    print("test_LoginByFacebook is running")
    assert True
@pytest.mark.regression
def test_LoginByMobileNumber():
    print("test_LoginByMobileNumber is running")
    assert True
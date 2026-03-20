import pytest

@pytest.fixture
def name(request):
    return request.config.getoption("--name")

def test_greet(name):
    print(f"Hello, {name}")
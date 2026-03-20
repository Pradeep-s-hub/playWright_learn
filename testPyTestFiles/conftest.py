
import pytest
@pytest.fixture
def setup():
    print("setup is running") 
    print("browser setup")
    yield ["chrome", "firefox", "edge"] 
    print()
    print("teardown code: close the browser")
    
def pytest_addoption(parser):
    parser.addoption("--name", action="store", default="Guest", help="User name")
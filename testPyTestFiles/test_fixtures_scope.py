import pytest
@pytest.fixture(scope="module")
def setup():
    print("setup is running") 
    print("browser setup")
class TestFixtures:
    def test_fixture_m1(self, setup):
        print("test_fixture_m1 is running")
    def test_fixture_m2(self, setup):
        print("test_fixture_m2 is running")
class TestFixturesNew:
    def test_fixture_m3(self, setup):
        print("test_fixture_m3 is running")
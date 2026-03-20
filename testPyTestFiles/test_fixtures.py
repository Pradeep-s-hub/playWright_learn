import pytest
class TestFixtures:
    @pytest.fixture
    def setup(self):
        print("setup is running") 
        print("browser setup")
    def test_fixture_m1(self, setup):
        print("test_fixture_m1 is running")
    def test_fixture_m2(self, setup):
        print("test_fixture_m2 is running")
        
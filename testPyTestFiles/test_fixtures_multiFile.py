import pytest
class TestFixtures:
    def test_fixture_m1(self, setup):
        print("test_fixture_m1 is running")
    def test_fixture_m2(self, setup):
        print("test_fixture_m2 is running")
        
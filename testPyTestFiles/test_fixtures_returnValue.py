import pytest
class TestFixtures:
    def test_fixture_m1(self, setup):
        print(setup)
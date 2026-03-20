import pytest
class TestFixtures:
    def test_fixture_m1(self):
        print("test_fixture_m1 is running")
    def test_fixture_m2(self):
        print("test_fixture_m2 is running")
    @pytest.mark.skip(reason="skipping this test for demo")
    def test_skipped(self):
        print("test_skipped is running")
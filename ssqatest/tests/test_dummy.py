import pytest

@pytest.mark.usefixtures("init_driver")
class TestDummy:
    def test_dummy_function(self):
        print("Testing dummy function")
        self.driver.get("http://google.com")
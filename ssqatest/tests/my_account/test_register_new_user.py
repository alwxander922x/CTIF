import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
import random
import string
import pdb

@pytest.mark.usefixtures("init_driver")


class TestRegisterNewUser:
    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(15))
        random_email = random_string
        username = random_email
        password = random_email
        my_account_o = MyAccountSignedOut(self.driver)
        my_account_o.go_to_my_account()
        my_account_o.input_register_email(username + str("@rambler.com"))
        my_account_o.input_register_password(password + str("123EERT"))
        pdb.set_trace()
        my_account_o.click_register_button()
        my_account_o.wait_until_message_of_successful_reg_is_displayed('')
        expected_message = f"Hello {username} (not {username}? Log out)"
        my_account_o.wait_until_message_of_successful_reg_is_displayed(expected_message)

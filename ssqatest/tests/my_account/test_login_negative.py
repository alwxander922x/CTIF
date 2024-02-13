import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")


class TestLoginNegative:
    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username('saaadassd')
        my_account.input_login_password('safsjdnkmldfs')
        my_account.click_login_button()
        expected_err = 'Error: The username saaadassd is not registered on this site. If you are unsure of your username, try your email address instead.'
        my_account.wait_until_error_is_displayed(expected_err)



# test_login_none_existing_user_ccde(self):
#         my_account_ccde = MyAccountSignedOut(self.driver)
#         my_account_ccde.go_to_my_account_ccde()
#         my_account_ccde.input_login_username_ccde('saa')
#         my_account_ccde.input_login_password_ccde('nope')
#         my_account_ccde.click_on_login_button_ccde()
#         expected_err = "Ne pare rău, numele de utilizator sau parola sunt eronate. "
#         my_account_ccde.wait_until_error_is_displayed_ccde(expected_err)
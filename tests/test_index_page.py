from pytest import mark
from env_setup import EnvVariables as Env


@mark.smoke
def test_successful_login(index_page):
    index_page.perform_login(
        username=Env.USERNAME,
        password=Env.PASSWORD
    )
    index_page.is_logged()


invalid_login = (
    ["", Env.PASSWORD, "Username field cannot be empty"],
    [Env.USERNAME, "", "Password field cannot be empty"],
    [Env.USERNAME, "wrong_password", "Password or username is incorrect"]
)


@mark.parametrize("username_param, password_param, error_msg_param", invalid_login,
                  ids=["empty username", "empty password", "invalid creds"])
def test_unsuccessful_login(index_page, username_param, password_param, error_msg_param):
    index_page.perform_login(
        username=username_param,
        password=password_param
    )
    index_page.is_error_msg_correct(
        expected_msg=error_msg_param
    )

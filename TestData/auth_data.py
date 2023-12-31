import dataclasses


"""В этом файле хранятся входные данные для проверок"""

@dataclasses.dataclass
class LogInParameters:
    login: str = None
    password: str = None

def return_valid_auth_data():
    return LogInParameters(
        login='standard_user',
        password='secret_sauce'
    )

def return_not_existing_data():
    login = [
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
    ]
    password = [
        "secret_sauce"
    ]
    return login, password

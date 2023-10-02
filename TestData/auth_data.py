import dataclasses
import random


@dataclasses.dataclass
class LogInParameters:
    login: str = None
    password: str = None


def return_valid_auth_data():
    return LogInParameters(
        login='standard_user1',
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

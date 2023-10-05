# Script that asks the user for their SPOTIFY_CLIENT_SECRET and
# SPOTIFY_CLIENT_ID, creates a .env file and populates it with them

# check file exists > if not then create one and say you are > then take input > then write to file

import os
import re


def check_for_env_file():
    return os.path.isfile(".env")


def is_hex(s: str):
    return re.fullmatch(r"[0-9a-fA-F]*", s) is not None


def check_api_variable_length(spotify_client_var: str, spotify_client_var_name: str):
    if len(spotify_client_var) != 32 or not is_hex(spotify_client_var):
        raise ValueError(f"{spotify_client_var_name} must be 32 characters long.")


def get_input(spotify_client_var_name: str) -> str:
    spotify_client_var = input(
        f"Please input your {spotify_client_var_name} (32 character string): "
    )
    check_api_variable_length(spotify_client_var, spotify_client_var_name)

    return spotify_client_var.strip("'\"")


def write_to_env(spotify_client_var_name: str, spotify_client_var: str):
    with open(".env", "w") as f:
        f.write(f"{spotify_client_var_name}=" + '"' + spotify_client_var + '"' + "\n")


def execute():
    if check_for_env_file() == False:
        print("Creating .env file.")
    spotify_client_id = get_input(spotify_client_var_name="SPOTIFY_CLIENT_ID")
    spotify_client_secret = get_input(spotify_client_var_name="SPOTIFY_CLIENT_SECRET")
    write_to_env(spotify_client_id, spotify_client_secret)


if __name__ == "__main__":
    execute()

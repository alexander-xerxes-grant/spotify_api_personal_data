# Script that asks the user for their SPOTIFY_CLIENT_SECRET and
# SPOTIFY_CLIENT_ID, creates a .env file and populates it with them

# check file exists > if not then create one and say you are > then take input > then write to file

import os


def check_for_env_file():
    return os.path.isfile(".env")


def check_api_variable_length(spotify_client_var, spotify_client_var_name):
    if len(spotify_client_var) != 32:
        raise ValueError(f"{spotify_client_var_name} must be 32 characters long.")


def get_input(spotify_client_var_name):
    spotify_client_var = input(
        f"Please input your {spotify_client_var_name} (32 character string): "
    )
    check_api_variable_length(spotify_client_var, spotify_client_var_name)

    return spotify_client_var.strip("'\"")


def write_to_env(spotify_client_id, spotify_client_secret):
    with open(".env", "w") as f:
        f.write("SPOTIFY_CLIENT_ID=" + '"' + spotify_client_id + '"' + "\n")
        f.write("SPOTIFY_CLIENT_SECRET=" + '"' + spotify_client_secret + '"')


def execute():
    if check_for_env_file() == False:
        print("Creating .env file.")
    spotify_client_id, spotify_client_secret = get_input(spotify_client_var_name)
    write_to_env(spotify_client_id, spotify_client_secret)


if __name__ == "__main__":
    execute()

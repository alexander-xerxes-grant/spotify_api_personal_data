from scripts.setup import check_for_env_file, get_input, check_api_variable_length
from unittest.mock import patch
import pytest


def test_check_for_env_file_returns_false_when_no_env_file():
    with patch("os.path.isfile", return_value=False):
        assert check_for_env_file() == False


def test_function_raises_on_incorrect_string_length():
    mock_spotify_client_var = "not32characterslong"
    mock_spotify_client_var_name = "SPOTIFY_CLIENT_ID"
    with pytest.raises(ValueError) as e:
        check_api_variable_length(mock_spotify_client_var, mock_spotify_client_var_name)

    assert str(e.value) == f"{mock_spotify_client_var_name} must be 32 characters long."

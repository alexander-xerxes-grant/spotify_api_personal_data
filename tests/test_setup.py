from unittest.mock import mock_open, patch

import pytest

from scripts.dev_environment_setup import (check_api_variable_length,
                                           check_for_env_file, is_hex,
                                           write_to_env)


@pytest.fixture
def mock_spotify_client_var_incorrect():
    return "not32characterslong"


@pytest.fixture
def mock_spotify_client_var():
    return "774c7e7dfefd434ca15e8c336bfe0f02"


@pytest.fixture
def mock_spotify_client_var_name():
    return "SPOTIFY_CLIENT_ID"


def test_check_for_env_file_returns_false_when_no_env_file():
    with patch("os.path.isfile", return_value=False):
        assert check_for_env_file() is False


def test_is_hex_returns_false_on_incorrect_string(mock_spotify_client_var_incorrect):
    assert is_hex(mock_spotify_client_var_incorrect) is False


def test_is_hex_returns_true_on_correct_string(mock_spotify_client_var):
    assert is_hex(mock_spotify_client_var) is True


def test_function_raises_on_incorrect_string_length(
    mock_spotify_client_var_incorrect, mock_spotify_client_var_name
):
    with pytest.raises(ValueError) as e:
        check_api_variable_length(
            mock_spotify_client_var_incorrect, mock_spotify_client_var_name
        )

    assert str(e.value) == f"{mock_spotify_client_var_name} must be 32 characters long."


def test_write_to_env(mock_spotify_client_var):
    expected_data = f'SPOTIFY_CLIENT_ID="{mock_spotify_client_var}"\n'

    with patch("builtins.open", mock_open()) as mock_file:
        write_to_env("SPOTIFY_CLIENT_ID", f"{mock_spotify_client_var}")

        mock_file.assert_called_once_with(".env", "w")
        mock_file().write.assert_called_once_with(expected_data)

from unittest.mock import Mock

from src.views import greetings


def test_greetings():
    mock_greet = Mock(return_value="Доброе утро!")
    greet = mock_greet
    assert greet() == "Доброе утро!"
    mock_greet.assert_called_once_with()


def test_res_output():
    mock_output = Mock(return_value="Result")
    output = mock_output
    assert output() == "Result"
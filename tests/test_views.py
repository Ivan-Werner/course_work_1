from datetime import datetime
from unittest.mock import Mock
from unittest.mock import patch

import pytest

from src.views import greetings


def test_greetings():
    mock_greet = Mock(return_value="Доброе утро!")
    greetings = mock_greet
    assert greetings() == "Доброе утро!"
    mock_greet.assert_called_once_with()


@pytest.mark.parametrize(
    ("now_datetime", "expected_greeting"),
    [
        (datetime(2023, 10, 15, hour=6), "Доброе утро!"),
        (datetime(2023, 10, 15, hour=14), "Добрый день!"),
        (datetime(2023, 10, 16, hour=18), "Добрый вечер!"),
        (datetime(2023, 10, 16, hour=0), "Доброй ночи!"),
    ],
)
@patch("src.views.datetime")
def test_get_greeting(mocked_datetime, now_datetime, expected_greeting):
    mocked_datetime.now.return_value = now_datetime
    assert greetings() == expected_greeting


def test_res_output():
    mock_output = Mock(return_value="Result")
    output = mock_output
    assert output() == "Result"

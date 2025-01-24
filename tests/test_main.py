from unittest.mock import patch

from src.main import service_running, report_running


@patch('builtins.input')
def test_service_running(mock_input):
    mock_input.return_value = 'empty'
    assert service_running() is None

@patch('builtins.input', side_effect=["empty", '10.10.2021'])
def test_report_running(mock_input):
    mock_input.return_value = "empty"
    mock_input.return_value = '10.10.2021'
    assert report_running() is None

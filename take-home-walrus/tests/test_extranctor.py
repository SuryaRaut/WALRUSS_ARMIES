import pytest
import requests
from requests.exceptions import HTTPError, Timeout, RequestException
from unittest.mock import patch, MagicMock
from extractor.crowdstrike import get_host_from_crowdstrikes
from extractor.qualys import get_host_from_qualys


# Test successful response from Qualys API
@patch('requests.post')
def test_get_host_from_qualys_success(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": "1", "hostname": "test-host"}]
    
    # Set the mock response for the API call
    mock_post.return_value = mock_response

    # Call the actual function
    result = get_host_from_qualys()

    # Assertions
    mock_post.assert_called_once()  # Ensure API was called
    assert result == [{"id": "1", "hostname": "test-host"}]  # Check response

# Test HTTPError handling
@patch('requests.post')
def test_get_host_from_qualys_http_error(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.raise_for_status.side_effect = HTTPError("Bad request")

    mock_post.return_value = mock_response

    # Call the function and expect an HTTPError
    with pytest.raises(HTTPError):
        get_host_from_qualys()

    # Ensure API was called
    mock_post.assert_called_once()

# Test Timeout error handling
@patch('requests.post')
def test_get_host_from_qualys_timeout(mock_post):
    mock_post.side_effect = Timeout("Request timed out")

    # Call the function and expect a Timeout error
    with pytest.raises(Timeout):
        get_host_from_qualys()

    # Ensure API was called
    mock_post.assert_called_once()

# Test network-related errors (RequestException)
@patch('requests.post')
def test_get_host_from_qualys_request_exception(mock_post):
    mock_post.side_effect = RequestException("Network error")

    # Call the function and expect a RequestException
    with pytest.raises(RequestException):
        get_host_from_qualys()

    # Ensure API was called
    mock_post.assert_called_once()

# Test ValueError (JSON parse error)
@patch('requests.post')
def test_get_host_from_qualys_json_parse_error(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError("Invalid JSON")

    mock_post.return_value = mock_response

    # Call the function and expect a ValueError
    with pytest.raises(ValueError):
        get_host_from_qualys()

    # Ensure API was called
    mock_post.assert_called_once()

# Test for unexpected error handling
@patch('requests.post')
def test_get_host_from_qualys_unexpected_error(mock_post):
    mock_post.side_effect = Exception("Unexpected error")

    # Call the function and expect a general Exception
    with pytest.raises(Exception):
        get_host_from_qualys()

    # Ensure API was called
    mock_post.assert_called_once()


# Test successful response from Crowdstrikes API
@patch('requests.post')
def test_get_host_from_crowdstrikes(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": "1", "hostname": "test-host"}]
    
    # Set the mock response for the API call
    mock_post.return_value = mock_response

    # Call the actual function
    result = get_host_from_crowdstrikes()

    # Assertions
    mock_post.assert_called_once()  # Ensure API was called
    assert result == [{"id": "1", "hostname": "test-host"}]  # Check response

# Test HTTPError handling
@patch('requests.post')
def test_get_host_from_crowdstrikes_http_error(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.raise_for_status.side_effect = HTTPError("Bad request")

    mock_post.return_value = mock_response

    # Call the function and expect an HTTPError
    with pytest.raises(HTTPError):
        get_host_from_crowdstrikes()

    # Ensure API was called
    mock_post.assert_called_once()

# Test Timeout error handling
@patch('requests.post')
def test_get_host_from_crowdstrikes_timeout(mock_post):
    mock_post.side_effect = Timeout("Request timed out")

    # Call the function and expect a Timeout error
    with pytest.raises(Timeout):
        get_host_from_crowdstrikes()

    # Ensure API was called
    mock_post.assert_called_once()

# Test network-related errors (RequestException)
@patch('requests.post')
def test_get_host_from_crowdstrikes_request_exception(mock_post):
    mock_post.side_effect = RequestException("Network error")

    # Call the function and expect a RequestException
    with pytest.raises(RequestException):
        get_host_from_crowdstrikes()

    # Ensure API was called
    mock_post.assert_called_once()

# Test ValueError (JSON parse error)
@patch('requests.post')
def test_get_host_from_crowdstrikes_json_parse_error(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError("Invalid JSON")

    mock_post.return_value = mock_response

    # Call the function and expect a ValueError
    with pytest.raises(ValueError):
        get_host_from_crowdstrikes()

    # Ensure API was called
    mock_post.assert_called_once()

# Test for unexpected error handling
@patch('requests.post')
def test_get_host_from_crowdstrikes_unexpected_error(mock_post):
    mock_post.side_effect = Exception("Unexpected error")

    # Call the function and expect a general Exception
    with pytest.raises(Exception):
        get_host_from_crowdstrikes()

    # Ensure API was called
    mock_post.assert_called_once()


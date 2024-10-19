import pytest
from unittest.mock import patch, MagicMock
from storage.mongo_storage import persist_dedups_hosts

# Mock pymongo MongoClient
@patch('storage.mongo_storage.MongoClient')
def test_persist_dedups_hosts_success(mock_mongo_client):
    # Mock the MongoDB client, database, and collection
    mock_client = MagicMock()
    mock_db = MagicMock()
    mock_collection = MagicMock()

    # Simulate a successful insert_many
    mock_collection.insert_many.return_value.inserted_ids = ['id1', 'id2', 'id3']

    # Mock the return values for client, db, and collection
    mock_mongo_client.return_value = mock_client
    mock_client.__getitem__.return_value = mock_db
    mock_db.__getitem__.return_value = mock_collection

    # Call the function with valid hosts data
    hosts = [{"id": "1", "hostname": "host1"}, {"id": "2", "hostname": "host2"}]
    persist_dedups_hosts(hosts)

    # Assertions
    mock_mongo_client.assert_called_once()  # Ensure MongoClient was called
    mock_collection.insert_many.assert_called_once_with(hosts)  # Ensure insert_many was called with hosts
    assert mock_collection.insert_many.call_count == 1  # Ensure insert_many was called exactly once


# Test empty list handling
@patch('storage.mongo_storage.MongoClient')
def test_persist_dedups_hosts_empty_list(mock_mongo_client):
    hosts = []

    # Call the function with an empty list
    persist_dedups_hosts(hosts)

    # Ensure MongoClient is never called when the list is empty
    mock_mongo_client.assert_not_called()


# Test exception handling during database operation
@patch('storage.mongo_storage.MongoClient')
def test_persist_dedups_hosts_exception(mock_mongo_client):
    # Mock the MongoDB client, database, and collection
    mock_client = MagicMock()
    mock_db = MagicMock()
    mock_collection = MagicMock()

    # Simulate an exception during insert_many
    mock_collection.insert_many.side_effect = Exception("MongoDB insertion error")

    # Mock the return values for client, db, and collection
    mock_mongo_client.return_value = mock_client
    mock_client.__getitem__.return_value = mock_db
    mock_db.__getitem__.return_value = mock_collection

    # Call the function with valid hosts data
    hosts = [{"id": "1", "hostname": "host1"}, {"id": "2", "hostname": "host2"}]

    # Expect the function to handle the exception and not raise it
    persist_dedups_hosts(hosts)

    # Ensure insert_many was called and an exception occurred
    mock_collection.insert_many.assert_called_once_with(hosts)
    assert mock_collection.insert_many.call_count == 1

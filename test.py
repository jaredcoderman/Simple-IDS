import pytest
from unittest.mock import MagicMock
from datetime import datetime
from your_module import Watcher  # Replace with your actual import path

@pytest.fixture
def mock_event():
    # Create a mock event object to simulate a file modification event
    mock_event = MagicMock()
    mock_event.is_directory = False  # Simulate it's a file
    mock_event.event_type = 'modified'
    mock_event.src_path = '/test_dir/file.txt'
    return mock_event

def test_on_modified(mock_event, capsys):
    # Create a Watcher instance
    watcher = Watcher()

    # Call the on_modified method with the mock event
    watcher.on_modified(mock_event)

    # Capture the output
    captured = capsys.readouterr()

    # Check if the output matches the expected pattern
    assert f"Event: modified | File: /test_dir/file.txt" in captured.out
    assert str(datetime.now().date()) in captured.out  # Date check for dynamic timestamp

def test_on_created(mock_event, capsys):
    mock_event.event_type = 'created'
    watcher = Watcher()
    watcher.on_created(mock_event)
    captured = capsys.readouterr()
    assert f"Event: created | File: /test_dir/file.txt" in captured.out

import pytest
from unittest.mock import MagicMock
from datetime import datetime
from classes.watcher import Watcher

@pytest.fixture
def mock_event():
    mock_event = MagicMock()
    mock_event.is_directory = False
    mock_event.event_type = 'modified'
    mock_event.src_path = '/test_dir/file.txt'
    return mock_event

def test_on_modified(mock_event, capsys):
    watcher = Watcher()

    watcher.on_modified(mock_event)

    captured = capsys.readouterr()

    assert f"Event: modified | File: /test_dir/file.txt" in captured.out
    assert str(datetime.now().date()) in captured.out

def test_on_created(mock_event, capsys):
    mock_event.event_type = 'created'
    watcher = Watcher()
    watcher.on_created(mock_event)
    captured = capsys.readouterr()
    assert f"Event: created | File: /test_dir/file.txt" in captured.out

def test_on_deleted(mock_event, capsys):
    mock_event.event_type = 'deleted'
    watcher = Watcher()
    watcher.on_deleted(mock_event)
    captured = capsys.readouterr()
    assert f"Event: deleted | File: /test_dir/file.txt" in captured.out


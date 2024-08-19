import pytest
from project import add_task, mark_done, delete_task, view_tasks

def test_add_task():
    tasks = []
    add_task(tasks, "Buy groceries")
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Buy groceries"
    assert not tasks[0]["done"]

def test_mark_done():
    tasks = [{"task": "Buy groceries", "done": False}]
    result = mark_done(tasks, 0)
    assert result is True
    assert tasks[0]["done"] is True

def test_mark_done_invalid():
    tasks = [{"task": "Buy groceries", "done": False}]
    result = mark_done(tasks, 1)  # Invalid index
    assert result is False
    assert tasks[0]["done"] is False

def test_delete_task():
    tasks = [{"task": "Buy groceries", "done": False}, {"task": "Walk the dog", "done": True}]
    result = delete_task(tasks, 0)
    assert result is True
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Walk the dog"

def test_delete_task_invalid():
    tasks = [{"task": "Buy groceries", "done": False}]
    result = delete_task(tasks, 1)  # Invalid index
    assert result is False
    assert len(tasks) == 1

def test_view_tasks(capsys):
    tasks = [
        {"task": "Buy groceries", "done": False},
        {"task": "Walk the dog", "done": True},
    ]
    view_tasks(tasks)
    captured = capsys.readouterr()
    assert "1. Buy groceries [Not Done]" in captured.out
    assert "2. Walk the dog [Done]" in captured.out

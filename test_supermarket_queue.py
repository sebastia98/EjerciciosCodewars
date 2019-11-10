from supermarket_queue import queue_time

def test_uno():
    assert queue_time([5], 1) == 5

def test_dos():
    assert queue_time([5, 2, 3, 5, 4, 1], 1) == 20

def test_tres():
    assert queue_time([4, 5, 2, 3], 4) == 5

def test_cuato():
    assert queue_time([2,2,3,3,4,4], 2) == 9
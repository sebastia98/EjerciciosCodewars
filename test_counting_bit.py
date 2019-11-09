from counting_bit import countBits

def test_uno():
    assert countBits(0) == 0

def test_dos():
    assert countBits(4) == 1

def test_tres():
    assert countBits(7) == 3
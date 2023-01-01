from Lesson5 import division_master


def test_1_is_simple():
    assert division_master.is_simple(1)


def test_2_is_simple():
    assert division_master.is_simple(2)


def test_3_is_simple():
    assert division_master.is_simple(3)


def test_17_is_simple():
    assert division_master.is_simple(17)


def test_40_is_not_simple():
    assert not division_master.is_simple(40)

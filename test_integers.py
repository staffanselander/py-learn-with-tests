import integers


def test_add():
    # Sums two integers.
    assert integers.add(7, 3) == 10

    # Sums two more integers.
    assert integers.add(31, 42) == 73

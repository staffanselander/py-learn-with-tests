from collections import Iterable


def test_for_loop():
    # Python does not seem to support a standard "for loop" syntax like:
    #
    #   for (i = 0; i < x; i++)
    #

    # Instead we need something that is considered Iterable.
    # Which we can create conveniently through range().
    r = range(3)

    # range() returns an instance called "range" which is an Iterable.
    assert isinstance(r, Iterable)
    assert isinstance(r, range)

    # Times the loop has been run.
    loop_count = 0

    # The loop.
    for _ in r:
        loop_count += 1

    # Assert that the loop was run 3 times.
    assert loop_count == 3


def test_while_loop():
    # The while loop looks pretty similar to other languages.
    count = 0

    while count < 3:
        count += 1

    assert count == 3

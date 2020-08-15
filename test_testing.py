

def test_assertions():
    # The keyword "assert" will throw/raise an AssertionError if the following
    # statement returns False.
    try:
        assert "something" == "something-else", "You can also add a more " \
                                                "descriptive message! "
    except AssertionError:
        assert True

    # Since we caught the exception we can assert some more.
    assert "something" == "something"

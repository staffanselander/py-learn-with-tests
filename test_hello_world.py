import hello_world


def test_welcome():
    # Assert the expected value from welcome.
    assert hello_world.welcome("Staffan") == "Welcome Staffan!"

    # Verifying that == is case sensitive.
    assert hello_world.welcome("Staffan") != "Welcome staffan!"

    # Assert another name.
    assert hello_world.welcome("John") == "Welcome John!"


def test_welcome_with_wrong_type():
    # When you call a function with the wrong type.
    # Python will throw/raise a expected/catchable TypeError.
    try:
        hello_world.welcome(0)
    except Exception as err:
        assert isinstance(err, TypeError)

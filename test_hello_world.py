import hello_world


def test_welcome():
    # Assert the expected value from welcome.
    assert hello_world.welcome("Staffan") == "Welcome Staffan!"

    # Verifying that == is case sensitive.
    assert hello_world.welcome("Staffan") != "Welcome staffan!"

    # Assert another name.
    assert hello_world.welcome("John") == "Welcome John!"

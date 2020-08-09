import sys


def test_interpolation():
    name = "Staffan"

    # Interpolate using string concatenation with the "+" operator.
    assert "Hello " + name + "!" == "Hello Staffan!"

    # Interpolate using %s.
    assert "Hello %s!" % name == "Hello Staffan!"

    # Interpolate using Str.format().
    assert 'Hello {}!'.format(name) == "Hello Staffan!"

    # Interpolate using f-strings is possible after Python version 3.5.
    if sys.version_info.major >= 3 and sys.version_info.micro >= 6:
        assert f"Hello {name}!" == "Hello Staffan!"

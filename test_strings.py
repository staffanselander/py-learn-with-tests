import sys


def test_interpolate_using_concatenation():
    name = "Staffan"

    # Interpolate using string concatenation with the "+" operator.
    assert "Hello " + name + "!" == "Hello Staffan!"


def test_interpolate_using_percentage_s():
    name = "Staffan"

    # Interpolate using %s.
    assert "Hello %s!" % name == "Hello Staffan!"


def test_interpolate_using_str_format():
    name = "Staffan"

    # Interpolate using Str.format().
    assert 'Hello {}!'.format(name) == "Hello Staffan!"


def test_interpolate_using_f_strings():
    name = "Staffan"

    # Interpolate using f-strings is possible after Python version 3.5.
    assert f"Hello {name}!" == "Hello Staffan!"

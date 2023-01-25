from unittest.mock import patch
from main import function_a


def test_function_a():
    # note that you must pass the name as it is imported on the application code
    with patch("main.complex_function") as complex_function_mock:

        # we dont care what the return value of the dependency is
        complex_function_mock.return_value = "foo"

        # we just want our function to work
        assert function_a() == "FOO"

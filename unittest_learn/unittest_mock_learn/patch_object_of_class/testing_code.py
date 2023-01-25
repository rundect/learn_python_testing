from unittest.mock import patch
from application_code import MyClass, function_b


def test_function_b():
    # mock an object of class
    with patch.object(MyClass, 'sayhi', return_value="hi i'm a mock object"):
        # the MyClass object used within function_b will
        # be replaced by a mock defined in the
        # patch.object call above
        assert function_b() == "hi i'm a mock object"

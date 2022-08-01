# Tests Parametrization

Test parametrization for `unittest` module inspired from `pytest`.

## Usecase

Ever had a project that does not use `pytest` and can't change that very easy ?
Well now you can use `unittest-param` which is your favorite method for unittest
parametrization.

Just like using `@pytest.mark.parametrize` this decorator ensures you can run
multiple testcases.

# Implementation

On your test case inside the test class inheriting `unittest.TestCase` decorate
the test with `@parametrize` and add your test case data and names.

Example:
```python
from unittest import TestCase
from unittest_param import parametrize

def TestClass(TestCase):

    ...

    @parametrize([
            dict(arg1=1, arg2=2, expected=3),
            dict(arg1=13, arg2=-3, expected=10
        ],[
            "test_adding",
            "test_adding_with_negative"
        ]
    )
    def test_case(self, arg1, arg2, expected):
        assert arg1 + arg2 == expected
```

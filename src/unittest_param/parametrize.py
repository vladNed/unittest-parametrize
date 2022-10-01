import functools
import typing
import unittest

from . import exceptions


def parametrize(
    test_cases: typing.Iterable[typing.Dict[str, typing.Any]],
    test_cases_names: typing.Iterable[str],
):
    """Test parametrization inspired from `pytest`.

    Provide test cases values and test cases names to both parameters and using
    unittest sub test context will run all of them separately.

    :param test_cases: The test cases values given in form of a dict
    :param test_cases_names: The test cases names for each test case data
    """

    def decorator(f: typing.Callable):
        @functools.wraps(f)
        def wrapper(self: unittest.TestCase):
            no_test_cases = len(list(test_cases))
            no_test_cases_names = len(list(test_cases_names))

            if isinstance(test_cases, typing.Iterable) and not no_test_cases > 0:
                raise exceptions.NoValuesProvided

            if no_test_cases_names != no_test_cases:
                raise exceptions.TestCasesNamesInconsistency

            try:
                for (test_name, params) in zip(test_cases_names, test_cases):
                    with self.subTest(test_name, **params):
                        f(self, **params)
            except TypeError as ex:
                raise exceptions.TestCaseHasIncompatibleArgs(str(ex))

        return wrapper

    return decorator

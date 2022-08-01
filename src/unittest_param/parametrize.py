import typing
import functools
import unittest

from . import exceptions


Params = typing.Iterable[typing.Dict[str, typing.Any]]
Keys = typing.Iterable[str]


def parametrize(test_cases: Params, test_cases_names: Keys):
    """Test parametrization inspired from `pytest`.

    Provide test cases values and test cases names to both parameters and using
    unittest sub test context will run all of them separately.

    :param test_cases: The test cases values given in form of a dict
    :param test_cases_names: The test cases names for each test case data
    """

    def decorator(f: typing.Callable):

        @functools.wraps(f)
        def wrapper(self: unittest.TestCase):
            if isinstance(test_cases, typing.Iterable) and not len(test_cases) > 0:
                raise exceptions.NoValuesProvided

            if len(test_cases_names) != len(test_cases):
                raise exceptions.TestCasesNamesInconsistency

            try:
                for (test_name, params) in zip(test_cases_names, test_cases):
                    with self.subTest(test_name, **params):
                        f(self, **params)
            except TypeError as ex:
                raise exceptions.TestCaseHasIncompatibleArgs(str(ex))

        return wrapper
    return decorator

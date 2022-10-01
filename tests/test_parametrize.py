from unittest import TestCase

import pytest

from unittest_param import exceptions, parametrize


def test_run_multiple_test_cases():

    TEST_CASES = dict(
        test_one=dict(arg1=1, arg2=1, expected=2),
        test_two=dict(arg1=12, arg2=2, expected=14),
    )

    class TestMock(TestCase):
        @parametrize(TEST_CASES.values(), TEST_CASES.keys())
        def test_case(self, arg1, arg2, expected):
            assert arg1 + arg2 == expected

    a = TestMock()
    a.test_case()


def test_no_values_provided():

    TEST_CASES = dict()

    class TestMock(TestCase):
        @parametrize(TEST_CASES.values(), TEST_CASES.keys())
        def test_case(self, arg1, arg2, expected):
            assert arg1 + arg2 == expected

    a = TestMock()
    with pytest.raises(exceptions.NoValuesProvided):
        a.test_case()


def test_inconsistent_test_cases_names():

    TEST_CASES = dict(
        test_one=dict(arg1=1, arg2=1, expected=2),
        test_two=dict(arg1=12, arg2=2, expected=14),
    )
    NAMES = ["test_one"]

    class TestMock(TestCase):
        @parametrize(TEST_CASES.values(), NAMES)
        def test_case(self, arg1, arg2, expected):
            assert arg1 + arg2 == expected

    a = TestMock()
    with pytest.raises(exceptions.TestCasesNamesInconsistency):
        a.test_case()


def test_incorrect_arguments_given():

    TEST_CASES = dict(test_one=dict(arg3=2, arg4="str"))

    class TestMock(TestCase):
        @parametrize(TEST_CASES.values(), TEST_CASES.keys())
        def test_case(self, arg1, arg2, expected):
            assert arg1 + arg2 == expected

    a = TestMock()
    with pytest.raises(exceptions.TestCaseHasIncompatibleArgs):
        a.test_case()


def test_cases_as_tuple_not_list():
    TEST_CASES = (dict(arg1=1, arg2=1, expected=2), dict(arg1=12, arg2=2, expected=14))

    TES_CASES_NAMES = ("test_one", "test_two")

    class TestMock(TestCase):
        @parametrize(TEST_CASES, TES_CASES_NAMES)
        def test_case(self, arg1, arg2, expected):
            assert arg1 + arg2 == expected

    a = TestMock()
    a.test_case()

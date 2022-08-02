from typing import Optional


class BaseException(Exception):
    message: str = str()

    def __init__(self, msg: Optional[str] = None):
        if msg:
            self.message = msg
        if not self.message:
            self.message = self.__class__.__name__  # pragma: no cover

    def __str__(self) -> str:
        return self.message  # pragma: no cover


class NoValuesProvided(BaseException):
    message = "No test cases were provided"


class TestCasesNamesInconsistency(BaseException):
    message = "Not enough test cases names for test cases"


class TestCaseHasIncompatibleArgs(BaseException):
    pass

"""
Module that represents assertions
"""
from typing import Any


class Assertions:

    @staticmethod
    def is_equal(actual: Any, expected: Any) -> None:
        """
        Function that will perform assertion for equal operands
        :param actual: actual item that will be known during test run
        :param expected: expected item that will be known beforehand
        :return: None
        """
        assert actual == expected, f"Expected is {expected} but actual is -> {actual}"

import allure
import typing
import unittest

from .. import allure_details

from src.validators import NUMBER_TYPES
from src.value_objects.real import Real


__all__ = [
    "RealTestCase",
]


@allure.suite("RealTest")
class RealTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.errors = (ValueError, TypeError)
        self.number_types = list(typing.get_args(NUMBER_TYPES))
        
        self.positive_numbers = range(1, 50, 5)
        self.negative_numbers = [-value for value in self.positive_numbers]

    @allure.sub_suite("Successful initialization")
    def test_successful_default_initialization(self) -> None:
        for type_ in self.number_types:
            real = Real(type_())
            self.assertIsInstance(real.value, type_)
            self.assertEqual(real.value, 0)
            allure_details(f"Initialized with {type_.__name__}()")
            
    @allure.sub_suite("Successful initialization")
    def test_successful_positive_initialization(self) -> None:
        for type_ in self.number_types:
            for value in self.positive_numbers:
                real = Real(type_(value))
                self.assertIsInstance(real.value, type_)
                self.assertEqual(real.value, value)
                allure_details(f"Initialized with {type_.__name__}({value})")
            
    @allure.sub_suite("Successful initialization")
    def test_successful_negative_initialization(self) -> None:
        for type_ in self.number_types:
            for value in self.negative_numbers:
                real = Real(type_(value))
                self.assertIsInstance(real.value, type_)
                self.assertEqual(real.value, value)
                allure_details(f"Initialized with {type_.__name__}({value})")
            
    @allure.sub_suite("Unsuccessful initialization")
    def test_unsuccessful_initialization(self) -> None:
        other_types = [list, str, dict, tuple]
        for type_ in [list, str, dict, tuple]:
            with self.assertRaises(self.errors) as context:
                Real(type_())
            self.assertIn(type(context.exception), self.errors)
            allure_details(str(context.exception))
            
        for type_ in other_types + self.number_types:
            with self.assertRaises(self.errors) as context:
                Real(type_)
            self.assertIn(type(context.exception), self.errors)
            allure_details(str(context.exception))
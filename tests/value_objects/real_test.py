import math
import allure
import typing
import unittest
import operator

from .. import allure_details, random_shuffle
from src.constants import OPERATORS

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
        self.positive_numbers = list(range(1, 20, 5))
        self.negative_numbers = [-value for value in self.positive_numbers]
        self.float_numbers = [-2.8, -1.5, -0.1, 0.1, 1.5, 2.8]

    @allure.sub_suite("Successful initialization")
    def test_successful_default_initialization(self) -> None:
        for type_ in random_shuffle(self.number_types):
            real = Real(type_())
            self.assertIsInstance(real.value, type_)
            self.assertEqual(real.value, 0)
            allure_details(f"Initialized with Real({type_.__name__}())")
            
    def __initialize_and_test(self, values: typing.List[int]):
        pairs = [(type_, value) for type_ in self.number_types for value in values]
        for type_, value in random_shuffle(pairs):
            real = Real(type_(value))
            self.assertIsInstance(real.value, type_)
            self.assertEqual(real.value, value)
            allure_details(f"Initialized with Real({type_.__name__}({value}))")
    
    @allure.sub_suite("Successful initialization")
    def test_successful_positive_initialization(self) -> None:
        self.__initialize_and_test(self.positive_numbers)
            
    @allure.sub_suite("Successful initialization")
    def test_successful_negative_initialization(self) -> None:
        self.__initialize_and_test(self.negative_numbers)
            
    @allure.sub_suite("Unsuccessful initialization")
    def test_unsuccessful_initialization(self) -> None:
        other_types = [list, str, dict, tuple]
        for type_ in random_shuffle(other_types):
            with self.assertRaises(self.errors) as context:
                Real(type_())
            self.assertIn(type(context.exception), self.errors)
            allure_details(str(context.exception))
        
        for type_ in random_shuffle(other_types + self.number_types):
            with self.assertRaises(self.errors) as context:
                Real(type_)
            self.assertIn(type(context.exception), self.errors)
            allure_details(str(context.exception))
            
    @allure.sub_suite("__pos__")
    def test_pos(self) -> None:
        values = self.positive_numbers + [0] + self.negative_numbers
        pairs = [(type_, value) for type_ in self.number_types for value in values]
        for type_, value in random_shuffle(pairs):
            real = Real(type_(value))
            self.assertEqual(+real, real)
            allure_details(f"""Real positive operation (__pos__ or +Real(value)) on +({real}) resulted in {+real}""")
                
    @allure.sub_suite("__neg__")
    def test_neg(self) -> None:
        values = self.positive_numbers + [0] + self.negative_numbers
        pairs = [(type_, value) for type_ in self.number_types for value in values]
        for type_, value in random_shuffle(pairs):
            real = Real(type_(value))
            neg_real = -real
            self.assertIsInstance(neg_real, Real)
            self.assertEqual(neg_real.value, -real.value)
            allure_details(f"""Real negation operation (__neg__ or -Real(value)) on -({real}) resulted in {-real}""")
            
    @allure.sub_suite("__abs__")
    def test_abs(self) -> None:
        values = self.positive_numbers + [0] + self.negative_numbers
        pairs = [(type_, value) for type_ in self.number_types for value in values]
        for type_, value in random_shuffle(pairs):
            real = Real(type_(value))
            abs_real = abs(real)
            self.assertIsInstance(abs_real, Real)
            self.assertEqual(abs_real.value, abs(real.value))
            allure_details(f"""Real absolute operation (__abs__ or abs(Real(value))) on abs({real}) resulted in {abs(real)}""")
            
    @allure.sub_suite("__invert__")
    def test_invert(self) -> None:
        values = self.positive_numbers + [0] + self.negative_numbers
        pairs = [(type_, value) for type_ in self.number_types for value in values]
        for type_, value in pairs:
            real = Real(type_(value))
            with self.assertRaises(self.errors) as context:
                ~real
            self.assertIn(type(context.exception), self.errors)
            allure_details(str(context.exception))
            
    def __math_operations(self, operation: typing.Callable, text: str) -> None:
        for value in random_shuffle(self.float_numbers):
            real = Real(value)
            new_real: Real = operation(real)
            self.assertIsInstance(new_real, Real)
            self.assertEqual(new_real.value, operation(real).value)
            allure_details(f"""Real {text} operation (__{text}__ or math.{text}(Real(value))) on math.{text}({real}) resulted in {operation(real)}""")
            
    @allure.sub_suite("__floor__")
    def test_floor(self) -> None:
        self.__math_operations(math.floor, "floor")
            
    @allure.sub_suite("__ceil__")
    def test_ceil(self) -> None:
        self.__math_operations(math.ceil, "ceil")
            
    @allure.sub_suite("__trunc__")
    def test_trunc(self) -> None:
        self.__math_operations(math.trunc, "trunc")
        
    def __conversion(self, type_: typing.Type) -> None:
        values = [0] + self.float_numbers + self.positive_numbers + self.negative_numbers
        for value in random_shuffle(values):
            real = Real(value)
            new_value = type_(real)
            self.assertIsInstance(new_value, type_)
            self.assertEqual(new_value, type_(real))
            allure_details(f"""Real {type_.__name__} conversion of Real({value}) resulted in {new_value}""")
        
    @allure.sub_suite("Conversation to int")
    def test_int(self) -> None:
        self.__conversion(int)
        
    @allure.sub_suite("Conversion to float")
    def test_float(self) -> None:
        self.__conversion(float)
        
    @allure.sub_suite("Conversion to bool")
    def test_bool(self) -> None:
        self.__conversion(bool)
        
    @allure.sub_suite("__round__")
    def test_round(self) -> None:
        values = [0] + self.float_numbers + self.positive_numbers + self.negative_numbers
        for value in random_shuffle(values):
            for n in range(-2, 3):
                real = Real(value)
                round_real = round(real, n)
                self.assertIsInstance(round_real, Real)
                self.assertEqual(round_real, round(value, n))
                allure_details(f"""Real round operation (__round__ or round(Real(value), {n})) on round({real}, {n}) resulted in {round(real, n)}""")
       
    def __operation(self, operation: typing.Callable, operation_name: str, text: str) -> None:
        values = self.positive_numbers + self.negative_numbers
        for value in random_shuffle(values):
            real = Real(value)
            for other in random_shuffle(values):
                other_real = Real(other)
                self.assertEqual(operation(real, other_real), operation(value, other))
                self.assertEqual(operation(real, other), operation(value, other))
                allure_details(f"Real {text} Real({value}) {operation_name} Real({other}) resulted in {operation(real, other_real)}")
            
    def __comparison(self, operation: typing.Callable, operation_name: str) -> None:
        self.__operation(operation, operation_name, "comparison")
        
    def __math(self, operation: typing.Callable, operation_name: str) -> None:
        self.__operation(operation, operation_name, "math operation")
                
    @allure.sub_suite("__eq__")
    def test_eq(self) -> None:
        self.__comparison(operator.eq, OPERATORS[operator.eq])
    
    @allure.sub_suite("__ne__")
    def test_eq(self) -> None:
        self.__comparison(operator.ne, OPERATORS[operator.ne])
        
    @allure.sub_suite("__lt__")
    def test_eq(self) -> None:
        self.__comparison(operator.lt, OPERATORS[operator.lt])
        
    @allure.sub_suite("__le__")
    def test_eq(self) -> None:
        self.__comparison(operator.le, OPERATORS[operator.le])
        
    @allure.sub_suite("__gt__")
    def test_eq(self) -> None:
        self.__comparison(operator.gt, OPERATORS[operator.gt])
        
    @allure.sub_suite("__ge__")
    def test_eq(self) -> None:
        self.__comparison(operator.ge, OPERATORS[operator.ge])
        
    @allure.sub_suite("__add__")
    def test_add(self) -> None:
        self.__math(operator.add, OPERATORS[operator.add])
    
    @allure.sub_suite("__radd__")
    def test_radd(self) -> None:
        self.__math(operator.add, OPERATORS[operator.add])
        
    @allure.sub_suite("__sub__")
    def test_sub(self) -> None:
        self.__math(operator.sub, OPERATORS[operator.sub])
    
    @allure.sub_suite("__rsub__")
    def test_rsub(self) -> None:
        self.__math(operator.sub, OPERATORS[operator.sub])
        
    @allure.sub_suite("__mul__")
    def test_mul(self) -> None:
        self.__math(operator.mul, OPERATORS[operator.mul])
    
    @allure.sub_suite("__rmul__")
    def test_rmul(self) -> None:
        self.__math(operator.mul, OPERATORS[operator.mul])
        
    @allure.sub_suite("__pow__")
    def test_pow(self) -> None:
        self.__math(operator.pow, OPERATORS[operator.pow])
    
    @allure.sub_suite("__rpow__")
    def test_rpow(self) -> None:
        self.__math(operator.pow, OPERATORS[operator.pow])
        
    @allure.sub_suite("__truediv__")
    def test_truediv(self) -> None:
        self.__math(operator.truediv, OPERATORS[operator.truediv])
    
    @allure.sub_suite("__rtruediv__")
    def test_rtruediv(self) -> None:
        self.__math(operator.truediv, OPERATORS[operator.truediv])
        
    @allure.sub_suite("__floordiv__")
    def test_floordiv(self) -> None:
        self.__math(operator.floordiv, OPERATORS[operator.floordiv])
    
    @allure.sub_suite("__rfloordiv__")
    def test_rfloordiv(self) -> None:
        self.__math(operator.floordiv, OPERATORS[operator.floordiv])
        
    @allure.sub_suite("__mod__")
    def test_mod(self) -> None:
        self.__math(operator.mod, OPERATORS[operator.mod])
    
    @allure.sub_suite("__rmod__")
    def test_rmod(self) -> None:
        self.__math(operator.mod, OPERATORS[operator.mod])
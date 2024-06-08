import pytest
import decimal
import fractions

from .fixture import RealFixture

from src.value_objects.real import Real


__all__ = [
    "TestReal",
]


real_fixture = RealFixture()

real_default = real_fixture.real_default


class TestReal:
    
    def test_real_initialization(self, real_default: Real):
        assert isinstance(
            real_default.value,
            (int, float, fractions.Fraction, decimal.Decimal)
        )
        assert real_default.value == 0
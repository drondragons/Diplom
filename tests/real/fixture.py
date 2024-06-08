import pytest
import random
import typing
from src.validators import NUMBER_TYPES
from src.value_objects.real import Real


__all__ = [
    "RealFixture",
]


class RealFixture:
    
    TYPES = typing.get_args(NUMBER_TYPES)
    
    @pytest.fixture(params=TYPES)
    def real_default(self, request: pytest.FixtureRequest) -> Real:
        return Real(request.param())
    
    # @pytest.fixture
    # def real_positive(self):
    #     return Real(10)
    
    # @pytest.fixture
    # def real_negative(self):
    #     return Real(-10)
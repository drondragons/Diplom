import operator
from typing import Iterator

from ... import _error, _validate, _operate, _type_error, _validation_operation
from ...validators import StringValidator


__all__ = [
    "Title",
]


class Title:
    
    __slots__ = [
        "_value",
    ]
    
    DEFAULT_TITLE = "Название"
    
    @property
    def class_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def value(self) -> str:
        return self._value
    
    @value.setter
    def value(self, value: str) -> None:
        s = f"\n\t{self.class_name}: "
        StringValidator._handle_exception(StringValidator.validate, s, value)
        self._value = value
    
    def __init__(self, value: str = DEFAULT_TITLE) -> None:
        self.value = value.value if isinstance(value, Title) else value
        
    # ------------------- Output ---------------------------
        
    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return f"{self.class_name} (value: {self.value})"
    
    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.class_name, self.value))
    
    # ------------------- Validation ---------------------------
    
    @staticmethod
    def _validate(right: object, left: object, operator: operator) -> None:
        _validate(right, str | Title, left, str | Title, operator)
    
    # ------------------- Operate ---------------------------
    
    @staticmethod
    def _operate(right: object, left: object, operator: operator) -> object:
        return _operate(right, str, left, Title, operator)
    
    # ------------------- Comparison operators ---------------------------
    
    @staticmethod
    def __compare(right: object, left: object, operator: operator) -> bool:
        return _validation_operation(right, left, operator, Title)
    
    def __eq__(self, other: object) -> bool:
        return Title.__compare(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return Title.__compare(self, other, operator.ne)
    
    def __lt__(self, other: object) -> bool:
        return Title.__compare(self, other, operator.lt)
    def __le__(self, other: object) -> bool:
        return Title.__compare(self, other, operator.le)
    
    def __gt__(self, other: object) -> bool:
        return Title.__compare(self, other, operator.gt)
    def __ge__(self, other: object) -> bool:
        return Title.__compare(self, other, operator.ge)
    
    def __bool__(self) -> bool:
        return len(self) != 0
    
    # ------------------- Mathematical operators ---------------------------
    
    @staticmethod
    def __math(right: object, left: object, operator: operator) -> "Title":
        return Title(_validation_operation(right, left, operator, Title))
    
    def __add__(self, other: object) -> "Title":
        return Title.__math(self, other, operator.add)
    def __radd__(self, other: object) -> "Title":
        return Title.__math(other, self, operator.add)
    def __iadd__(self, other: object) -> "Title":
        return Title.__math(self, other, operator.iadd)
    
    def __mul__(self, other: object) -> "Title":
        message = f"\n\t{self.class_name}: "
        if not isinstance(other, int):
            raise TypeError(message + _type_error(self, other, operator.mul))
        return self.value * other
    def __rmul__(self, other: object) -> "Title":
        message = f"\n\t{self.class_name}: "
        if not isinstance(other, int):
            raise TypeError(message + _type_error(other, self, operator.mul))
        return self * other
    def __imul__(self, other: object) -> "Title":
        message = f"\n\t{self.class_name}: "
        if not isinstance(other, int):
            raise TypeError(message + _type_error(self, other, operator.imul))
        return self * other
    
    # ------------------- String operators ---------------------------
    
    def capitalize(self) -> "Title":
        return Title(self.value.capitalize())
    def casefold(self) -> "Title":
        return Title(self.value.casefold())
    
    def center(self, width: int, fillchar: str = " ") -> "Title":
        message = f"\n\t{self.class_name}.center: "
        if not isinstance(width, int):
            message += f"Ширина должна быть типа int, а не {type(width).__name__}!"
            raise TypeError(message)
        if not isinstance(fillchar, str):
            message += f"Заполняющий элемент должен быть типа str, "
            message += f"а не {type(fillchar).__name__}!"
            raise TypeError(message)
        if len(fillchar) != 1:
            message += f"Длина заполняющего элемента должна быть 1, а не {len(fillchar)}!"
            raise ValueError(message)
        return Title(self.value.center(width, fillchar))
    
    def isalnum(self) -> bool:
        return self.value.isalnum()
    def isalpha(self) -> bool:
        return self.value.isalpha()
    def isascii(self) -> bool:
        return self.value.isascii()
    def isdecimal(self) -> bool:
        return self.value.isdecimal()
    def isdigit(self) -> bool:
        return self.value.isdigit()
    def isidentifier(self) -> bool:
        return self.value.isidentifier()
    def islower(self) -> bool:
        return self.value.islower()
    def isnumeric(self) -> bool:
        return self.value.isnumeric()
    def isprintable(self) -> bool:
        return self.value.isprintable()
    def isspace(self) -> bool:
        return self.value.isspace()
    def istitle(self) -> bool:
        return self.value.istitle()
    def isupper(self) -> bool:
        return self.value.isupper()
    
    # ------------------- List operators ---------------------------
    
    def __iter__(self) -> Iterator:
        return iter(self.value)
    
    def __len__(self) -> int:
        return len(self.value)
    
    def __contains__(self, item: object) -> bool:
        Title.__validate(self, item, operator.contains)
        return item in self.value
    
    def __getitem__(self, index: int | slice) -> str:
        message = f"\n\t{self.class_name}: "
        if not isinstance(index, int | slice):
            message += f"Операция {self.class_name}[{type(index).__name__}] недоступна!"
            raise TypeError(message)
        return self.value[index]
    
    def __setitem__(self, index: int, value: str) -> None:
        message = f"\n\t{self.class_name}: "
        if not isinstance(index, int):
            message += f"Операция {self.class_name}[{type(index).__name__}] недоступна!"
            raise TypeError(message)
        if not isinstance(value, str):
            message += f"Операция {self.class_name}[{type(index).__name__}] "
            message += f"= {type(value).__name__} недоступна!"
            raise TypeError(message)
        self.value = self.value[:index] + value + self.value[index + 1:]
    
    # ------------------- Other magic methods ---------------------------
    
    def __format__(self, format_spec: str = str(), /) -> str:
        return self.__str__()
    
    def __index__(self) -> "Title":
        message = f"Операция индексирования (Iterable[{self.class_name}]) недоступна!"
        raise TypeError(_error(self, message))
    
    def __getattribute__(self, name: str) -> None:
        try:
            return super().__getattribute__(name)
        except AttributeError:
            pass
        message = f"Класс '{self.class_name}' не содержит атрибут {name}!"
        raise AttributeError(_error(self, message))
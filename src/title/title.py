import operator
from typing import Iterator

from ..constants import OPERATORS
from ..validators import StringValidator


__all__ = [
    "Title",
]


class Title:
    
    __slots__ = [
        "__value",
    ]
    
    DEFAULT_TITLE = "Название"
    
    @property
    def class_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def value(self) -> str:
        return self.__value
    
    @value.setter
    def value(self, value: str) -> None:
        s = f"\n\t{self.class_name}: "
        StringValidator._handle_exception(StringValidator.validate, s, value)
        self.__value = value
    
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
    
    # ------------------- Error validation ---------------------------
    
    @staticmethod
    def __error(obj: object, message: str = str()) -> str:
        return f"\n\t{type(obj).__name__}: {message}"
    
    @staticmethod
    def __type_error(right: object, left: object, operator: operator) -> str:
        left_name = f"'{type(left).__name__}'"
        right_name = f"'{type(right).__name__}'"
        return f"Операция {right_name} {OPERATORS[operator]} {left_name} недоступна!"
    
    @staticmethod
    def __validate(right: object, left: object, operator: operator) -> None:
        message = Title.__type_error(right, left, operator)
        if not isinstance(right, str | Title):
            raise TypeError(Title.__error(left, message))
        if not isinstance(left, str | Title):
            raise TypeError(Title.__error(right, message))
    
    # ------------------- Operate ---------------------------
    
    @staticmethod
    def __operate(right: object, left: object, operator: operator) -> object:
        if isinstance(right, str) and isinstance(left, Title):
            return operator(right, left.value)
        if isinstance(right, Title) and isinstance(left, str):
            return operator(right.value, left)
        return operator(right.value, left.value)
    
    # ------------------- Comparison operators ---------------------------
    
    @staticmethod
    def __compare(right: object, left: object, operator: operator) -> bool:
        Title.__validate(right, left, operator)
        return Title.__operate(right, left, operator)
    
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
        Title.__validate(right, left, operator)
        return Title(Title.__operate(right, left, operator))
    
    def __add__(self, other: object) -> "Title":
        return Title.__math(self, other, operator.add)
    def __radd__(self, other: object) -> "Title":
        return Title.__math(other, self, operator.add)
    def __iadd__(self, other: object) -> "Title":
        return Title.__math(self, other, operator.iadd)
    
    def __mul__(self, other: object) -> "Title":
        if not isinstance(other, int):
            raise TypeError(f"\n\t{self.class_name}: {self.__type_error(self, other, operator.mul)}")
        return self.value * other
    def __rmul__(self, other: object) -> "Title":
        if not isinstance(other, int):
            raise TypeError(f"\n\t{self.class_name}: {self.__type_error(other, self, operator.mul)}")
        return self * other
    def __imul__(self, other: object) -> "Title":
        if not isinstance(other, int):
            raise TypeError(f"\n\t{self.class_name}: {self.__type_error(self, other, operator.imul)}")
        return self * other
    
    # ------------------- String operators ---------------------------
    
    def capitalize(self) -> "Title":
        return Title(self.value.capitalize())
    def casefold(self) -> "Title":
        return Title(self.value.casefold())
    
    def center(self, width: int, fillchar: str = " ") -> "Title":
        if not isinstance(width, int):
            raise TypeError(f"\n\t{self.class_name}.center: Ширина должна быть типа int, а не {type(width).__name__}!")
        if not isinstance(fillchar, str):
            raise TypeError(f"\n\t{self.class_name}.center: Заполняющий элемент должен быть типа str, а не {type(fillchar).__name__}!")
        if len(fillchar) != 1:
            raise ValueError(f"\n\t{self.class_name}.center: Длина заполняющего элемента должна быть 1, а не {len(fillchar)}!")
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
        if not isinstance(index, int | slice):
            raise TypeError(f"\n\t{self.class_name}: Операция {self.class_name}[{type(index).__name__}] недоступна!")
        return self.value[index]
    
    def __setitem__(self, index: int, value: str) -> None:
        if not isinstance(index, int):
            raise TypeError(f"\n\t{self.class_name}: Операция {self.class_name}[{type(index).__name__}] недоступна!")
        if not isinstance(value, str):
            raise TypeError(f"\n\t{self.class_name}: Операция {self.class_name}[{type(index).__name__}] = {type(value).__name__} недоступна!")
        self.value = self.value[:index] + value + self.value[index + 1:]
    
    # ------------------- Other magic methods ---------------------------
    
    def __format__(self, format_spec: str = str(), /) -> str:
        return self.__str__()
    
    def __index__(self) -> "Title":
        message = f"Операция индексирования (Iterable[{self.class_name}]) недоступна!"
        raise TypeError(Title.__error(self, message))
    
    def __getattribute__(self, name: str) -> None:
        try:
            return super().__getattribute__(name)
        except AttributeError:
            pass
        message = f"Класс '{self.class_name}' не содержит атрибут {name}!"
        raise AttributeError(Title.__error(self, message))
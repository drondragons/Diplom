import pandas
from typing import Dict

from .money import Money
from .money_validator import MoneyValidator

from ..converter import Converter


__all__ = [
    "MoneyConverter",
]


class MoneyConverter(Converter):
    
    CBR_URL = "http://www.cbr.ru/scripts/XML_daily.asp"
    
    @classmethod
    def get_daily_currency_values(cls) -> Dict[str, float]:
        money_types = [subclass for subclass in Money.__subclasses__()]
        international_forms = [money_type.INTERNATIONAL_FORM for money_type in money_types]
        
        df = pandas.read_xml(cls.CBR_URL, encoding="cp1251")
        currencies = df[df["CharCode"].isin(international_forms)]
        
        result = dict.fromkeys(international_forms)
        for form in international_forms:
            values = currencies.loc[currencies['CharCode'] == form, 'Value'].values
            result[form] = 1
            if values:
                result[form] = float(values[0].replace(",", "."))
        result.setdefault(Money.INTERNATIONAL_FORM, 1)
        return result
    
    @classmethod
    def convert(cls, input: Money, output: type = Money) -> Money:
        exception, message = MoneyValidator.validate_type(input, Money)
        if exception:
            raise exception(f"\n\t{cls.__name__}.convert: " + message)
        if not issubclass(output, Money):
            message = f"Недопустимый тип '{output.__name__}'! Ожидался тип {MoneyValidator.format_union_types(output)}!"
            raise TypeError(f"\n\t{cls.__name__}.convert: " + message)
        
        daily_currency = cls.get_daily_currency_values()
        # print(daily_currency)
        first = daily_currency[input.INTERNATIONAL_FORM]
        second = daily_currency[output.INTERNATIONAL_FORM]
        # print(first, second)
        # print(input.value * first / second)
        return output(input.value * first / second)
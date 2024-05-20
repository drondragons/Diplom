import os
import pandas
from typing import Dict
from datetime import date

from .money import Money
from .money_validator import MoneyValidator

from ..converter import Converter


__all__ = [
    "MoneyConverter",
]


class MoneyConverter(Converter):
    
    CBR_URL = "http://www.cbr.ru/scripts/XML_daily.asp"
    # ?date_req=21/05/2024
    PROJECT_DIR = os.getcwd()
    CURRENT_DIR = os.path.join(PROJECT_DIR, "src", "measurement", "money")
    FILE_PATH = os.path.join(CURRENT_DIR, "currency.xml")
    
    @classmethod
    def _get_currency(cls) -> pandas.DataFrame:
        url = f"{cls.CBR_URL}?date_req={date.today().strftime('%d/%m/%Y')}"
        return pandas.read_xml(url, encoding="cp1251")
    
    @classmethod
    def _save_currency(cls, df: pandas.DataFrame) -> None:
        df.to_xml(cls.FILE_PATH, encoding="utf-8", index=False)
        
    @classmethod
    def _load_currency(cls) -> pandas.DataFrame:
        return pandas.read_xml(cls.FILE_PATH, encoding="utf-8")
    
    @classmethod
    def _get_daily_currency_values(cls) -> Dict[str, float]:
        money_types = [subclass for subclass in Money.__subclasses__()]
        international_forms = [money_type.INTERNATIONAL_FORM for money_type in money_types]
        
        df = None
        path_exists = os.path.exists(cls.FILE_PATH)
        if not path_exists or (path_exists and \
            date.fromtimestamp(os.path.getmtime(cls.FILE_PATH)) != date.today()):
            df = cls._get_currency()
            cls._save_currency(df)
            # print("______________________________________________")
            # print(df)
            # print("______________________________________________")
        else:
            df = cls._load_currency()
        # df = pandas.read_xml(cls.CBR_URL, encoding="cp1251")
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
        exception, message = MoneyValidator.validate_object_type(input, Money)
        if exception:
            raise exception(f"\n\t{cls.__name__}.convert: " + message)
        if not issubclass(output, Money):
            message = f"Недопустимый тип '{output.__name__}'! Ожидался тип {MoneyValidator.format_union_types(output)}!"
            raise TypeError(f"\n\t{cls.__name__}.convert: " + message)
        
        daily_currency = cls._get_daily_currency_values()

        first = daily_currency[input.INTERNATIONAL_FORM]
        second = daily_currency[output.INTERNATIONAL_FORM]

        return output(input.value * first / second)
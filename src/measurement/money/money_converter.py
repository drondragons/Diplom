import os
import pandas
from typing import Dict, Type, List
from datetime import date

from .money import Money

from .. import _convert
from ..converter import Converter

from ...validators import Validator


__all__ = [
    "MoneyConverter",
]


class MoneyConverter(Converter):
    
    CBR_URL = "http://www.cbr.ru/scripts/XML_daily.asp" # ?date_req=21/05/2024
    PROJECT_DIR = os.getcwd()
    CURRENT_DIR = os.path.join(PROJECT_DIR, "src", "measurement", "money")
    FILE_PATH = os.path.join(CURRENT_DIR, "currency.xml")
    
    @classmethod
    def get_money_types(cls) -> List[Type]:
        return [subclass for subclass in Money.__subclasses__()]
    
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
        else:
            df = cls._load_currency()
            
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
    def _convert(cls, input: Money, output: Type = Money) -> Money:
        daily_currency = cls._get_daily_currency_values()
        first = daily_currency[input.INTERNATIONAL_FORM]
        second = daily_currency[output.INTERNATIONAL_FORM]
        return output(input.value) \
            if type(input) == Money or type(output) == Money else \
                output(_convert(input.value, first, second))
    
    @classmethod
    def convert(cls, input: Money, output: Type = Money) -> Money:
        s = f"\n\t{cls.__name__}.convert: "
        money_types = cls.get_money_types() + [Money]
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, input, money_types)
        handler(Validator.validate_type_of_type, s, output, money_types)
        
        return cls._convert(input, output)
    
    @classmethod
    def _increase_money_type(cls, value: Money) -> Money:
        return cls._increase_type(value, cls.get_money_types())
        
    @classmethod
    def _decrease_money_type(cls, value: Money) -> Money:
        return cls._decrease_type(value, cls.get_money_types())
    
    @classmethod
    def _auto_convertation(cls, value: Money) -> Money:
        return cls._auto_convert(
            value,
            Money,
            cls._decrease_money_type,
            cls._increase_money_type
        )
    
    @classmethod
    def auto_convert(cls, value: Money) -> Money:
        s = f"\n\t{cls.__name__}.auto_convert: "
        money_types = cls.get_money_types() + [Money]
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, value, money_types)
        
        return cls._auto_convertation(value)
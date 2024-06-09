import random
import allure
import typing

def allure_details(text: str) -> None:
    allure.attach(text, name="Details", attachment_type=allure.attachment_type.TEXT)
    
def random_shuffle(list_: typing.List) -> typing.List:
    random.shuffle(list_)
    return list_
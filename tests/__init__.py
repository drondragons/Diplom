import allure

def allure_details(text: str) -> None:
    allure.attach(text, name="Details", attachment_type=allure.attachment_type.TEXT)
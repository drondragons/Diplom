from datetime import datetime
from setuptools import setup


FULLNAME = "Trunov Andrew"
CURRENT_YEAR = datetime.now().year


with open("README.md", "r") as file:
    readme = file.read()


with open("LICENSE", "r") as file:
    license = file.read()
    license = license.replace("[year]", str(CURRENT_YEAR))
    license = license.replace("[fullname]", FULLNAME)


setup(
    name="Diploma work",
    author="Трунов Андрей ИУ7 МГТУ им. Баумана",
    author_email="trunov2014@list.ru",
    version="0.1.0",
    # use_scm_version=True,
    # setup_requires=["setuptools_scm"],
    # packages=find_packages(),
    readme=readme,
    license=license,
)
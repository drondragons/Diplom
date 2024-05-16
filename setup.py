from datetime import datetime
from setuptools import setup
import setuptools


FULLNAME = "Trunov Andrew"

PROJECT_YEAR = 2024
CURRENT_YEAR = datetime.now().year
LICENSE_YEAR = f"{PROJECT_YEAR}-{CURRENT_YEAR}"

LICENSE_TEXT = """MIT License

Copyright (c) {year}, {fullname}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


with open("README.md", "r") as file:
    readme = file.read()

with open("LICENSE", "w") as file:
    license = LICENSE_TEXT.format(
        year=LICENSE_YEAR, 
        fullname=FULLNAME
    )
    file.write(license)
    

setup(
    name="Diploma work",
    author="Трунов Андрей ИУ7 МГТУ им. Баумана",
    author_email="trunov2014@list.ru",
    version="0.1.0",
    description="Дипломная работа",
    url="https://github.com/drondragons/Diplom",
    long_description=readme,
    license=license,
)
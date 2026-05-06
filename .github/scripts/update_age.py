from datetime import date
from os import environ
from pathlib import Path
import re

birthday = date.fromisoformat(environ["BIRTHDAY"])
today = date.today()

age = today.year - birthday.year
if (today.month, today.day) < (birthday.month, birthday.day):
    age -= 1

readme = Path("README.md")
text = readme.read_text(encoding="utf-8")

text = re.sub(
    r"<!-- age:start -->\d+<!-- age:end -->",
    f"<!-- age:start -->{age}<!-- age:end -->",
    text,
)

readme.write_text(text, encoding="utf-8")

import re


text = "This picture is an oil on canvas painting by 1Danish artist2 Anna Petersen between 1845 and 1910 year"

print(re.findall(r"\b\d+\b", text))

print()
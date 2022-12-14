import re
from requests import get
k = input("(LINK:>")
b = get(k).text
email = re.findall("\S+@\S+",b)
for x in email:
    print(x)

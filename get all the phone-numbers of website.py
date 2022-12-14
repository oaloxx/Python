import re
from selenium import webdriver
fd = input("LINK>")
dri = webdriver.Chrome(r"C:\SCHEISSEL\chromedriver.exe")
dri.get(fd)
go = dri.page_source
phone = re.findall(r"[\d]{3}[\d]{3}[\d]{4}",go)
for i in phone:
    print(i)



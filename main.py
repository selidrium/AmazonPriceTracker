import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

MY_EMAIL = ""
PASSWORD = ""

# visit http://myhttpheader.com/ to find header params

r = requests.get("https://www.amazon.com/Apple-MacBook-16-inch-10%E2%80%91core-16%E2%80%91core/dp/B09JQKBQSB/ref"
                 "=sr_1_3?keywords=macbook%2Bpro&qid=1671591525&sr=8-3&th=1",
                 headers={
                     "User-Agent": "",
                     "Accept-Language": ""})

soup = BeautifulSoup(r.text, "lxml")
total_price = soup.find(name="span", class_="a-price").text.split("$")[1]
target_price = 2200.00
total_price = float(total_price.replace(',', ''))

if total_price < target_price:
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="",
            msg=f"Subject:Price Alert on Mac!\n\nThe price has hit")

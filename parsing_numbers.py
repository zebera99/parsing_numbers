import requests
from bs4 import BeautifulSoup


page = requests.get('https://workey.codeit.kr/orangebottle/index')
soup = BeautifulSoup(page.text, 'html.parser')

number = soup.select('.phoneNum')

phone_numbers = []

for num in number:
    phone_numbers.append(num.text)

print(phone_numbers)

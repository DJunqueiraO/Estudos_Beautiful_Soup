from bs4 import BeautifulSoup

from scripts.page import Page

adviceslip = Page('https://api.adviceslip.com/', 'home.html')


soup = BeautifulSoup(adviceslip, 'lxml')

link_tags = soup.find_all('a')

messages = soup.find_all('div', class_='msg')

for message in messages:
    print(message)
    print(message.p)
    print(message.p.text)
    print(message.p.text.split()[-1])


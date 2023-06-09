from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sqlite3 as sq
from datetime import datetime

driver = webdriver.Chrome()
driver.get("https://cs2plg.com/ru/crash")

conn = sq.connect('csgopoly.db')
cur = conn.cursor()

last_item = 0
values =[]


while True:
    deposit = 0
    profit = 0
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    crash_info = soup.find('div', {'class': 'crash-info'})
    bet_info = soup.find_all('span', {'class': 'crash_amount_span'})
    win_info = soup.find_all('span', {'class': 'profit win'})
    lose_info = soup.find_all('span', {'class': 'profit lose'})

    if "CRASHED" in crash_info.text:
        item_list = soup.find_all('ul', class_='crash-history')
        now_item = item_list[0].li.span.text

        if(last_item != now_item):
            values.append(now_item)

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            for item in bet_info:
                value = item.find('span').text
                deposit += int(value)

            for item in win_info:
                value = item.text
                profit += int(str(value)[1:])

            for item in lose_info:
                value = item.text
                profit -= int(str(value)[1:])

            cur.execute("INSERT INTO casino_hack (coeff, time, deposit, profit) VALUES (?,?,?,?);", (now_item, current_time, deposit, profit))
            conn.commit()


        last_item = item_list[0].li.span.text
        time.sleep(1)




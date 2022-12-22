import requests
import bs4
import time
import datetime
import smtplib
import os


def priceTracker():
    global num
    url = 'https://crypto.com/price/binance-coin'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    price = soup.find_all('div', {'class': 'css-1b2cb7e'})[0].find('span').text
    price = re.findall("\d+\.\d+", price)
    for num in price:
        return num

print('Crawling every 60 seconds..')

while True:
    priceTracker()
    time.sleep(60)
    if float(num) < 605.00:
        print(f'LOWER THAN 605: {num}')
        
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_object.starttls()
        
        email = os.environ.get('EMAIL_USER')
        password = os.environ.get('EMAIL_PASS')
        smtp_object.login(email, password)
        
        from_address = email
        to_address = email
        subject = 'BNB Price Test'
        message = f"BNB is on sale! BNB < $605.00 at ${price}" + "\nNow is a good time to buy!" "\n\nhttps://crypto.com/price/binance-coin"
        msg = 'Subject: ' +subject+'\n\n'+message

        smtp_object.sendmail(from_address, to_address, msg)

    if float(num) > 620.00:
        print(f'HIGHER THAN 620: {num}')
        
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_object.starttls()
        
        email = os.environ.get('EMAIL_USER')
        password = os.environ.get('EMAIL_PASS')
        smtp_object.login(email, password)
        
        from_address = email
        to_address = email
        subject = 'BNB Price Test'
        message = f"BNB is going up.. BNB < $620 at ${price}" + "\nBuy soon.." "\n\nhttps://crypto.com/price/binance-coin"
        msg = 'Subject: ' +subject+'\n\n'+message

        smtp_object.sendmail(from_address, to_address, msg)

    else:
        print(f'BNB currently at - ${num}')
        print('As of - ', datetime.datetime.now())

# price tracker of a product in amazon

import requests
from bs4 import BeautifulSoup
import smtplib
import time

#URL = 'https://www.amazon.in/Sony-24-3MP-Digital-28-70mm-ILCE-7M2K/dp/B00UBMZM0K/ref=sr_1_1?crid=2JIJ0QCD423W&keywords=sony+alpha+ilce-7m2k&qid=1570859330&sprefix=sony+alpha+ILCE-7%2Caps%2C279&sr=8-1'
URL = 'https://www.amazon.in/Sony-24-3MP-Digital-28-70mm-ILCE-7M2K/dp/B00UBMZM0K/ref=sr_1_1?crid=2JIJ0QCD423W&keywords=sony+alpha+ilce-7m2k&qid=1570859330&sprefix=sony+alpha+ILCE-7%2Caps%2C279&sr=8-1'
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

def check_price():
    page = requests.get(URL , headers=headers)

    soup1 = BeautifulSoup(page.content , 'lxml')
    #soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup1.find(id= "productTitle").get_text()
    price = soup1.find(id='priceblock_ourprice').get_text().strip().replace(',' , '')[2:8]
    converted_price = float(price)
    #price[2:3] + price[4:6] + price[7:10]

    print(title.strip())
    send_email() 
    if(converted_price < 122):
        print(converted_price)

def send_email():
    server = smtplib.SMTP('smtp.gmail.com' , 587) 
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('vardhan.harsh94@gmail.com' , 'hgwnmauzjsqifsic')
    subject = "Price fell dowm\n ."
    body = "Buy the camera"

    msg = f'Subject : {subject} \n\n {body}'
    server.sendmail(
        'vardhan.harsh94@gmail.com',
        'vardhan.harsh123@protonmail.com',
        msg
    )
    print('Email sent')
    server.quit()

while(True):
    check_price()
    time.sleep(60*60*24)
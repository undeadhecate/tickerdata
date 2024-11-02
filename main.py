from typing import Union
from selenium import webdriver
import lxml.etree
from lxml import html
from fastapi import FastAPI
import requests
from lxml.cssselect import CSSSelector
app = FastAPI()


@app.get("/quote/{ticker}/{exchange}")
def read_root(ticker: str,exchange: str):
    url =("https://www.google.com/finance/quote/"+ticker+":"+exchange)
    xpath = '/html/body/c-wiz[2]/div/div[4]/div/main/div[2]/div[1]/div[1]/c-wiz/div/div[1]/div/div[1]/div/div[1]/div/span/div/div'

    browser = webdriver.Firefox()
    browser.get(url)
    html_source = browser.page_source

    tree = html.fromstring(html_source)
    text = tree.xpath(xpath)
    for i in text:
        print(i.text)
    return {"ticker": ticker,"exchange":exchange,'value':text[0].text,'asd':'asdf'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

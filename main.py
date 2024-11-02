from typing import Union
from lxml import html
from fastapi import FastAPI
import requests
from lxml.cssselect import CSSSelector
app = FastAPI()


@app.get("/quote/{ticker}/{exchange}")
def read_root(ticker: str,exchange: str):
    response =requests.get("https://www.google.com/finance/quote/"+ticker+":"+exchange)
    tree = html.fromstring(response.content)
    selector = CSSSelector('.AHmHk > span:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    elements = selector(tree)
    for value in elements:
        pass
    return {"ticker": ticker,"exchange":exchange,'value':value.text,'asd':'asdf'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

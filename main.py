from typing import Union
from bs4 import BeautifulSoup

from fastapi import FastAPI
import requests
app = FastAPI()


@app.get("/quote/{ticker}/{exchange}")
def read_root(ticker: str,exchange: str):
    response =requests.get("https://www.google.com/finance/quote/"+ticker+":"+exchange)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the element by class name
        # Replace 'your-class-name' with the actual class name
        element1 = soup.find(class_='YMlKec fxKbKc')
        element2 = soup.find(class_='zzDege')


    return {"ticker": ticker,"exchange":exchange,'value':element1.text,'realname':element2.text}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

from typing import Union
from xml.etree.ElementPath import xpath_tokenizer

from bs4 import BeautifulSoup

from fastapi import FastAPI
import requests
app = FastAPI()


@app.get("/quote/")
def read_root(URL: str):
    # https://g.co/finance/AAPL34:BVMF
    teststring="https://g.co/finance/"
    if URL[0:21]==teststring and len(URL)<40 :

        response =requests.get(URL)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the element by class name
            # Replace 'your-class-name' with the actual class name
            element1 = soup.find(class_='YMlKec fxKbKc')
            element2 = soup.find(class_='zzDege')


        return {'data':{'value':element1.text,'realname':element2.text}, "type":"stock"}


@app.get("/motorracing/")
def motor_racing(sport:str, stats:int):
    if sport=="f1" and stats==1:
        # https://www.formula1.com/en/results/2024/races
        response=requests.get('https://www.formula1.com/en/results')
        soup = BeautifulSoup(response.text, 'html.parser')
        currentyear=soup.find(class_="f1-heading tracking-normal text-fs-24px tablet:text-fs-42px leading-tight normal-case font-normal non-italic f1-heading__body font-formulaOne")
        currentyear=str(currentyear.text)[0:4]
        response=requests.get('https://www.formula1.com/en/results/'+currentyear+'/drivers')
        soup = BeautifulSoup(response.text, 'html.parser')

        data = []
        table = soup.find(class_="f1-table f1-table-with-data w-full")
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            print(cols)
            data.append([ele for ele in cols if ele])  # Get rid of empty values

        formatted_data=[]
        for i in data:
            templist=[i[0],i[1].replace('\xa0',' ')[-3:],i[4]]
            print(templist)
            formatted_data.append(templist)
    elif sport=="f1" and stats==2:
        response=requests.get('https://www.formula1.com/en/results')
        soup = BeautifulSoup(response.text, 'html.parser')
        currentyear=soup.find(class_="f1-heading tracking-normal text-fs-24px tablet:text-fs-42px leading-tight normal-case font-normal non-italic f1-heading__body font-formulaOne")
        currentyear=str(currentyear.text)[0:4]
        response=requests.get('https://www.formula1.com/en/results/'+currentyear+'/team')
        soup = BeautifulSoup(response.text, 'html.parser')

        data = []
        table = soup.find(class_="f1-table f1-table-with-data w-full")
        print(soup)
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            print(cols)
            data.append([ele for ele in cols if ele])  # Get rid of empty values

        formatted_data=[]
        for i in data:
            templist=[i[0],i[1],i[2]]
            print(templist)
            formatted_data.append(templist)

    elif sport == "f1" and stats == 3:

        response = requests.get('https://www.formula1.com/en/results')
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find(
            class_="f1-table f1-table-with-data w-full")
        data = []
        table_body = table.find('tbody')

        latestraceurl=[tag.find("a")["href"] for tag in soup.select("td:has(a)")][-1]
        currentyear=soup.find(class_="f1-heading tracking-normal text-fs-24px tablet:text-fs-42px leading-tight normal-case font-normal non-italic f1-heading__body font-formulaOne")
        currentyear=str(currentyear.text)[0:4]
        response = requests.get('https://www.formula1.com/en/results/'+currentyear+'/'+latestraceurl)
        soup = BeautifulSoup(response.text, 'html.parser')
        print('https://www.formula1.com/en/results/'+currentyear+'/'+latestraceurl)
        data = []
        table = soup.find(class_="f1-table f1-table-with-data w-full")
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])  # Get rid of empty values

        formatted_data = []
        print(data)
        for i in data:
            if i[0]=='DQ':
                print(i)
                templist = [i[0], i[2].replace('\xa0', ' ')[-3:],"NA", i[4], i[5]]
            else:
                templist = [i[0], i[2].replace('\xa0',' ')[-3:], i[4],i[5],i[6]]
            print(templist)
            formatted_data.append(templist)


    return {"data":formatted_data,"type":'motorracing'}




@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

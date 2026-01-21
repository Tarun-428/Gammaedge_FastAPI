from fastapi import FastAPI,Response
import httpx
from typing import Union, Optional
import json
app = FastAPI()
datafile = []
@app.get("/")
async def read_root(response:Response):
    # response.headers["X-Cat"] = "Alone in GammaEdge"
    response = Response(content="helow",media_type="Xml")
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.get("/items/{item_id}")
async def read_item(item_id:int, q:Union[int,None]=None):
    Response.headers["X-Cat"] = "Alone in GammaEdge"
    return {"Item_id":item_id,"q":q}


@app.get("/fetch_data")
async def get_data(cursor:Optional[str]=None,limit:int=None):
    with open('data.json','r') as file:
        data = json.load(file)
    data = sorted(data,key=lambda item: item['id'])
    print(len(data))
    if cursor:
        startindex=0
        for index,datas in enumerate(data):
            # print(index)
            # print(datas["id"])
            if datas["id"]==cursor:
                startindex=index+1
                break
        returndata=data[startindex:startindex+limit+1]   
        # print(returndata)
        return returndata  
    else:
        return data[0:limit]




@app.get('/fetch')
async def fetch_data_from_source(): 
    api_url = 'https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json'
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        data = response.json()
        datafile.append(data)
        print(datafile)
        return {
                "data":data
                }





from fastapi import FastAPI, BackgroundTasks
import httpx
import asyncio
app = FastAPI()

async def fetch_data():
    async with httpx.AsyncClient() as client:
        await asyncio.sleep(3)
        api_url = 'https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json'
        response = await client.get(api_url)
        print(response.text)
        

@app.get("/send")
async def sending(background_tasks:BackgroundTasks):
    background_tasks.add_task(fetch_data)
    return{"message":"data"}



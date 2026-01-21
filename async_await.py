import asyncio
import time
from fastapi import FastAPI

app = FastAPI()

async def fetch_weather():
    print("  [Weather] Starting request...")

    await asyncio.sleep(3) 
    print("  [Weather] Data received!")
    return {"temp": "22C"}

async def fetch_stock_prices():
    print("  [Stocks] Starting request...")

    await asyncio.sleep(1) 
    print("  [Stocks] Data received!")
    return {"NVDA": "900.50"}

async def fetch_news():
    print("  [News] Starting request...")

    await asyncio.sleep(2) 
    print("  [News] Data received!")
    return {"headline": "Async is the future"}

@app.get("/dashboard")
async def get_dashboard():
    start_time = time.perf_counter()
    print(">>> Dashboard: Fetching everything at once...")
    
    results = await asyncio.gather(
        fetch_weather(),
        fetch_stock_prices(),
        fetch_news()
    )
    
    end_time = time.perf_counter()
    
    return {
        "time_taken": f"{end_time - start_time:.2f}s",
        "data": results
    }


# import time
# import requests
# from fastapi import FastAPI

# app = FastAPI()

# def fetch_weather():
#     print("  [Weather] Starting request...")
#     time.sleep(3)  
#     print("  [Weather] Done!")
#     return {"temp": "22C"}

# def fetch_stock_prices():
#     print("  [Stocks] Starting request...")
#     time.sleep(1)  
#     print("  [Stocks] Done!")
#     return {"NVDA": "900.50"}

# def fetch_news():
#     print("  [News] Starting request...")
#     time.sleep(2)
#     print("  [News] Done!")
#     return {"headline": "Sequential is slower"}

# @app.get("/dashboard-sync")
# def get_dashboard():
#     start_time = time.perf_counter()
    
#     
#     print(">>> Dashboard: Starting sequential fetch...")
    
#     weather = fetch_weather()       
#     stocks = fetch_stock_prices()   
#     news = fetch_news()             
    
#     end_time = time.perf_counter()
    
#     
#     return {
#         "time_taken": f"{end_time - start_time:.2f}s",
#         "data": [weather, stocks, news]
#     }

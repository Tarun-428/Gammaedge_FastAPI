from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

@app.middleware("1234")
async def add_header(request:Request,call_next):
    start_time =time.ctime()
    print("1 start")
    response = await call_next(request)
    process_time = time.ctime()
    sring = str(start_time)+" "+str(process_time)
    print("1 end")
    response.headers['X-Process-Time'] = sring
    return response

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"Hello":"GammaEdge buddies"}
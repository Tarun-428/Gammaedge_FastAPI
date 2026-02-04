"""API Response Cache Manager
Build a file-based caching system for API responses. This simulates real-world scenarios where applications
cache external API responses to reduce costs and improve performance.
Create functions to:
Generate a cache key from API endpoint and parameters
Save API response to JSON file with timestamp
Load cached response if it exists and is not expired (TTL: 5 minutes)
Clean up expired cache files
Generate cache statistics (hit rate, total cached items, total size)"""


def gen_cache_key(endpoint,parameters):
    key = endpoint+parameters
    return key

import json
from datetime import datetime
def save_response(response,key):
    print("Inside save_response.....")
    cache=load_response()
    try:
        data = response
        timestamp = str(datetime.now())
        data = {
            "timestamp":timestamp,
                    "data":data
            }
        if key not in cache:
            cache[key]=data
            # print(cache)
            with open("api_response.json",'w') as f:
                json.dump(cache,f,indent=4)
            print("Data Successfully saved!")
        else:
            print("Already Present!")
    except Exception as e:
        print(e)

def load_response():
    cache = {}
    print("inside load_response....")
    try:
        with open("api_response.json","r") as f:
            cache = json.load(f)
    except Exception as e:
        print(e)
    return cache
def response_endpoint(key):
    print("inside response_endpoint search by key:")
    cache = load_response()
    if cache[key]:
        print(cache[key])
    else:
        print("no request in cache!")



from datetime import timedelta
def check_expiray(key):
    print('inside check_expiry....')
    cache = load_response()
    time_of = cache[key].get("timestamp")
    time_of = datetime.strptime(time_of,"%Y-%m-%d %H:%M:%S.%f")
    time_delta = timedelta(minutes=5)
    expiry = time_of + time_delta
    time_now = datetime.now()
    if time_now > expiry:
        return False
    else:
        return True

def delete_response(key):
    print('inside delete_response....')
    cache = load_response()
    try:
        del cache[key]
        with open('api_response.json','w') as f:
            json.dump(cache,f,indent=4)
    except Exception as e:
        print(e)

def clean_expiray():
    print('inside clean_expiry...')
    cache = load_response()
    for key,value in cache.items():
        if not check_expiray(key):
            delete_response(key)
    print("All Expiry data deleted")


response = [
    {
      "data": [
        {
          "type": "articles",
          "id": "3",
          "attributes": {
            "title": "JSON:API paints my bikeshed!",
            "body": "The shortest article. Ever.",
            "created": "2015-05-22T14:56:29.000Z",
            "updated": "2015-05-22T14:56:28.000Z"
          }
        }
      ],
    }
]
# save_response(response)
# load_response()
# clean_expiray()

def main(response,endpoint="http://localhost:8000",parameters="/api/data/4"):
    #generate key
    key = gen_cache_key(endpoint,parameters)
    save_response(response,key)
    clean_expiray()
    response_endpoint(key)

main(response)
# key = "http://localhost:8000/api/data/1"
# cache = load_response()
# # print(cache)
# # if key in cache:
# #     cache[key] = response
# print(cache)
# print(type(cache))




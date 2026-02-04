"""APIClient class with:
Rate limiter using decorators (max 10 requests per minute)
Automatic retry with exponential backoff decorator
Response caching with TTL using functools.lru_cache
Request/response logging with timestamps
Circuit breaker pattern (stop requests after 5 consecutive failures)"""


from functools import wraps,lru_cache
import time
from collections import deque

from jedi.api import extract_function


# class APIClient:
def rate_limiter(max_call:int,period:int):
    def decorator(func):
        calls = deque()
        @wraps(func)
        def wrapper(*args,**kwargs):
            tiem = time.time()
            # one_min = tiem+60
            while calls and calls[0] <= tiem - period:
                calls.popleft()
            if len(calls)>=max_call:
                print("Limitt exceeded")
                return
            print(len(calls))
            calls.append(tiem)
            result = func(*args,**kwargs)
            print("resource available!")
            return result
        return wrapper
    return decorator

def retries(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        max_limit = 3
        for attempt in range(0,3):
            try:
                return func(*args,**kwargs)
            except Exception as e:
                print(f"retrying....",attempt+1)
                if attempt == max_limit-1:
                    print("Maximum reached!")
    return wrapper
def ttl_cache(func):
    # ttl = 6
    ttl_second=10
    @lru_cache(maxsize=128)
    def wrapper(*args,tt,**kwargs):
        try:
            # print(lru_cache())
            # result =func(*args,**kwargs)
            # print(f"printing",result)
            return lru_cache()(func)(*args,**kwargs)
        except Exception as e:
            print(e)

    @wraps(func)
    def inner(*args,**kwargs):
        print("calling")
        return wrapper(*args,tt=round(time.time()/ttl_second),**kwargs)

    inner.cache_info = wrapper.cache_info
    return inner
# class APIMetrics:
#     def __init__(self):



# @rate_limiter(5,60)
# @lru_cache
@ttl_cache
def add(a,b):
    time.sleep(3)
    return a+b
for i in range(0,10):
    print(add(10,20))
data = add.cache_info()
lst = []
for i in data:
    lst.append(i)
print(f"Total request ", lst[0]+lst[1])
print(f"Hit request ",lst[0])
print(f"Miss request ",lst[1])
print(data.hits)










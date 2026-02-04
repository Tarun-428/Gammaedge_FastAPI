#Use list comprehension to create a list of squares from 1 to 20, but only for even numbers.
import re

lst = [x*x for x in range(2,21,2)]
print(lst)

#Write a generator function that yields Fibonacci numbers up to n.
from functools import wraps
import time
def exec_timing(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        startime = time.perf_counter()
        result = func(*args,**kwargs)
        endtime = time.perf_counter()
        exec = endtime-startime
        print(f"{func.__name__()}time of execution is : {exec:.4f}")
        return result
    return wrapper

def fibonacci(n):
    a,b = 0,1
    while a<=n:
        yield a
        a,b = b,a+b

# for i in fibonacci(100):
#     print(i)
@exec_timing
def add():
    time.sleep(3)
    return 0
# add()


#Create a decorator that caches function results (memoization) using a dictionary.
def caches_deco(func):
    cache = {}
    @wraps(func)
    def wrapper(*args,**kwargs):
        key = args+tuple(sorted(kwargs.items()))
        if key in cache:
            print("found in cache")
            return cache[key]
        else:
            print("not found calling functin")
            result = func(*args,**kwargs)
            cache[key] = result
            return result
    return wrapper

# @caches_deco
# def add(a,b,c=3):
#     return a+b+c
# print(add(10,20))
# print(add(10,20))
# print(add(10,25))
# print(add(10,20))

#Implement a decorator that retries a function up to 3 times on failure with exponential backoff.
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
# @retries
# def testing(a):
#     print("int is ",int(a))
# testing("Tarun")


#Use itertools.combinations to find all possible pairs from a list and filter pairs that sum to a target value.
from itertools import combinations
def find_sum(number,target):
    pairs = combinations(number,2)
    # t_pair = [pair for pair in pairs if sum(pair)==target]
    for pair in pairs:
        if sum(pair)==target:
            t_pair = pair
    return t_pair

# print(find_sum([1,2,3,4,5,3,2,1],4))

#Write a program using regular expressions to extract email addresses, phone numbers, and URLs from text.
def extractor(strr):
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    email = re.findall(r'[a-zA-Z0-9.+%-]+@[a-zA-Z0-9.+%-]+\.[a-zA-z]{2,}',strr)
    phone = re.findall(r'\d{10}',strr)
    urls = re.findall(r'(?P<url>https?://[^\s]+)',strr)
    return email,phone,urls
print(extractor("here is my emails tarun@gmail.com, mr.tarunpatidar@gmail.io here is my number is 9302964803, 9302957251 with my urls https://google.com, https://example.com"))
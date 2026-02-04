# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
#
# def add(x, y):
#     return x + y
#
# sum_of_numbers = reduce(add, numbers)
# print(sum_of_numbers)
#
# def even(x):
#     return x%2==0
# lst = [1,2,3,4,5,12,6,7,8,9,10]
# even_no = list(filter(even,lst))
# print(even_no)
#
# def square(x):
#     return x*x
# sq = list(map(square,lst))
# print(sq)
#
# names = ['Alice', 'Bob', 'Charlie']
# scores = [1, 3, 3]
# for name, score in zip(names,scores):
#     print(name,score)
# for i,name in enumerate(names,start=1):
#     print(i,name)
#
# result = any(x%2==0 for x in scores)
# result2 = list(map(lambda x: x%2==0, scores))
# print(result2)
#
# print(isinstance(scores,list))
#
# class human:
#     def walk(self):
#         print("walking")
# class rahul(human):
#     def fly(self):
#         print("flying")
#
# abc= rahul()
# iss=isinstance(abc,human)
# print(iss)
# import inspect
# print(inspect.ismethod(abc.walk))

import json
data = []
def json_to_dict():
    with open("data.json","r") as f:
        data = json.load(f)
    dataL = {k:v for d in data for k,v in d.items()}
    print(dataL)

# Create a function to write a list of dictionaries to a CSV file with headers.
import csv
def data_to_csv():
    with open("test.csv",'w') as f:
        csv_data = csv.DictWriter(f,["name","language","id","bio","version"])
        csv_data.writeheader()
        csv_data.writerows(data)

#Implement a function that generates a random password with specific requirements (length, uppercase, lowercase, digits, special chars).
import random
password = []
for _ in range(0,3):
    char= random.randint(65,90)
    password.append(chr(char))
for _ in range(0,5):
    char=random.randint(97,122)
    password.append(chr(char))
for _ in range(0,2):
    char = random.randint(33,38)
    password.append(chr(char))
for _ in range(0,2):
    char = random.randint(48,57)
    password.append(chr(char))
# print(password)
random.shuffle(password)
str_pass= ""
for char in password:
    str_pass+=char
print(str_pass)

#Implement a decorator function that measures the execution time of other functions.
import time
from datetime import timedelta
def time_calc(func):
    def main_fun(*args,**kwargs):
        t1 = time.perf_counter()
        result = func(*args,**kwargs)
        t2 = time.perf_counter()
        tot_time = t2-t1
        print(f"execution time : of {t2-t1:.6f}")
        return result
    return main_fun

@time_calc
def test():
    for i in range(0,1000000):
        for j in range(0,100):
            pass
test()

#Create a function that reads a large file line by line efficiently using a generator, and processes it in chunks.

def chunks(file):
    # while True:
        lin = file.readlines()
        if not lin:
            # break
            return
        else:
            yield(lin)

with open("test.txt",'r') as f:
    for i in chunks(f):
        print("\n",i)

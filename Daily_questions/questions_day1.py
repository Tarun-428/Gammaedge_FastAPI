print("# Write a program to swap two variables without using a third variable.")
a,b =input("Enter two numbers:").split()
a = int(a)
b = int(b)
print(f"Value of a: {a} and b: {b} before swapping")
#method 1 using addition
a = a+b
b = a-b
a = a-b

#method 2 pythonic way
a,b = b,a

#method 3 bitwise
a = a^b
b = a^b
a = a^b
print(f"Value of a: {a} and b: {b} after swapping")


print("\n#Create a program that takes user input for name and age, then prints a formatted message using f-strings\n#Write a program to format a string using all three formatting methods (%, .format(), f-strings)\n")
name,age = input("Enter Name and Age: ").split()
age = int(age)
print(f"{name} is {age} years old, using f string")
print("Name {} and Age {}, using format".format(name,age))
print("Name %s and Age %d, using modulo" %(name,age))


print("\n#Write a program to check if a number is even or odd using modulo operator.")
a = int(input("Enter Number to check  :"))
if a%2==0:
    print("Even no.")
else:
    print("odd no.")



print("\n#Convert temperature from Celsius to Fahrenheit and vice versa.")
"""Temp Celsius to fahrenheit"""
temp = int(input("Enter temperature in Celsius : "))
temp_to_Fahrenheit  = (temp*9/5) + 32
print(f"Temperature in Fahrenheit : {temp_to_Fahrenheit:.2f}`F")

"""Temp Fahrenheit to Celsius"""
temp = int(input("\nEnter temperature in Fahrenheit : "))
temp_to_celsius= (temp-32)*5/9
print(f"Temperature in Celsius : {temp_to_celsius:.2f}`C")



print("\n#Check if a given string is a palindrome (case-insensitive).")
strr = input("Enter String to check palindrome : ")
strr = strr.lower()

is_palindrome = strr[:] == strr[::-1]
if is_palindrome:
    print("string is palindrome using comparison")
else:
    print("String is not palindrome")
i,j = 0, len(strr)-1
while i<=j:
    if strr[i] != strr[j]:
        print("String is not palindrome using two pointer's")
        break
    i+=1
    j-=1
else:
    print("String is palindrome")


print("\n#Count the frequency of each character in a string using a dictionary.")
input_string = input("input string to check characters : ")
freq_dict={}
for i in input_string:
    if i not in freq_dict:
        freq_dict[i] = 1
    else :
        freq_dict[i] +=1
for key,value in freq_dict.items():
    print(f"KEY {key}: Value {value}")



print("\n#Write a program to check if a year is a leap year.")
year = int(input("Enter Year : "))
if year%4==0:
    print("Leap Year")
else:
    print("Not Leap Year")



print("\n#Check if two strings are anagrams of each other.")
anagram1 = input("Enter first string : ")
anagram2 = input("Enter second string  : ")
if sorted(anagram1.lower()) == sorted(anagram2.lower()):
    print("Both strings are anagrams!")
else:
    print("Strings are not anagrams!")






"""calculator Functions"""
def addition(*args):
    add = 0
    for i in args:
        add+=i
    print(f"Addition of {len(args)} Numbers : ",add)


def subtract(*args):
    sub = args[0]
    for i in args[1:]:
        sub -= i
    print(f"Subtraction of {len(args)} Numbers : ", sub)

def multiply(*args):
    multiple = 1
    for i in args:
        multiple*=i
    print(f"Multiply of {len(args)} Numbers : ",multiple)


def division(*args):
    divisor = args[0]
    for i in args[1:]:
        divisor/=i
    print(f"Division of {len(args)} Numbers : ",divisor)


print("\n#Create a CLI calculator that performs basic arithmetic operations based on user input with input validation")
print("*** Welcome to Calculator! ***")
print("\nSelect your choice")
while(True):
    choice = input("\n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division\n5 for Exit\n")
    if not choice.isdigit():
        print("Choice should be Integer only!!")
    else:
        if int(choice)==1:
            args = [int(num) for num in input().split() if num.isdigit()]
            addition(*args)
        elif int(choice)==2:
            args = [int(num) for num in input().split() if num.isdigit()]
            subtract(*args)
        elif int(choice)==3:
            args = [int(num) for num in input().split() if num.isdigit()]
            multiply(*args)
        elif int(choice)==4:
            args = [int(num) for num in input().split() if num.isdigit()]
            division(*args)
        elif int(choice)==5:
            print("Thank you!")
            break
        else:
            print("Choice can not be greater than 4!")



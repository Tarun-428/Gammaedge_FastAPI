print("Write a program to print all even numbers from 1 to 100 using a for loop.")
for i in range(0,101):
    if i%2==0:
        print(i)

print("Print the first 10 numbers in the Fibonacci sequence using a while loop.")
a = 0
b = 1
i = 2
print(a,b)
while i<=10:
    c = a+b
    a,b = b,c
    i+=1
    print(c)

print("Create a list of squares of numbers from 1 to 10 using list comprehension.")
lst = [x*x for x in range(1,11)]
print(lst)

print("Write a program to find the largest element in a list.")
maximum = 0
for i in lst:
    if i>maximum:
        maximum = i
print(maximum)

print("Write a program to find the second largest number in a list without sorting.")
maximum = 0
secMax = 0
for i in lst:
    if maximum<i:
        secMax = maximum
        maximum = i
    elif i>secMax and i!=maximum:
        secMax = i
print(secMax)

print("Create a dictionary from two lists (one for keys, one for values) using zip().")
keys = ["Mango","Apple","Orange"]
values = [10,20,12]
stock_dict = dict(zip(keys,values))
print(stock_dict)

print("Find the common elements between two lists using sets.")
list_a = [1, 2, 3, 4, 5, 6]
list_b = [4, 5, 6, 7, 8, 9]

set_a = set(list_a)
set_b = set(list_b)

common = set_a & set_b

common_list = list(common)
print(common_list)

print("Implement a basic phonebook using a dictionary (add, search, delete, update contacts).")
phonebook = {}

def add_contact():
    name = input("Enter contact name: ")
    if not name:
        print("Name cannot be empty.")
        return

    name = name.title()
    if name in phonebook:
        print(f"'{name}' already exists. Use 'Update' to change the number.")
        return

    number = input("Enter phone number: ")
    if not number:
        print("Number cannot be empty.")
        return

    phonebook[name] = number
    print(f"'{name}' added successfully.")

def search_contact():
    name = input("Enter name to search: ")
    name = name.title()

    if name in phonebook:
        print(f"Name: {name}, Number: {phonebook[name]}")
    else:
        print(f"'{name}' not found in the phonebook.")

def delete_contact():
    name = input("Enter name to delete: ")
    name = name.title()

    if name in phonebook:
        del phonebook[name]
        print(f"'{name}' deleted successfully.")
    else:
        print(f"'{name}' not found in the phonebook.")


def update_contact():
    name = input("Enter name to update: ")
    name = name.title()

    if name in phonebook:
        new_number = input(f"Enter new number for '{name}': ")
        if not new_number:
            print("Number cannot be empty; update cancelled.")
            return
        phonebook[name] = new_number
        print(f"'{name}' number updated successfully.")
    else:
        print(f"'{name}' not found. Use 'Add' to create a new contact.")

def view_all_contacts():
    if not phonebook:
        print("The phonebook is currently empty.")
    else:
        print("\n Current Phonebook")
        # Sort by name for a cleaner display
        for name, number in sorted(phonebook.items()):
            print(f"{name}: {number}")
        print("*******\n")

def main_menu():
    while True:
        print("\n*** Phonebook Menu ***")
        print("1. Add a contact")
        print("2. Search for a contact")
        print("3. Delete a contact")
        print("4. Update a contact")
        print("5. View all contacts")
        print("6. Exit")
        print("*******")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            view_all_contacts()
        elif choice == '6':
            print("Exiting Phonebook!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
main_menu()


print("Implement a program to check if parentheses/brackets in a string are balanced using a stack (list).")
def paranthesis(s):
    stack = []
    bracket_pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    opening_brackets = set(bracket_pairs.keys())
    closing_brackets = set(bracket_pairs.values())
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            last_opening_bracket = stack.pop()
            if bracket_pairs[last_opening_bracket] != char:
                return False
    return len(stack)==0

test_case = [
        "()",
        "()[]{}",
        "{[()]}",
        "([)]",
        "{[}",
        "]",
        "((()))",
        "(()",
        "{{}}[()]"
    ]
for test in test_case:
    balance = "balanced" if paranthesis(test) else "not balanced"
    print(f"{test} is {balance}")


print("Create a dictionary that groups anagrams together from a list of words.")
arr = ["act", "god", "cat", "dog", "tac"]
dicto = {}
for ele in arr:
    sortele = ''.join(sorted(ele))
    if sortele not in dicto:
        dicto[sortele] = [ele]
    else:
        dicto[sortele].append(ele)
print(dicto)
# '''
# Create a program that uses a dictionary to store phonebook
# entries. Must have user interaction.
# Include ability to:
# 1. Search
# 2. Add Entry
# 3. Chage Entry
# 4. Delete Entry
# 5. Exit Program
# '''
​
phonebook = {
'chris': {'name': 'Chris', 'phone': "503-277-9710"},
    'sam': {'name': 'Sam', 'phone': "503-277-9710"}}

def search():
    search = input('Who are you looking for')
    print(phonebook[search.lower]["name"])
    print(phonebook[search.lower]["phone"])

def add_entry():
    add_entry = input('What is the name?')
    phone = input('What is the phone number')
    phonebook [add_entry] = {'name': add_entry, 'phone': phone}

​
# How to look someone up in a dictionary
# try:
#     search = input('Who are you looking for? ')
#     print(phonebook[search.lower()])
#     print(phonebook[search.lower()]['name'])
#     print(phonebook[search.lower()]['phone'])
# except KeyError:
#     print('There is no entry of {}'.format(search))
​
# Add to a dictionary
# name = input('What is the name? ')
# phone = input('What is the phone? ')
# phonebook[name.lower()] = {'name': name.capitalize(), 'phone': phone}
# print(phonebook)
​
# Delete something from a dictionary
# del phonebook['chris']
# print(phonebook)
​
# User input loop fuction
# def phone_book():
#     print("Welcome to the Phone Book!")
#     while True:
#         print("-" * 40)
#         print("Press 1 to search.")
#         print("Press 2 to add.")
#         print("Press 3 to change an entry.")
#         print("Press 4 to remove.")
#         print("Press 5 to exit.")
#         print("-" * 40)
#         try:
#             choice = int(input('> '))
#             if choice == 1:
#                 search()
#             elif choice == 2:
#                 add()
#             elif choice == 3:
#                 change()
#             elif choice == 4:
#                 remove()
#             elif choice == 5:
#                 exit()
#         except ValueError:
#             print("That is not a valid entry. Please try again.")
#
# phone_book()

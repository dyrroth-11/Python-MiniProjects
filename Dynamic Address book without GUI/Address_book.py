#!/usr/bin/env python3
"""
Created on Thu Apr 23 19:21:42 2020

@author: Ashish Patel
"""
"""
Problem: Task: Create an small address book 
         Case: Write an address book program in python which have the following option:
            1. Add_contact
            2. Display_contact
            3. Delete_contact
            4. Modify_contact
            5. Seach_contact

"""

class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email
    def edit_name(self, name):
        self.name = name
        return self.name
    def edit_number(self, number):
        self.number = number
        return self.number
    def edit_email(self, email):
        self.email = email
        return self.email

    @classmethod
    def add(cls, name,number,email):
        return cls(name, number,email)
    @staticmethod
    def summary(index=0):
        if index == -1:
            for j in range(0, len(address_book)):
                print(address_book[j].name ,'-',address_book[j].number, '-', address_book[j].email )
        else:
            print(address_book[index].name, '-', address_book[index].number, '-', address_book[index].email)
        print()
        return None
    @staticmethod
    def saved():
        print('CONTACT LIST : ')
        for j in range(0, len(address_book)):
            print(j+1, address_book[j].name)
        return None
    @staticmethod
    def isempty(list):
        if len(list) == 0:
            print('NO CONTACT IN ADDRESS BOOK \n')
            return True
        return False
address_book = []
msg_error = 'Invalid option\n'
while True:
    print('##############  CONTACTS MENU ###############')
    print("""
               1. Add_contact         
               2. Display_contact
               3. Delete_contact
               4. Modify_contact 
               5. Search_contact
               0. Exit            """)

    option = input('>>')
    if option not in '012345':
        print(msg_error)
        continue
    else:
        option = int(option)
    if option == 0:
        print('*** Thanks For using our menu ***\n')
        break

    elif option == 1:
        name = input('Name: ').capitalize().strip()
        number = input('Number: ').strip()
        email = input('Email: ').strip().lower()
        address_book.append(Contact.add(name,number, email))
        print('Contact saved\n')

    elif option == 4:
        if Contact.isempty(address_book):
            continue
        Contact.saved()
        name_index = int(input('\nEnter the number in front  of contact to be modified: \n'))
        print('\nModify which entry?')
        entry_index = int(input('1. NAME    \n2. NUMBER   \n3. EMAIL\n>>>'))
        if entry_index == 1:
            modification = input('New name: ').capitalize().strip()
            address_book[name_index-1].edit_name(modification)
        elif entry_index == 2:
            modification = input('New number: ').strip()
            address_book[name_index-1].edit_number(modification)
        elif entry_index == 3:
            modification = input('New email: ').lower().strip()
            address_book[name_index-1].edit_email(modification)
        print('Modification saved\n')

    elif option == 3:
        if Contact.isempty(address_book):
            continue
        Contact.saved()
        name_index = int(input('\nEnter the number in front  of contact to be modified: '))
        if(name_index>len(address_book) or name_index <0): print("NO CONTACT WITH THIS NAME \n")
        else:
             del address_book[name_index-1]
             print('Contact deleted')

    elif option == 5:
        if Contact.isempty(address_book):
            continue
        Contact.saved()
        index = int(input('\nContact position: '))
        Contact.summary(index-1)

    elif option == 2:
        if Contact.isempty(address_book):
            continue
        Contact.summary(-1)


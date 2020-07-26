#!/usr/bin/env python3
"""
Created on Thu Apr 23 17:42:08 2020

@author: Ashish Patel
"""
"""
Problem: Task: Menu Calculator 
         Case: Imagine you have started up a small restaurant and are trying to make it easier to take
               and calculate orders. Since your restaurant only sells 5 different items, you assign each one to a
               number, as shown below.
                 1. Chicken Strips - $3.50
                 2. French Fries - $2.50
                 3. Hamburger - $4.00
                 4. Hotdog - $3.50
                 5. Large Drink - $1.75
                 6. Medium Drink - $1.50
                 7. Milk Shake - $2.25
                 8. Salad - $3.75
                 9. Small Drink - $1.25
        To quickly take orders, your program should allow the user to type in a string of numbers and
        then it should calculate the cost of the order.

        For example, if one large drink, two small drinks, two hamburgers, one hotdog, and a salad are
        ordered, the user should type in 5993348, and the program should say that it costs $19.50.
        Also, make sure that the program loops so the user can take multiple orders without having to
        restart the program each time.
        ● Subgoals:
            ○ If you decide to, print out the items and prices every time before the user
              types in an order.
            ○ Once the user has entered an order, print out how many of each item
              have been ordered, as well as the total price.
            ○ If an item was not ordered at all, then it should not show up.

"""
menu = [
    [1, "Chicken Strips", 3.55],
    [2, "French Fries", 2.50],
    [3, "Hamburger", 4.00],
    [4, "Hot Dog", 3.50],
    [5, "Large Drink", 1.75],
    [6, "Medium Drink", 1.50],
    [7, "Milk Shake", 2.25],
    [8, "Salad", 3.75],
    [9, "Small Drink", 1.25]
       ]

print("\n************ Menu ************")
for item in menu:
    print('{}. {} - ${:.2f}'.format(*item))

x = str(input('\nPlease enter the order: '))

print("\nYou ordered is : \n************************************",)
a=[0,0,0,0,0,0,0,0,0]
for i in x:
    a[int(i)-1]=a[int(i)-1]+1
total = 0
for i in range(9):
    if(a[i]>0):
        print('{}.{} X{} - ${}'.format(i+1,menu[i][1],a[i],int(menu[i][2])*a[i]))
        total = total + int(menu[i][2])*a[i]

print("************************************\nTotal is : ${} ".format(total))

sm = 1
ii = 1

while i <= sm:
    ii = sm
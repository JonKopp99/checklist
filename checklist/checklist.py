# coding: utf-8
import os
checklist = []
CRED = '\033[91m'
CEND = '\033[0m'
CGREEN = '\033[92m'

def my_fun_function(say_this):
    print(say_this)

def create(item):
    checklist.append(item)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + CRED + list_item + CEND)
        index += 1


def read(index):
    item = checklist[index]
    return item

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)


def mark_completed(index):
    temp = checklist[index]
    temp = "√" + temp
    update(index,temp)



def select(theString):
    # Create item
    if theString.lower() == "a":
        input_item = user_input("What item would you like to add?:")
        create(input_item)
        unused_variable = os.system("clear")
    elif theString.lower() == "d":
        item_index = int(user_input("Index Number?:"))
        if(item_index <= len(checklist)):
            destroy(item_index)
        else:
            print("Enter a number in the list's range pls.")
            unused_variable = os.system("clear")
    elif theString.lower() == "c":
        item_index = int(user_input("Index Number?:"))
        if(item_index <= len(checklist)):
            mark_completed(item_index)
        else:
            print("Enter a number in the list's range pls.")
            unused_variable = os.system("clear")
    elif theString.lower() == "u":
        item_index = int(user_input("Index Number?:"))
        if(item_index <= len(checklist)):
            update(item_index,raw_input("What would you like to update it with?:"))
        else:
            print("Enter a number in the list's range pls.")
            unused_variable = os.system("clear")
    # Read item
    elif theString.lower() == "r":
        item_index = int(user_input("Index Number?:"))
        # Remember that item_index must actually exist or our program will crash.
        if(item_index <= len(checklist)):
            print(CRED + read(item_index) + CEND)
        else:
            print("Enter a number in the list's range pls.")
            unused_variable = os.system("clear")

    # Print all items
    elif theString.lower() == "p":
        list_all_items()

    elif theString.lower() == "q":
        unused_variable = os.system("clear")
        return False
    # Catch all
    else:
        print("Unknown Option :()")
    return True

def user_input(prompt):
    user_input = raw_input(prompt)
    return str(user_input)

def test():
    create("purple sox")

    running = True
    while running:
        selection = user_input(CGREEN+"Press A to add to list, R to Read from list, P to display list, U to update, D to destroy,C to check, and Q to quit\nEnter:"+CEND)
        running = select(selection)


test()

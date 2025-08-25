import csv
from random import choice

arr = []

def syncArrToCsv():
    global arr
    arr = []  # reset to avoid duplicates
    with open("passwords.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            arr.append(row)

def addPassword():
    name = input("Enter your username/email: ")
    password = input("Enter your password: ")
    syncArrToCsv()
    id = len(arr) + 1
    data = [id, name, password]
    with open("passwords.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def removePassword():
    syncArrToCsv()
    for item in arr:
        print(item["name"])
    name = input("Enter name to remove: ")
    to_remove = next((d for d in arr if d.get("name") == name), None)
    if to_remove:
        arr.remove(to_remove)
        print(arr)
        with open("passwords.csv", "w", newline='') as f:
            fieldnames = ["id", "name", "password"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(arr)

def viewPasswords():
    syncArrToCsv()
    print("Available usernames:")
    for item in arr:
        print(item["name"])
    user = input("> ")
    account = next((d for d in arr if d.get("name") == user), None)
    if account:
        print(f"{user}'s password: {account['password']}")
    else:
        print("User not found.")    
    
def generatePassword():
    string = "abcdefghijkl`~!@#$%^&*()_+-=|:;'\"\\/?.><mnopqrstuvwxyzABCDEFGHI0123456789JKLMNOPQRSTUVWXYZ"
    length = ""
    password = ""
    
    while True:
        try:
            length = int(input("Length? "))
        except:
            print("Enter a number")
            continue
        finally:
            break

    for i in range(length):
        password += choice(string)
    print(password)

def editPassword():
    syncArrToCsv()
    print("Available usernames:")
    for item in arr:
        print(item["name"])
    user = input("Enter the username to edit: ")
    account = next((d for d in arr if d.get("name") == user), None)
    if account:
        new_pass = input(f"Enter new password for {user}: ")
        account["password"] = new_pass
        # Write updated data back to CSV
        with open("passwords.csv", "w", newline='') as f:
            fieldnames = ["id", "name", "password"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(arr)
        print(f"Password for {user} updated successfully.")
    else:
        print("User not found.")


while True:
    inp = input("Select function ([q]uit, [r]emove, [a]dd, [v]iew, [g]enerate): ")
    match inp:
        case "q":
            break
        case "r":
            removePassword()
        case "a":
            addPassword()
        case "v":
            viewPasswords()
        case "g":
            generatePassword()
        case "e":
            editPassword()
        case _:
            continue
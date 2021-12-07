# Create Contacts List
contactList = []

# Clear Console Function
import os
def clear(): os.system('cls')

# Check if inputs are valid

def getValidStr(inp):
    valid = True
    while valid:
        try:
            int(inp)
            inp = input("Invalid response, please enter a string: ")
        except:
            valid = False
            return inp

def getValidInt(inp):
    valid = True
    while valid: 
        try: 
            int(inp)
            valid  = False
            return int(inp)
        except:
            inp = input("Invalid reponse, please enter a number: ")

# Login or Signup Menu
from logindata import *
import json

def getLoginMenuSelection():
    clear()
    print("\nDo you wish to login or sign up?")
    print("1: Login")
    print("2: Signup")

    inp = input("Enter option 1 or option 2: ")
    inp = getValidInt(inp)

    if inp == 1:
        login()
    
    elif inp == 2:
        signup()

def login():
    username = input("Enter your username: ")
    username = getValidStr(username)

    # Open json file
    f = open('users.json')

    # return json object as a dict and turn it into array
    users = json.load(f)
    users = dict.items(users)

    for i in range(len(users) - 1):
        if username == users[i]:
            f.close()
            pass
        else:
            print("Username not registered")
            getLoginMenuSelection

def signup():
    # Open json file
    f = open('users.json', "r")
    data = json.load(f) # read file data and convert JSON to dictionary
    f.close()

    # object to be appended
    inp = input("Enter a new username: ")
    inp = getValidStr(inp)
    
    # appending data
    data["users"].append(inp)

    # convert object into JSON string and write to file
    f = open("users.json", "w")
    json.dump(data, f) 
    f.close()
    
    getLoginMenuSelection()
    
getLoginMenuSelection()

# Contacts Class
class Contact:
    # Initialize method
    def __init__(self, name, number, email):

        self.name = name
        self.number = number
        self.email = email

    # Print Object Method
    def __str__(self):
        return f"\nName: {self.name} \nNumber: {self.number} \nEmail: {self.email}"

    # Set New Name Method
    def setName(self, newName):
        self.name = newName
    
    # Set New Number Method
    def setNumber(self, newNumber):
        self.number = newNumber

    # Set New Email Method
    def setEmail(self, newEmail):
        self.email = newEmail

# Create Initial Contacts
#contactList.append(Contact("Colin", "780-123-4567", "colinveldkamp6@gmail.com"))
#contactList.append(Contact("Advi", "780-163-9527", "adviislam34@gmail.com"))
#contactList.append(Contact("Robert", "780-191-6799", "roberto9@gmail.com"))
#contactList.append(Contact("Kim", "780-232-2145", "kimberlyy04@yahoo.com"))
#contactList.append(Contact("Riyana", "780-857-1093", "ririyana7@gmail.com"))
#contactList.append(Contact("Darrell", "780-909-0022", "darellderrick0@yahoo.com"))
#contactList.append(Contact("Mohamed", "780-289-2034", "momoabdelrahman1@gmail.com"))
#contactList.append(Contact("William", "780-745-5954", "willywilliam90@gmail.com"))
#contactList.append(Contact("Jaehoon", "780-289-2418", "jaejit892@gmail.com"))
#contactList.append(Contact("Julia", "780-366-0595", "heyjuliee00@gmail.com"))

# Main Menu Loop
def main():
    # Clear Console
    clear()

    # Main Menu Loop
    loop = True
    while loop:
        selection = getMenuSelection()

        # Output Based on Selection
        if selection == "1":
            displayList()
        elif selection == "2":
            addNewContact()
        elif selection == "3":
            deleteContact()
        elif selection == "4":
            searchContacts()
        elif selection == "5":
            showContact()
        elif selection == "6":
            changeContact()
        elif selection == "7":
            print("\nGoodbye")
            loop = False
        else:
            print("\nInvalid menu selection")
        # End main while loop
    # End main()
    
# Get Menu Selection
def getMenuSelection(): 

    print("\nMAIN MENU")
    print("1: Display Contacts")
    print("2: Add new contact")
    print("3: Delete Contact")
    print("4: Search for contact")
    print("5: Show Contact Information")
    print("6: Change Contact Information")
    print("7: Exit")

    return input("Enter a menu option: ")
    # End getMenuSelection()

# MENU FUNCTIONS:

# Display contacts
def displayList():

    clear()
    print("Contacts: ")
    for i in range(len(contactList)):
        print(str(i + 1) + ".", contactList[i].name)
    # End displayList()

# Add New Contact
def addNewContact():

    clear()
    contactList.append(Contact(input("Enter name: "), input("Enter phone number: "), input("Enter email: ")))
    # End addNewContact()

# Delete Contact
def deleteContact():

    clear()
    displayList()
    contactNumber = input("Which contact # do you wish to delete? ")
    contactNumber = getValidInt(contactNumber)

    if contactNumber <= len(contactList) and contactNumber > 0:
        contactList.pop(contactNumber - 1)
        print("Done")
    else:
        print("Invalid input")
    # End deleteContact()

# Search for Contact
def searchContacts():
    clear()
    found = False
    # Get input for contact name and check
    inp = input("\nEnter contact name: ")
    inp = getValidStr(inp)
    print("\nResults:")

    for i in range(len(contactList)):
        if contactList[i].name == inp or inp in contactList[i].name.lower():
            found = True
            print(contactList[i].name)
    
    # Display message if no contacts found
    if found == False:
        print("No Contacts were found")
    # End searchContacs()

# Show Contact Information
def showContact():

    # Display Contacts
    displayList()
    # Get User Input 
    inp = int(input("\nWhich contact # do you wish to see? "))
    inp = getValidInt(inp)
    if inp <= len(contactList) and inp > 0:
        print(contactList[inp - 1])
    
    else: 
        print("Invalid Input")
    # End showContact()

# Change Contact Information
def changeContact():

    # Ask which contact 
    displayList()

    contactNumber = (input("\nWhich contact # do you wish to edit? "))
    contactNumber = getValidInt(contactNumber)

    if int(contactNumber) <= len(contactList) and int(contactNumber) > 0:  
        # Get User Input 
        inp = input("\nDo you wish to change contact name, phone number or email? ")
        inp = getValidStr(inp)

        # Action based on input
        if inp == "Name" or inp == "name":
            Contact.setName(contactList[contactNumber- 1], input("Enter new name: "))
            print("Done")
        elif inp == "Number" or inp == "number":
            Contact.setNumber(contactList[contactNumber- 1], input("Enter new phone number: "))
            print("Done")
        elif inp == "Email" or inp == "email":
            Contact.setEmail(contactList[contactNumber- 1], input("Enter new email: "))
            print("Done")
        else:
            print("\nInvalid input")
    
    else:
        print("\nCOntact does not exist")
    # End changeContact()

# Call main() to start program
main()
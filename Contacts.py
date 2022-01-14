# Create Users List
users = []
import sys

# Clear Console Function
import os
def clear(): os.system('cls')

# Input Validation Function
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

# Contact Class
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

# User Class
class User: 
    # Initialize method
    def __init__(self, username, contactList):

        self.username = username
        self.contactList = contactList
    
    # Display contacts
    def displayList(self):
        clear()
        print("Contacts: ")
        for i in range(len(self.contactList)):
            print(str(i + 1) + "." + self.contactList[i].name)
        # End displayList()

    # Add New Contact
    def addNewContact(self):
        clear()
        self.contactList.append(Contact(input("Enter name: "), input("Enter phone number: "), input("Enter email: ")))
        # End addNewContact()

    # Delete Contact
    def deleteContact(self):
        clear()
        User.displayList(self)
        contactNumber = input("Which contact # do you wish to delete? ")
        contactNumber = getValidInt(contactNumber)

        if contactNumber <= len(self.contactList) and contactNumber > 0:
            self.contactList.pop(contactNumber - 1)
            print("Done")
        else:
            print("Invalid input")
        # End deleteContact()

    # Search for Contact
    def searchContacts(self):
        clear()
        found = False
        # Get input for contact name and check
        inp = input("\nEnter contact name: ")
        inp = getValidStr(inp)
        print("\nResults:")

        for i in range(len(self.contactList)):
            if self.contactList[i].name == inp or inp in self.contactList[i].name.lower():
                found = True
                print(str(i + 1) + ". " + self.contactList[i].name)
        
        # Display message if no contacts found
        if found == False:
            print("No Contacts were found")
        # End searchContacs()

    # Show Contact Information
    def showContact(self):

        # Display Contacts
        User.displayList(self)
        # Get User Input 
        inp = int(input("\nWhich contact # do you wish to see? "))
        inp = getValidInt(inp)
        if inp <= len(self.contactList) and inp > 0:
            print(self.contactList[inp - 1])
        
        else: 
            print("Invalid Input")
        # End showContact()

    # Change Contact Information
    def changeContact(self):

        # Ask which contact 
        User.displayList(self)

        contactNumber = (input("\nWhich contact # do you wish to edit? "))
        contactNumber = getValidInt(contactNumber)

        if int(contactNumber) <= len(self.contactList) and int(contactNumber) > 0:  
            # Get User Input 
            inp = input("\nDo you wish to change contact name, phone number or email? ")
            inp = getValidStr(inp)

            # Action based on input
            if inp == "Name" or inp == "name":
                Contact.setName(self.contactList[contactNumber- 1], input("Enter new name: "))
                print("Done")
            elif inp == "Number" or inp == "number":
                Contact.setNumber(self.contactList[contactNumber- 1], input("Enter new phone number: "))
                print("Done")
            elif inp == "Email" or inp == "email":
                Contact.setEmail(self.contactList[contactNumber- 1], input("Enter new email: "))
                print("Done")
            else:
                print("\nInvalid input")
        
        else:
            print("\nCOntact does not exist")
        # End changeContact()
 
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

# currentUser global variable
currentUser = None

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
            User.displayList(currentUser)
        elif selection == "2":
            User.addNewContact(currentUser)
        elif selection == "3":
            User.deleteContact(currentUser)
        elif selection == "4":
            User.searchContacts(currentUser)
        elif selection == "5":
            User.showContact(currentUser)
        elif selection == "6":
            User.changeContact(currentUser)
        elif selection == "7":
            print("\nGoodbye")
            loop = False
            sys.exit()
        else:
            print("\nInvalid menu selection")
   
# Login and Signup
def login():
    global currentUser
    username = input("Enter your username: ")
    username = getValidStr(username)

    for i in range(len(users)):
        if users[i - 1].username == username:
            currentUser = users[i - 1]
            main()
        
    else:
        print("Username not registered please select signup to register a new user")
        # Call Login Menu Selection
        getLoginMenuSelection()

def signup():
    # object to be appended
    inp = input("Enter a new username: ")
    inp = getValidStr(inp)
    
    # appending username
    users.append(User(inp, []))
    print("Done")
    getLoginMenuSelection()
    
# Create Initial Contacts
users.append(User("Advi", [(Contact("Colin", "780-123-4567", "colinveldkamp6@gmail.com")),
(Contact("Advi", "780-163-9527", "adviislam34@gmail.com")),
(Contact("Robert", "780-191-6799", "roberto9@gmail.com")),
(Contact("Kim", "780-232-2145", "kimberlyy04@yahoo.com")),
(Contact("Riyana", "780-857-1093", "ririyana7@gmail.com")),]))

users.append(User("Colin", [(Contact("Darrell", "780-909-0022", "darellderrick0@yahoo.com")),
(Contact("Mohamed", "780-289-2034", "momoabdelrahman1@gmail.com")),
(Contact("William", "780-745-5954", "willywilliam90@gmail.com")),
(Contact("Jaehoon", "780-289-2418", "jaejit892@gmail.com")),
(Contact("Julie", "780-366-0595", "heyjuliee00@gmail.com"))]))

# Login or Signup Menu
def getLoginMenuSelection():
    print("\nDo you wish to login or sign up?")
    print("1: Login")
    print("2: Signup")

    inp = input("Enter option 1 or option 2: ")
    inp = getValidInt(inp)

    if inp == 1:
        login()
    
    elif inp == 2:
        signup()

# Call Login Menu Selection
getLoginMenuSelection()

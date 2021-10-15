# Create Contacts List
contactList = []

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
contactList.append(Contact("Colin", "780-123-4567", "colinveldkamp6@gmail.com"))
contactList.append(Contact("Advi", "780-163-9527", "adviislam34@gmail.com"))
contactList.append(Contact("Robert", "780-191-6799", "roberto9@gmail.com"))
contactList.append(Contact("Kim", "780-232-2145", "kimberlyy04@yahoo.com"))
contactList.append(Contact("Riyana", "780-857-1093", "ririyana7@gmail.com"))
contactList.append(Contact("Darrell", "780-909-0022", "darellderrick0@yahoo.com"))
contactList.append(Contact("Mohamed", "780-289-2034", "momoabdelrahman1@gmail.com"))
contactList.append(Contact("William", "780-745-5954", "willywilliam90@gmail.com"))
contactList.append(Contact("Jaehoon", "780-289-2418", "jaejit892@gmail.com"))
contactList.append(Contact("Julia", "780-366-0595", "heyjuliee00@gmail.com"))

# Clear Console Function
import os
def clear(): os.system('cls')

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

# Add New Contact
def addNewContact():

    clear()
    contactList.append(Contact(input("Enter name: "), input("Enter number: "), input("Enter email: ")))
    # End addNewContact()

# Delete Contact
def deleteContact():

    clear()
    displayList()
    contactNumber = int(input("Which contact # do you wish to delete? "))

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
    print("\nResults:")
    for i in range(len(contactList)):
        if contactList[i].name == inp or inp in contactList[i].name:
            found = True
            print(contactList[i].name)
    
    # Display message if no contacts found
    if found == False:
        print("No Contacts were found")
    # End searchContact()

# Show Contact Information
def showContact():

    # Display Contacts
    displayList()
    # Get User Input 
    inp = int(input("\nWhich contact do you wish to see? "))
    if inp <= len(contactList) and inp > 0:
        print(contactList[inp - 1])

    # End showContact()

# Change Contact Information
def changeContact():

    # Ask which contact 
    displayList()
    contactNumber = int(input("\nWhich contact do you wish to change? ")) 

    if contactNumber <= len(contactList) and contactNumber > 0:  
        # Get User Input 
        inp = input("\nDo you wish to change contact name, number or email? ")

        # Action based on input
        if inp == "Name" or inp == "name":
            Contact.setName(contactList[contactNumber- 1], input("Enter new name: "))
            print("Done")
        elif inp == "Number" or inp == "number":
            Contact.setNumber(contactList[contactNumber- 1], input("Enter new number: "))
            print("Done")
        elif inp == "Email" or inp == "email":
            Contact.setEmail(contactList[contactNumber- 1], input("Enter new email: "))
            print("Done")
        else:
            print("\nInvalid input")
    
    else:
        print("\nInvalid input")

    
# Call main() to start program
main()
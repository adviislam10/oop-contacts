# Create Contacts List
import os
contacts = []

# Contacts Class
class Contacts:
    def __init__(self, name, number, email):

        self.name = name
        self.number = number
        self.email = email
        contacts.append(name)

# Clear Console Function
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
            searchContact()
        elif selection == "5":
            showContact()
        elif selection == "6":
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
    print("6: Exit")

    return input("Enter a menu option: ")
    # End getMenuSelection()

# Display contacts
def displayList():

    clear()
    print("Contacts: ")
    for i in contacts:
        print(i)
    # End displayList()

# Add new contact
def addNewContact():

    clear()
    Contacts(input("Enter name: "), input("Enter number: "), input("Enter email: "))
    displayList()
    # End addNewContact()

# Delete Contact
def deleteContact():

    clear()
    displayList()
    contactNumber = int(input("Which contact # do you wish to delete? "))
    contacts.pop(contactNumber)
    # End deleteContact()

# Search for Contact
def searchContact():
    pass

# Show Contact Information
def showContact():
    pass


# Create Initial Contacts
contacts[0] = Contacts("Colin", "780-123-4567", "colinveldkamp6@gmail.com")
contacts[1] = Contacts("Advi", "780-163-9527", "adviislam34@gmail.com")

# Call main() to start program
main()

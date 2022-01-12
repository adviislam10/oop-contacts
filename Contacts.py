from User import*

contactList = []

# Clear Console Function
import os
def clear(): os.system('cls')

# Contact Class
class Contact:
    # Initialize method
    def __init__(self, name, number, email):

        self.name = name
        self.number = number
        self.email = email

    # Get as Dict
    def asDict(self ): 
        return {
            "name": self.name,
            "number": self.number,
            "email": self.email
        }

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

# Call main() to start program
main
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

# Create Initial Contacts
contactList.append(Contact("Colin", "780-123-4567", "colinveldkamp6@gmail.com"))
contactList.append(Contact("Advi", "780-163-9527", "adviislam34@gmail.com"))
contactList.append(Contact("Robert", "780-191-6799", "roberto9@gmail.com"))
contactList.append(Contact("Kim", "780-232-2145", "kimberlyy04@gmail.com"))

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
            searchContact()
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

# Display contacts1
def displayList():

    clear()
    print("Contacts: ")
    for i in range(len(contactList)):
        print(str(i + 1) + ".", contactList[i].name)

# Add new contact
def addNewContact():

    clear()
    Contact(input("Enter name: "), input("Enter number: "), input("Enter email: "))
    # End addNewContact()

# Delete Contact
def deleteContact():

    clear()
    displayList()
    contactNumber = int(input("Which contact # do you wish to delete? "))
    contactList.pop(contactNumber - 1)
    # End deleteContact()

# Search for Contact
def searchContact():
    pass
    # End searchContact()

# Show Contact Information
def showContact():

    # Display Contacts
    displayList()
    # Get User Input 
    inp = int(input("Which contact do you wish to see? "))
    if inp < len(contactList) and inp > 0:
        print(contactList[inp - 1])
    # End showContact()

# Change Contact Information
def changeContact():
    pass

# Call main() to start program
main()
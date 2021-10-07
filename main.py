contacts = []

class Contacts:
    def __init__(self, name, number, email):

        self.name = name
        self.number = number
        self.email = email
        contacts.append(name)


def displayList():
        for i in contacts:
            print(i)

def addNewContact(answer):
    if answer == "yes":
        Contacts(input("Enter name: "), input( "Enter number: "), input("Enter email: "))
        displayList()

    if answer == 'no':
        print("Understood")
        

c1 = Contacts("Colin", "780-123-4567", "colinveldkamp6@gmail.com")
c2 = Contacts("Advi", "780-163-9527", "adviislam34@gmail.com")
displayList()
addNewContact(input("Do you wish to add a new contact: "))
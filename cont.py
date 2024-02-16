#  contact book project
# store name ,phone number,eamil,address
# add contact
# view contact
# update contact
# delete contact
# userinterface

contact = {}

while True:
    choose = input("Enter the number to perform the activity\n 1.Add Contact\n 2.Update the Contact \n 3. Delete Contact \n 4. Search \n 5.display contact \n 6.Exit \n")

    if choose == '1':
        name = input("Enter the name : ")
        phone = int(input("Enter the Number : "))

        contact[name] = phone
        print("Contact added ")

    elif choose == '2':
        search = input("enter the name to search")
        if search in contact:
            NewNumber = input("Enter the new Number")
            contact[search] = NewNumber
            print("updated sucessfuly")
        else:
            print("No contact found!")
    elif choose == '3':
        search = input("enter the name to search")
        if search in contact:
            del contact[search]
            print("sucessfully deleted")
        else:
            print("No contact found!")
    elif choose == '4':
        search = input("enter the name to search")
        if search in contact:

            print(
                f'contact is present... name{search} number is {contact[search]}')
        else:
            print("No contact found!")
    elif choose == '5':
        

        for name, number in contact.items():
            print(f'Name:{name} , Number:{number}')
    elif choose == '6':
        ex = input("confirm you really want to exit y/n")
        if ex == "y" or ex == "Y":
            break
        else:
            continue
    else:
        print("please the correct option")
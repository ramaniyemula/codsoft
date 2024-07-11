contact = {}


def display_contact():
    print("Contact List:")
    if not contact:
        print("Empty contact book")
    else:
        print("Name\t\tPhone Number\t\tEmail\t\t\t\tAddress")
        for name, details in contact.items():
            print("{}\t\t{}\t\t{}\t\t{}".format(name, details['phone'], details['email'], details['address']))
    print()


while True:
    print("Welcome to Contact Book")
    print("1. Add new contact")
    print("2. Search contact")
    print("3. Display contact list")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter the contact name: ")
        phone = input("Enter the mobile number: ")
        email = input("Enter the email address: ")
        address = input("Enter the address: ")
        contact[name] = {'phone': phone, 'email': email, 'address': address}
        print("Contact added successfully.\n")

    elif choice == 2:
        search_name = input("Enter the contact name to search: ")
        if search_name in contact:
            details = contact[search_name]
            print("Contact details:")
            print("Name:", search_name)
            print("Phone Number:", details['phone'])
            print("Email:", details['email'])
            print("Address:", details['address'])
        else:
            print("Name not found in contact book.\n")

    elif choice == 3:
        display_contact()

    elif choice == 4:
        edit_contact = input("Enter the contact name to edit: ")
        if edit_contact in contact:
            phone = input("Enter new mobile number: ")
            email = input("Enter new email address: ")
            address = input("Enter new address: ")
            contact[edit_contact] = {'phone': phone, 'email': email, 'address': address}
            print("Contact updated successfully.\n")
            display_contact()
        else:
            print("Name not found in contact book.\n")

    elif choice == 5:
        del_contact = input("Enter the contact name to delete: ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact? (y/n): ")
            if confirm.lower() == 'y':
                contact.pop(del_contact)
                print("Contact deleted successfully.\n")
            else:
                print("Deletion canceled.\n")
            display_contact()
        else:
            print("Name not found in contact book.\n")

    elif choice == 6:
        print("Thank you for using Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.\n")



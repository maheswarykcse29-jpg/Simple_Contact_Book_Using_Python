contacts = []
while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contact = (name, phone)
        contacts.append(contact)  
        print("Contact added successfully")
    elif choice == 2:
        print("Contact List:")
        for c in contacts:
            print("Name:", c[0], "Phone:", c[1])
    elif choice == 3:
        search = input("Enter name to search: ")
        found = False
        for c in contacts:
            if c[0] == search:
                print("Found:", c)
                found = True
        if not found:
            print("Contact not found")
    elif choice == 4:
        print("Exiting Contact Book")
        break
    else:
        print("Invalid choice")

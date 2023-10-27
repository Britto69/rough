#Develop a contact management program where users can add, edit,  delete and search contact details using a dictionary.The menu options would facilitatethese actions.
contacts = {}

def add_contact():
    name = input("Enter the name: ").strip().title()
    mobile = input("Enter the mobile number: ")
    address = input("Enter the address: ")
    
    contact = {
        "name":name,
        "mobile": mobile,
        "address": address,
    }
    
    contacts[name] = contact
    print(f"Contact for {name} has been added.")

def edit_contact():
    name = input("Enter the name to edit: ").strip().title()
    
    if name in contacts:
        new_mobile = input(f"Enter new mobile number for {name}: ")
        new_address = input(f"Enter new address for {name}: ")
        
        contact = contacts[name]
        contact["mobile"] = new_mobile
        contact["address"] = new_address
        
        print(f"Contact for {name} has been updated.")
    else:
        print(f"Contact {name} not found.")

def delete_contact():
    name = input("Enter the name to delete: ").strip().title()
    
    if name in contacts:
        contacts.pop(name)
        print(f"Contact for {name} has been deleted.")
    else:
        print(f"Contact {name} not found.")

def search_contact():
    name = input("Enter the name to search: ").strip().title()
    
    if name in contacts:
        contact = contacts[name]
        print(f"Name: {name}")
        print(f"Mobile: {contact['mobile']}")
        print(f"Address: {contact['address']}")
    else:
        print(f"Contact {name} not found.")

def display_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("List of Contacts:")
        for name, contact in contacts.items():
            print(f"Name: {name}")
            print(f"Mobile: {contact['mobile']}")
            print(f"Address: {contact['address']}")
            print("-" * 20)

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Display Contacts")
    print("6. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        edit_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")



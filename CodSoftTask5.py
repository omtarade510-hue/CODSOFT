# CONTACT BOOK

'''Contact Information: Store name, phone number, email, and address for each contact.
Add Contact: Allow users to add new contacts with their details.
View Contact List: Display a list of all saved contacts with names and phone numbers.
Search Contact: Implement a search function to find contacts by name or phone number.
Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.
User Interface: Design a user-friendly interface for easy interaction.'''


contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return

    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()


def search_contact():
    search = input("Enter Name or Phone to search: ")

    found = False
    for contact in contacts:
        if search.lower() in contact["name"].lower() or search in contact["phone"]:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True

    if not found:
        print("Contact not found.\n")


def update_contact():
    phone = input("Enter Phone Number of contact to update: ")

    for contact in contacts:
        if contact["phone"] == phone:
            print("Enter new details (leave blank to keep old value)")
            name = input("New Name: ")
            email = input("New Email: ")
            address = input("New Address: ")

            if name:
                contact["name"] = name
            if email:
                contact["email"] = email
            if address:
                contact["address"] = address

            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")


def delete_contact():
    phone = input("Enter Phone Number of contact to delete: ")

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")


def menu():
    while True:
        print("===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thank you for using Contact Book!")
            break
        else:
            print("Invalid choice. Try again.\n")


menu()

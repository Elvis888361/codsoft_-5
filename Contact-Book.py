# Initialize an empty dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")

    contacts[name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully!")

# Function to view the contact list
def view_contacts():
    if not contacts:
        print("Your contact list is empty.")
    else:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone Number: {details['phone_number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print()

# Function to search for a contact
def search_contact(query):
    results = []
    for name, details in contacts.items():
        if query.lower() in name.lower() or query in details['phone_number']:
            results.append((name, details))

    if not results:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for name, details in results:
            print(f"Name: {name}")
            print(f"Phone Number: {details['phone_number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print()

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        print("Enter new contact details:")
        add_contact()
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found in your list.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found in your list.")

# Main loop
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        query = input("Enter a name or phone number to search: ")
        search_contact(query)
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6).")

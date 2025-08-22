# Simple Contacts Console App

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    with open("contacts.txt", "a") as file:  # append mode
        file.write(f"{name}:{phone}\n")
    print("✅ Contact saved successfully!\n")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.\n")
            else:
                print("\n📒 Saved Contacts:")
                for line in contacts:
                    name, phone = line.strip().split(":")
                    print(f"👤 {name} -> 📞 {phone}")
                print()
    except FileNotFoundError:
        print("No contacts file found. Add some contacts first!\n")

def main():
    while True:
        print("=== Contact Manager ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice, please try again.\n")

# Run the app
main()

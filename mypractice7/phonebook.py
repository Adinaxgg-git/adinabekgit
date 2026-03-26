from connect import get_connection
import csv

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv():
    conn = get_connection()
    cur = conn.cursor()
    with open("contacts.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row["name"], row["phone"])
            )
    conn.commit()
    cur.close()
    conn.close()
    print("Contacts imported from CSV.")

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()
    print(f"Contact {name} added.")

def query_contacts():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def search_by_name():
    name = input("Enter name to search: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", ('%' + name + '%',))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def update_contact():
    name = input("Enter name of contact to update: ")
    new_phone = input("Enter new phone number: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET phone=%s WHERE name=%s", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()
    print(f"{name}'s phone updated.")

def delete_contact():
    name = input("Enter name of contact to delete: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
    conn.commit()
    cur.close()
    conn.close()
    print(f"{name} deleted.")

if __name__ == "__main__":
    create_table()
    while True:
        print("\nPhoneBook Menu:")
        print("1. Import contacts from CSV")
        print("2. Add contact")
        print("3. Show all contacts")
        print("4. Search by name")
        print("5. Update contact")
        print("6. Delete contact")
        print("0. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            insert_from_csv()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            query_contacts()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            delete_contact()
        elif choice == "0":
            break
        else:
            print("Invalid option.")
from connect import create_connection
import csv

conn = create_connection()
cur = conn.cursor()

#create table

cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
);
""")
conn.commit()


#insert manual


def insert_user():
    name = input("Name: ")
    phone = input("Phone: ")

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Added!")


#insert csv


def insert_csv():
    with open("contacts.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )
    conn.commit()
    print("CSV imported!")


#search


def search():
    text = input("Name prefix: ")

    cur.execute(
        "SELECT * FROM contacts WHERE name LIKE %s",
        (text + "%",)
    )

    for row in cur.fetchall():
        print(row)


#update


def update():
    name = input("Name: ")
    phone = input("New phone: ")

    cur.execute(
        "UPDATE contacts SET phone=%s WHERE name=%s",
        (phone, name)
    )
    conn.commit()
    print("Updated!")


#delete 


def delete():
    name = input("Name to delete: ")

    cur.execute(
        "DELETE FROM contacts WHERE name=%s",
        (name,)
    )
    conn.commit()
    print("Deleted!")

def search_by_phone():
    text = input("Phone prefix: ")

    cur.execute(
        "SELECT * FROM contacts WHERE phone LIKE %s",
        (text + "%",)
    )

    for row in cur.fetchall():
        print(row)

while True:
    print("\n PHONEBOOK MENU:")
    print("1. Add contact")
    print("2. Import CSV")
    print("3. Update contact")
    print("4. Search contact")
    print("5. Delete contact")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        insert_user()
    elif choice == "2":
        insert_csv()
    elif choice == "3":
        update()
    elif choice == "4":
        search()
    elif choice == "5":
        delete()
    elif choice == "6":
        search_by_phone()
    elif choice == "7":
        break
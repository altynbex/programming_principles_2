from connect import create_connection

conn = create_connection()
cur = conn.cursor()

# CALL SEARCH FUNCTION
def search():
    text = input("Search: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (text,))
    print(cur.fetchall())

# CALL PAGINATION FUNCTION
def paginate():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    print(cur.fetchall())

# UPSERT
def upsert():
    name = input("Name: ")
    phone = input("Phone: ")

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()

# DELETE
def delete():
    value = input("Name or phone: ")

    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()

# MENU
while True:
    print("1. Search")
    print("2. Paginate")
    print("3. Upsert")
    print("4. Delete")
    print("5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        search()
    elif choice == "2":
        paginate()
    elif choice == "3":
        upsert()
    elif choice == "4":
        delete()
    elif choice == "5":
        break

cur.close()
conn.close()
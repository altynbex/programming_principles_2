# phonebook.py
import json
from connect import get_connection

# ---------------- BASIC HELPERS ----------------

def get_contact_by_name(cur, name):
    cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
    return cur.fetchone()

# ---------------- CONSOLE FEATURES ----------------

def filter_by_group():
    group = input("Enter group: ")
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name ILIKE %s
    """, (f"%{group}%",))

    for row in cur.fetchall():
        print(row)

    conn.close()


def search_by_email():
    query = input("Search email: ")
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts WHERE email ILIKE %s", (f"%{query}%",))

    for row in cur.fetchall():
        print(row)

    conn.close()


def sorted_contacts():
    field = input("Sort by (name/birthday/date): ")

    mapping = {
        "name": "name",
        "birthday": "birthday",
        "date": "created_at"
    }

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM contacts ORDER BY {mapping.get(field, 'name')}")

    for row in cur.fetchall():
        print(row)

    conn.close()


def pagination():
    conn = get_connection()
    cur = conn.cursor()

    page = 0
    limit = 5

    while True:
        cur.execute("SELECT * FROM get_contacts_page(%s, %s)", (limit, page))
        rows = cur.fetchall()

        if not rows:
            print("No more data")

        for r in rows:
            print(r)

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            page += 1
        elif cmd == "prev" and page > 0:
            page -= 1
        elif cmd == "quit":
            break

    conn.close()

# ---------------- JSON EXPORT ----------------

def export_json():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
    """)

    contacts = []

    for c in cur.fetchall():
        cid = c[0]

        cur.execute("SELECT phone, type FROM phones WHERE contact_id = %s", (cid,))
        phones = cur.fetchall()

        contacts.append({
            "name": c[1],
            "email": c[2],
            "birthday": str(c[3]),
            "group": c[4],
            "phones": [{"number": p[0], "type": p[1]} for p in phones]
        })

    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

    conn.close()
    print("Exported!")

# ---------------- JSON IMPORT ----------------

def import_json():
    conn = get_connection()
    cur = conn.cursor()

    with open("contacts.json") as f:
        data = json.load(f)

    for contact in data:
        name = contact["name"]

        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists. skip/overwrite: ")
            if choice == "skip":
                continue
            else:
                cur.execute("DELETE FROM contacts WHERE name=%s", (name,))

        cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT DO NOTHING", (contact["group"],))
        cur.execute("SELECT id FROM groups WHERE name=%s", (contact["group"],))
        group_id = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO contacts(name,email,birthday,group_id)
            VALUES(%s,%s,%s,%s) RETURNING id
        """, (name, contact["email"], contact["birthday"], group_id))

        cid = cur.fetchone()[0]

        for p in contact["phones"]:
            cur.execute("INSERT INTO phones(contact_id,phone,type) VALUES(%s,%s,%s)",
                        (cid, p["number"], p["type"]))

    conn.commit()
    conn.close()
    print("Imported!")

# ---------------- MAIN MENU ----------------

def menu():
    while True:
        print("Phonebook Menu:")
        print("1. Filter by group")
        print("2. Search by email")
        print("3. Sort")
        print("4. Pagination")
        print("5. Export JSON")
        print("6. Import JSON")
        print("7. Exit")
        print("Choice:")
        choice = input()

        if choice == "1":
            filter_by_group()
        elif choice == "2":
            search_by_email()
        elif choice == "3":
            sorted_contacts()
        elif choice == "4": 
            pagination()
        elif choice == "5": 
            export_json()
        elif choice == "6": 
            import_json()
        elif choice == "7": 
            break


if __name__ == "__main__":
    menu()

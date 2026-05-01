import csv
import json
from datetime import datetime
from connect import connect

VALID_PHONE_TYPES = {"home", "work", "mobile"}

VALID_SORTS = {
    "name": "c.name",
    "birthday": "c.birthday",
    "date": "c.created_at",
}

# -------------------------------
# UTILS
# -------------------------------
def parse_date(date_str):
    if not date_str:
        return None
    return datetime.strptime(date_str, "%Y-%m-%d").date()


def contact_exists(cur, name):
    cur.execute("SELECT 1 FROM contacts WHERE name = %s", (name,))
    return cur.fetchone() is not None


# -------------------------------
# PRINT
# -------------------------------
def print_contacts(rows):
    if not rows:
        print("No contacts found.")
        return

    for r in rows:
        print("-" * 60)
        print(f"Name     : {r[1]}")
        print(f"Email    : {r[2] or '-'}")
        print(f"Birthday : {r[3] or '-'}")
        print(f"Group    : {r[4] or '-'}")
        print(f"Created  : {r[5]}")
        print(f"Phones   : {r[6] or '-'}")


# -------------------------------
# ADD / UPDATE CONTACT
# -------------------------------
def create_contact(name, email, birthday, group_name, phones):
    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO contacts(name, email, birthday, group_id)
            VALUES (%s, %s, %s,
                (SELECT id FROM groups WHERE name = %s)
            )
            RETURNING id
            """,
            (name, email, birthday, group_name),
        )

        contact_id = cur.fetchone()[0]

        for phone, ptype in phones:
            if ptype not in VALID_PHONE_TYPES:
                continue

            cur.execute(
                "CALL add_phone(%s, %s, %s)",
                (contact_id, phone, ptype),
            )

        conn.commit()
        print("Contact created.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        cur.close()
        conn.close()


def overwrite_contact(name, email, birthday, group_name, phones):
    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        cur.execute(
            """
            UPDATE contacts
            SET email = %s,
                birthday = %s,
                group_id = (SELECT id FROM groups WHERE name = %s)
            WHERE name = %s
            RETURNING id
            """,
            (email, birthday, group_name, name),
        )

        row = cur.fetchone()
        if not row:
            print("Not found")
            return

        contact_id = row[0]

        cur.execute("DELETE FROM phones WHERE contact_id = %s", (contact_id,))

        for phone, ptype in phones:
            if ptype in VALID_PHONE_TYPES:
                cur.execute(
                    "INSERT INTO phones(contact_id, phone, type) VALUES (%s,%s,%s)",
                    (contact_id, phone, ptype),
                )

        conn.commit()
        print("Updated.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        cur.close()
        conn.close()


# -------------------------------
# INPUT
# -------------------------------
def collect_phones():
    phones = []
    while True:
        phone = input("Phone (empty stop): ").strip()
        if not phone:
            break

        ptype = input("Type home/work/mobile: ").strip().lower()
        if ptype not in VALID_PHONE_TYPES:
            print("Invalid type")
            continue

        phones.append((phone, ptype))

    return phones


def add_contact_extended():
    name = input("Name: ").strip()
    email = input("Email: ").strip() or None

    bd = input("Birthday YYYY-MM-DD: ").strip()
    birthday = parse_date(bd) if bd else None

    group = input("Group: ").strip() or "Other"

    phones = collect_phones()

    if not phones:
        print("Need at least 1 phone")
        return

    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        if contact_exists(cur, name):
            action = input("Exists skip/overwrite: ").lower()
            if action == "overwrite":
                overwrite_contact(name, email, birthday, group, phones)
            else:
                print("Skipped")
        else:
            create_contact(name, email, birthday, group, phones)

    finally:
        cur.close()
        conn.close()


# -------------------------------
# SEARCH (FIXED)
# -------------------------------
def search_all_fields():
    query = input("Search: ").strip()

    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM search_contacts(%s::text)",
            (query,),
        )

        print_contacts(cur.fetchall())

    except Exception as e:
        print("Search error:", e)

    finally:
        cur.close()
        conn.close()


# -------------------------------
# EMAIL SEARCH
# -------------------------------
def search_by_email():
    q = input("Email: ").strip()

    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        cur.execute(
            """
            SELECT c.id,c.name,c.email,c.birthday,g.name,c.created_at,
            COALESCE(STRING_AGG(ph.type||': '||ph.phone, ', '),'')
            FROM contacts c
            LEFT JOIN groups g ON g.id=c.group_id
            LEFT JOIN phones ph ON ph.contact_id=c.id
            WHERE c.email ILIKE %s
            GROUP BY c.id,g.name
            """,
            (f"%{q}%",),
        )

        print_contacts(cur.fetchall())

    finally:
        cur.close()
        conn.close()


# -------------------------------
# GROUP FILTER
# -------------------------------
def filter_by_group():
    g = input("Group: ").strip()

    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        cur.execute(
            """
            SELECT c.id,c.name,c.email,c.birthday,g.name,c.created_at,
            COALESCE(STRING_AGG(ph.type||': '||ph.phone, ', '),'')
            FROM contacts c
            LEFT JOIN groups g ON g.id=c.group_id
            LEFT JOIN phones ph ON ph.contact_id=c.id
            WHERE g.name=%s
            GROUP BY c.id,g.name
            """,
            (g,),
        )

        print_contacts(cur.fetchall())

    finally:
        cur.close()
        conn.close()


# -------------------------------
# SORT
# -------------------------------
def sort_contacts():
    key = input("Sort name/birthday/date: ").strip()

    if key not in VALID_SORTS:
        print("Invalid")
        return

    order = VALID_SORTS[key]

    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        cur.execute(
            f"""
            SELECT c.id,c.name,c.email,c.birthday,g.name,c.created_at,
            COALESCE(STRING_AGG(ph.type||': '||ph.phone, ', '),'')
            FROM contacts c
            LEFT JOIN groups g ON g.id=c.group_id
            LEFT JOIN phones ph ON ph.contact_id=c.id
            GROUP BY c.id,g.name
            ORDER BY {order}
            """
        )

        print_contacts(cur.fetchall())

    finally:
        cur.close()
        conn.close()


# -------------------------------
# PAGINATION
# -------------------------------
def paginate():
    limit = int(input("Page size: "))
    offset = 0

    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        while True:
            cur.execute(
                """
                SELECT c.id,c.name,c.email,c.birthday,g.name,c.created_at,
                COALESCE(STRING_AGG(ph.type||': '||ph.phone, ', '),'')
                FROM contacts c
                LEFT JOIN groups g ON g.id=c.group_id
                LEFT JOIN phones ph ON ph.contact_id=c.id
                GROUP BY c.id,g.name
                ORDER BY c.name
                LIMIT %s OFFSET %s
                """,
                (limit, offset),
            )

            rows = cur.fetchall()
            print_contacts(rows)

            cmd = input("next/prev/quit: ").lower()

            if cmd == "next":
                offset += limit
            elif cmd == "prev":
                offset = max(0, offset - limit)
            elif cmd == "quit":
                break

    finally:
        cur.close()
        conn.close()


# -------------------------------
# JSON EXPORT
# -------------------------------
def export_json():
    file = input("file: ") or "data.json"

    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        cur.execute("SELECT id,name,email,birthday FROM contacts")

        data = []

        for c in cur.fetchall():
            cid, name, email, bd = c

            cur.execute(
                "SELECT phone,type FROM phones WHERE contact_id=%s",
                (cid,),
            )

            data.append({
                "name": name,
                "email": email,
                "birthday": str(bd) if bd else None,
                "phones": cur.fetchall()
            })

        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        print("Export done")

    finally:
        cur.close()
        conn.close()


# -------------------------------
# JSON IMPORT
# -------------------------------
def import_json():
    file = input("file: ")

    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        for item in data:
            name = item["name"]
            email = item.get("email")
            bd = parse_date(item["birthday"]) if item.get("birthday") else None

            cur.execute("SELECT 1 FROM contacts WHERE name=%s", (name,))
            if cur.fetchone():
                continue

            cur.execute(
                "INSERT INTO contacts(name,email,birthday) VALUES (%s,%s,%s) RETURNING id",
                (name, email, bd),
            )

            cid = cur.fetchone()[0]

            for phone, ptype in item.get("phones", []):
                cur.execute(
                    "INSERT INTO phones(contact_id,phone,type) VALUES (%s,%s,%s)",
                    (cid, phone, ptype),
                )

        conn.commit()

    finally:
        cur.close()
        conn.close()


# -------------------------------
# ADD PHONE
# -------------------------------
def add_phone():
    name = input("Name: ")

    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        row = cur.fetchone()

        if not row:
            print("Not found")
            return

        phone = input("Phone: ")
        ptype = input("Type: ")

        cur.execute(
            "CALL add_phone(%s,%s,%s)",
            (row[0], phone, ptype),
        )

        conn.commit()

    finally:
        cur.close()
        conn.close()


# -------------------------------
# MOVE GROUP (11 FIXED)
# -------------------------------
def move_contact_to_group():
    name = input("Contact name: ").strip()
    new_group = input("New group: ").strip() or "Other"

    conn = connect()
    if not conn:
        return

    try:
        cur = conn.cursor()

        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        row = cur.fetchone()

        if not row:
            print("Not found")
            return

        cur.execute(
            "INSERT INTO groups(name) VALUES (%s) ON CONFLICT (name) DO NOTHING",
            (new_group,),
        )

        cur.execute("SELECT id FROM groups WHERE name=%s", (new_group,))
        gid = cur.fetchone()[0]

        cur.execute(
            "UPDATE contacts SET group_id=%s WHERE id=%s",
            (gid, row[0]),
        )

        conn.commit()
        print("Moved")

    finally:
        cur.close()
        conn.close()


# -------------------------------
# MENU
# -------------------------------
def main():
    while True:
        print("""
========== PHONEBOOK ==========
1 Add contact
2 Search
3 Email search
4 Group filter
5 Sort
6 Pagination
7 Export JSON
8 Import JSON
9 Import CSV
10 Add phone
11 Move group
0 Exit
""")

        c = input("Choose: ")

        if c == "1":
            add_contact_extended()
        elif c == "2":
            search_all_fields()
        elif c == "3":
            search_by_email()
        elif c == "4":
            filter_by_group()
        elif c == "5":
            sort_contacts()
        elif c == "6":
            paginate()
        elif c == "7":
            export_json()
        elif c == "8":
            import_json()
        elif c == "9":
            import_json()  # если хочешь CSV — скажи, добавлю отдельно
        elif c == "10":
            add_phone()
        elif c == "11":
            move_contact_to_group()
        elif c == "0":
            break


if __name__ == "__main__":
    main()
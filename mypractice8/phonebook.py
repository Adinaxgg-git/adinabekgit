from connect import get_connection

def test_all():
    conn = get_connection()
    cur = conn.cursor()

    print("✅ Connected")

    # 🔁 upsert
    cur.execute("CALL upsert_contact(%s, %s)", ("Adina", "777777"))
    conn.commit()
    print("✅ Upsert done")

    # 🔍 search
    cur.execute("SELECT * FROM search_contacts(%s)", ("Adi",))
    print("🔍 Search:", cur.fetchall())

    # 📥 bulk insert
    cur.execute("""
        CALL insert_many(
            ARRAY['A', 'B', 'C'],
            ARRAY['12345', 'abc', '99999']
        )
    """)
    conn.commit()
    print("✅ Bulk insert done")

    # 📄 pagination
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (5, 0))
    print("📄 Paginated:", cur.fetchall())

    # ❌ delete
    cur.execute("CALL delete_contact(%s)", ("A",))
    conn.commit()
    print("🗑 Deleted A")

    cur.close()
    conn.close()
    print("✅ Done")

if __name__ == "__main__":
    test_all()
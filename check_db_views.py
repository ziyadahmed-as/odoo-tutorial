import psycopg2

try:
    conn = psycopg2.connect("dbname='odoomanage' user='odoo' password='odoo' host='127.0.0.1' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT id, name, arch_db FROM ir_ui_view WHERE model='beltech.project'")
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, NAME: {row[1]}")
        print(row[2])
        print("-" * 50)
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")

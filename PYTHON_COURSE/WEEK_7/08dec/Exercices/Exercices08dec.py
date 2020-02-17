import sqlite3

try:
    connect = sqlite3.connect('public.db')
    cursor = connect.cursor()

    for row in req.fetchall():
        print(row[0])


except Exception as e:
    print("[ERROR]", e)
    connect.rollback()

finally:
    connect.close()
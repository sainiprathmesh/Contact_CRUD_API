import sqlite3

DB_PATH = './Contact_API.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'


def create_record_id():
    rec_id = 'CAPI_'
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('select * from records')
        rows = cur.fetchall()
        rec_id = rec_id + str(len(rows) + 1)
        return rec_id
    except Exception as e:
        print('Error: ', e)
        return None


def add_to_database(record_id, contact_name, contact_email_id, contact_number):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('insert into records(record_id, contact_name, contact_email_id, contact_number) values(?,?,?,?)',
                    (record_id, contact_name, contact_email_id, contact_number))
        conn.commit()
        return {"record_id": record_id, "contact_name": contact_name, "contact_email_id": contact_email_id,
                "contact_number": contact_number}
    except Exception as e:
        print('Error: ', e)
        return None


def get_all_items():
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('select * from records')
        rows = cur.fetchall()
        return {"count": len(rows), "items": rows}
    except Exception as e:
        print('Error: ', e)
        return None


print(get_all_items())

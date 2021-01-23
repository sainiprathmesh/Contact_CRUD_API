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


def add_to_database(record):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('insert into records(record_id, contact_name, contact_email_id, contact_number) values(?,?,?,?)',
                    record)
        conn.commit()
        return {"record": record}
    except Exception as e:
        print('Error: ', e)
        return None



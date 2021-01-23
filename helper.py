import sqlite3

DB_PATH = './Contact_API.db'


def pagination(page, json):
    start = ((page - 1) * 3)
    end = page * 3
    return json[start:end]


def add_to_database(contact_name, contact_email_id, contact_number):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        print("hi")
        cur.execute('insert into records(contact_name, contact_email_id, contact_number) values(?,?,?)',
                    (contact_name, contact_email_id, contact_number))
        conn.commit()
        cur.execute('select max(record_id) from records')
        rows = cur.fetchall()

        return {"record_id": rows[0][0], "contact_name": contact_name, "contact_email_id": contact_email_id,
                "contact_number": contact_number}
    except Exception as e:
        print('Error: ', e)
        return None


def get_all_records(page):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('select * from records')
        rows = cur.fetchall()
        return pagination(page, rows)
        # return {"count": len(rows), "items": rows}
    except Exception as e:
        print('Error: ', e)
        return None


def get_record_by_name(contact_name, page):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(f"select * from records where contact_name like '%{contact_name}%'")
        status = cur.fetchall()
        return pagination(page, status)
    except Exception as e:
        print('Error: ', e)
        return None


def get_record_by_mail(contact_email_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("select * from records where contact_email_id='%s'" % contact_email_id)
        status = cur.fetchall()
        print(status)
        return status
    except Exception as e:
        print('Error: ', e)
        return None


def update_record(record_id, new_contact_name, new_contact_email, new_contact_number):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('update records set contact_name=?,contact_email_id=?,contact_number=? where record_id=?',
                    (new_contact_name, new_contact_email, new_contact_number, record_id))
        conn.commit()
        return {record_id: new_contact_name}
    except Exception as e:
        print('Error: ', e)
        return None


def delete_record(record_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('delete from records where record_id=?', (record_id,))
        conn.commit()
        if cur:
            return {'record_id': record_id}
    except Exception as e:
        print('Error: ', e)
        return None

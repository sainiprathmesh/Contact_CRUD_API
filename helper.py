import sqlite3

DB_PATH = './Contact_API.db'


# for pagination of 10 data per page
def pagination(page, json):
    start = ((page - 1) * 10)
    end = page * 10
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


# pass page number
def get_all_records(page):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('select * from records')
        rows = cur.fetchall()
        return pagination(page, rows)
    except Exception as e:
        print('Error: ', e)
        return None


# pass contact name as argument
def get_record_by_name(contact_name):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(f"select * from records where contact_name like '%{contact_name}%'")
        status = cur.fetchall()
        return status
    except Exception as e:
        print('Error: ', e)
        return None


# pass contact mail id as argument
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


# for update record enter record_id, new contact name, new contact email, new contact number
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


# for deleting the record pass record_id as argument.
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

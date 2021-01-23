import sqlite3

DB_PATH = './Contact_API.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'


def add_to_database(record):
    try:
        conn = sqlite3.connect(DB_PATH)

    except Exception as e:
        print('Error: ', e)
        return None

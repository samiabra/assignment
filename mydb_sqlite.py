from datetime import datetime
import sqlite3

connection = sqlite3.connect('assigment.db')
cursor = connection.cursor()


def create_table():
    cursor.execute('''create table if not exists URLS (
    timestamp_url text, url text, HTTP_status_code text, Headers text)''')


def insert_values(urls, status_code, headers):
    cursor.execute("INSERT INTO URLS (timestamp_url,url,HTTP_status_code, Headers) VALUES (?, ?, ?, ?)",
                       (str(datetime.now()),
                        str(urls), str(status_code
                                       ),
                        str(headers
                            )
                        ))
    connection.commit()


def get_values():
    cursor.execute("SELECT * FROM URLS")
    records = cursor.fetchall()
    return records

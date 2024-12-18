#!/usr/bin/python3
"""
Filter states:
Script that lists all states with a name
starting with N (upper N) from the database.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()

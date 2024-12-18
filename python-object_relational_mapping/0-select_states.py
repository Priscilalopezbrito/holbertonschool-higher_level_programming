#!/usr/bin/python3
"""
Get all states
MySQL database connection using Python
"""
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()

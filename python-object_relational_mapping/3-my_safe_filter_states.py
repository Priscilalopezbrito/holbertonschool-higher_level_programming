#!/usr/bin/python3

"""
SQL Injection...
"""

import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    state_search = sys.argv[4]

    cursor = db.cursor()
    query = """SELECT * FROM states WHERE name = %s ORDER BY id ASC"""
    cursor.execute(query, (state_search,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()

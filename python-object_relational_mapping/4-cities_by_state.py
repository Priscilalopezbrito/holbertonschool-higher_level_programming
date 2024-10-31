#!/usr/bin/python3

"""
Cities by states
"""

import sys
import MySQLdb

if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )

    cursor = db.cursor()
    cursor.execute(
        """
        SELECT cities.id, cities.name, states.name"
        FROM cities 
        Join states on cities.id = states.id
        ORDER BY cities.id ASC;
        """
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()

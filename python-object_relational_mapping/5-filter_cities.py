#!/usr/bin/python3

"""
All cities by state
"""

import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    state_name = sys.argv[4]

    cursor = db.cursor()
    query = """
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """
    cursor.execute(query, (state_name,))
    print(", ".join([row[1] for row in rows]))

    cursor.close()
    db.close()

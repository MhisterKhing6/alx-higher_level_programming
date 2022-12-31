#!/usr/bin/env python3
""" Select all states from cities using MySQLdb"""

import sys
import MySQLdb

# create a connection to database
connect = MySQLdb.connect(host='localhost', user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], port=3036)
#  get a cursor
cursor = connect.cursor()
cursor.execute('''SELECT * from states ORDER BY states.id ASC''')
rows = cursor.fetchall()
for row in rows:
    print(row)

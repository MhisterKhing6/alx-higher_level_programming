#!/usr/bin/python3

"""
    Python MySQLdb introduction
    Select all states from the states database
"""
if __name__ == '__main__':
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

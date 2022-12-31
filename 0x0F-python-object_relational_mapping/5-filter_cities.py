#!/usr/bin/python3

"""
    Python MySQLdb introduction
    Select all states from the states database
    where states name is equal to user inputs
"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    # create a connection to database
    connect = MySQLdb.connect(host='localhost', user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3], port=3036)
    #  get a cursor
    cursor = connect.cursor()
    cursor.execute('''
                   SELECT cities.name 
                   FROM cities inner join states 
                   ON states.id = cities.state_id AND states.name = BINARY %s
                   ''', (sys.argv[4], ))
    new = [x[0] for x in cursor.fetchall()]
    print(', '.join(new))

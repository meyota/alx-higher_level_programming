#!/usr/bin/python3

""""
    Ascript that lists all states from the database hbtn_0e_0_usa
    Username, password and database names are given as user args
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    data = cur.fetchall()
    for row in data:
        print (row)

    cur.close()
    db.close()

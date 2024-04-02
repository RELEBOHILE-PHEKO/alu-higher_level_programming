#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N' from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user, pwd, db = sys.argv[1:4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=pwd, db=db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()

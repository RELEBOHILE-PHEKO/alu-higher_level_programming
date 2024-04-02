#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, db_name = sys.argv[1:4]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()

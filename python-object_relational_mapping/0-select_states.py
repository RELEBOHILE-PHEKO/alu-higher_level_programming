#!/usr/bin/python3
"""
Script to list all states from the database 'hbtn_0e_0_usa'

This script connects to a MySQL server running on 'localhost' at port '3306'
and retrieves all rows from the 'states' table in the 'hbtn_0e_0_usa' database.
The results are sorted in ascending order by the 'id' column and displayed on
the console.

Usage:
    ./script.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: The username to connect to the MySQL server.
    mysql_password: The password associated with the MySQL username.
    database_name: The name of the MySQL database to connect to.
"""
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

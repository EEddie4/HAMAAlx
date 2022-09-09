#!/usr/bin/python3
import sys

if __name__ == "__main__":
    import MySQLdb
    if (len(sys.argv) == 5):
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=password,
            db=database,
            charset="utf8")
        cur = conn.cursor()
        sql = "SELECT name FROM cities WHERE state_id = "
        sql = sql + "(SELECT id FROM states WHERE name = "
        sql = sql + "'{}'".format(sys.argv[4]) + " LIMIT 1) ORDER BY id ASC"
        cur.execute(sql)
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close() 

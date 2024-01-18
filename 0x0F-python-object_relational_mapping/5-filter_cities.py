#!/usr/bin/python3
"""
script to list all states from hbtn_0e_0_usa that start with N
"""


if __name__ == "__main__":
    import MySQLdb
    import sqlalchemy
    from sys import argv

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute(
        "SELECT cities.name\
        FROM cities\
        JOIN states\
        ON cities.state_id=states.id\
        WHERE states.name= %s\
        ORDER BY cities.id", (argv[4],))
    rows = cur.fetchall()
    city_list = []
    for row in rows:
        city_list.append(row[0])
    print(*city_list, sep=', ')
    db.close()

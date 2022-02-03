import sqlite3

conn = sqlite3.connect(input())
cursor = conn.cursor()

minimal_invisibility = int(input())
property_name = input()

cursor.execute(f"SELECT name, {property_name} FROM demiguisse INNER JOIN "
               "places ON demiguisse.place_id = places.id "
               f"WHERE invisibility >= {minimal_invisibility} "
               "ORDER BY invisibility DESC, name")
records = cursor.fetchall()

for record in records:
    print(record[0], record[1])

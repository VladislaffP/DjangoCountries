import json
import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()
#cursor.execute('Create Table if not exists country ([id] INTEGER PRIMARY KEY, [country] CharField(100))')

traffic = json.load(open('countries.json'))
columns = ['country', 'languages']
for row in traffic:
    keys = tuple(row[c] for c in columns)
    #print(keys[0])
    #cursor.execute('select country from country')
    cursor.execute('insert into MainApp_country(country) values(?)', [keys[0]])
#    print(f'{row["name"]} data inserted Succefully')

connection.commit()
connection.close()
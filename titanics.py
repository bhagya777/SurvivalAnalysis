import sqlite3
import re
import zlib

conn = sqlite3.connect('titanics.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS TitanicSurvival ''')
cur.execute('''DROP TABLE IF EXISTS Survived ''')
cur.execute('''DROP TABLE IF EXISTS Sex ''')
cur.execute('''DROP TABLE IF EXISTS Age ''')
cur.execute('''DROP TABLE IF EXISTS Class ''')

cur.execute('''CREATE TABLE IF NOT EXISTS TitanicSurvival
    (id INTEGER PRIMARY KEY, name TEXT,survived_id TEXT,sex_id TEXT,age_id,class_id TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Survived
    (id INTEGER PRIMARY KEY,
     survived TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Sex
    (id INTEGER PRIMARY KEY, sex TEXT )''')
cur.execute('''CREATE TABLE IF NOT EXISTS Age
    (id INTEGER PRIMARY KEY, age )''')
cur.execute('''CREATE TABLE IF NOT EXISTS Class
    (id INTEGER PRIMARY KEY, class TEXT)''')

conn_1 = sqlite3.connect('file:titanic.db?mode=ro', uri=True)
cur_1 = conn_1.cursor()

allpassengers = list()
cur_1.execute('''SELECT field1 FROM TitanicSurvival''')
for passenger_row in cur_1 :
    passenger =passenger_row[0]
    if passenger is None : continue
    if passenger in allpassengers: continue
    allpassengers.append(passenger)
    cur.execute('''INSERT OR IGNORE INTO TitanicSurvival(name) VALUES (?)''',(name,))
conn.commit()
print("Loaded allpassengers",len(allpassengers))

cur_1.execute('''SELECT survived FROM TitanicSurvival''')
count = 0
for passenger_row in cur_1 :
    ss= passenger_row[0]
    if ss=='yes':
        count=count+1
    else:continue
    
print('no.of passengers survived',count)
    
#cur.execute(INSERT INTO titanics.TitanicSurvival SELECT * FROM titanics.TitanicSurvival)
#cur_1.execute('''SELECT field1  from TitanicSurvival''')
#for namep in curr_1:
#cur.execute('''INSERT OR IGNORE INTO TitanicSurvival )

import sqlite3

conn = sqlite3.connect('file:titanic.db?mode=rw', uri=True)
cur = conn.cursor()

#Creating tables in database
cur.execute('''DROP TABLE IF EXISTS SurvivedSex''')
cur.execute('''CREATE TABLE IF NOT EXISTS SurvivedSex(people TEXT, male INTEGER, female INTEGER)''')

cur.execute('''DROP TABLE IF EXISTS SurvivedClass''')
cur.execute('''CREATE TABLE IF NOT EXISTS SurvivedClass(people TEXT, first INTEGER, second INTEGER, third INTEGER,
            firstm INTEGER,secondm INTEGER,thirdm INTEGER,firstf INTEGER,secondf INTEGER,thirdf INTEGER)''')

cur.execute('''DROP TABLE IF EXISTS SurvivedAgeclass''')
cur.execute('''CREATE TABLE IF NOT EXISTS SurvivedAgeclass(people TEXT,young INTEGER,adult INTEGER,aged INTEGER)''')

#Counting in various scenarios
allpassengers = list()
cur.execute('''SELECT field1 FROM TitanicSurvival''')
for passenger_row in cur :
    passenger =passenger_row[0]
    if passenger is None : continue
    if passenger in allpassengers: continue
    allpassengers.append(passenger)
    
print("Loaded allpassengers",len(allpassengers))

cur.execute('''SELECT field1,survived,sex FROM TitanicSurvival''')
count = 0
countm=0
for passenger_row in cur :
    ss= passenger_row[1]
    ssex=passenger_row[2]
    if ss == 'yes' :
        count=count+1
        if ssex=='male':
            countm=countm+1
conn.commit()
print('no. of passengers survived',count)
countd=len(allpassengers)-count
print('no. of passengers died',countd)
print('no. of male passengers survived',countm)

#above can be done by sql command as follows
#cur.execute('''SELECT field1 FROM TitanicSurvival WHERE survived='yes' AND sex='male' ''')
#countm=cur.fetchall()
#print('no.of passengers survived',len(countm))

cur.execute('''SELECT field1 FROM TitanicSurvival WHERE survived='yes' AND sex='female' ''')
countf=cur.fetchall()
countff=len(countf)
print('no.of female passengers survived',countff)

cur.execute('''SELECT field1 FROM TitanicSurvival WHERE survived='no' AND sex='male' ''')
countmns=cur.fetchall()
countmnss=len(countmns)
print('no.of male passengers died',countmnss)

cur.execute('''SELECT field1 FROM TitanicSurvival WHERE survived='no' AND sex='female' ''')
countfns=cur.fetchall()
countfnss=len(countfns)
print('no.of female passengers died',countfnss)

m1=0
cur.execute('''SELECT * FROM TitanicSurvival WHERE survived='yes' AND passengerClass='1st' ''')
firsts=cur.fetchall()
for x in firsts:
    s=x[2]
    if s=='male':
        m1=m1+1
    conn.commit()
first_survived=len(firsts)

m2=0
cur.execute('''SELECT * FROM TitanicSurvival WHERE survived='yes' AND passengerClass='2nd' ''')
seconds=cur.fetchall()
for x in seconds:
    s=x[2]
    if s=='male':
        m2=m2+1
    conn.commit()
second_survived=len(seconds)

m3=0
cur.execute('''SELECT * FROM TitanicSurvival WHERE survived='yes' AND passengerClass='3rd' ''')
thirds=cur.fetchall()
for x in thirds:
    s=x[2]
    if s=='male':
        m3=m3+1
    conn.commit()
third_survived=len(thirds)

m4=0
cur.execute('''SELECT * FROM TitanicSurvival WHERE survived='no' AND passengerClass='1st' ''')
firstd=cur.fetchall()
for x in firstd:
    s=x[2]
    if s=='male':
        m4=m4+1
    conn.commit()
first_died=len(firstd)

m5=0
cur.execute('''SELECT * FROM TitanicSurvival WHERE survived='no' AND passengerClass='2nd' ''')
secondd=cur.fetchall()
for x in secondd:
    s=x[2]
    if s=='male':
        m5=m5+1
    conn.commit()
second_died=len(secondd)

m6=0
cur.execute('''SELECT * FROM TitanicSurvival WHERE survived='no' AND passengerClass='3rd' ''')
thirdd=cur.fetchall()
for x in thirdd:
    s=x[2]
    if s=='male':
        m6=m6+1
    conn.commit()
third_died=len(thirdd)

count_young=0
count_adult=0
count_aged=0
cur.execute('''SELECT * FROM TitanicSurvival WHERE survived='yes' ''')
sages=cur.fetchall()
for sage in sages:
    age=sage[3]
    if age=='NA':continue
    elif float(age)<18:
        count_young=count_young+1
    elif float(age)<60:
        count_adult=count_adult+1
    else:
        count_aged=count_aged+1

count_young_died=0
count_adult_died=0
count_aged_died=0
cur.execute('''SELECT * FROM TitanicSurvival WHERE survived='no' ''')
dages=cur.fetchall()
for dage in dages:
    age=dage[3]
    if age=='NA':continue
    elif float(age)<18:
        count_young_died=count_young_died+1
    elif float(age)<60:
        count_adult_died=count_adult_died+1
    else:
        count_aged_died=count_aged_died+1

#printing all the counts
print('total 1st class',first_survived+first_died)
print('total 2nd class',second_survived+second_died)
print('total 3rd class',third_survived+third_died)
print('no.of first class survived',first_survived)
print('no.of second class survived',second_survived)
print('no.of third class survived',third_survived)
print('no.of first class died',first_died)
print('no.of second class died',second_died)
print('no.of third class died',third_died)
print('male first survived',m1)
print('male second survived',m2)
print('male third survived',m3)
print('female first survived',first_survived-m1)
print('female second survived',second_survived-m2)
print('female third survived',third_survived-m3)
print('male first died',m4)
print('male second died',m5)
print('male third died',m6)
print('female first died',first_died-m4)
print('female second died',second_died-m5)
print('female third died',third_died-m6)
print('young,adult,aged count survived',count_young,count_adult,count_aged)
print('doesnt know age but survived',count-(count_young+count_adult+count_aged))
print('young,adult,aged count died',count_young_died,count_adult_died,count_aged_died)
print('doesnt know age but died',countd-(count_young_died+count_adult_died+count_aged_died))

#Inserting data into the tables created
cur.execute(f'''INSERT OR IGNORE INTO SurvivedSex (people,male,female) VALUES (?,?,?)''',('survived',countm,countff))
cur.execute(f'''INSERT OR IGNORE INTO SurvivedSex (people,male,female) VALUES (?,?,?)''',('died',countmnss,countfnss))
cur.execute(f'''INSERT OR IGNORE INTO SurvivedClass (people,first,second,third,firstm,secondm,thirdm,firstf,secondf,thirdf) VALUES (?,?,?,?,?,?,?,?,?,?)''',
            ('survived',first_survived,second_survived,third_survived,m1,m2,m3,first_survived-m1,second_survived-m2,third_survived-m3))
cur.execute(f'''INSERT OR IGNORE INTO SurvivedClass (people,first,second,third,firstm,secondm,thirdm,firstf,secondf,thirdf) VALUES (?,?,?,?,?,?,?,?,?,?)''',
            ('died',first_died,second_died,third_died,m4,m5,m6,first_died-m4,second_died-m5,third_died-m6))

cur.execute(f'''INSERT OR IGNORE INTO SurvivedAgeclass (people,young,adult,aged) VALUES (?,?,?,?)''',('survived',count_young,count_adult,count_aged))
cur.execute(f'''INSERT OR IGNORE INTO SurvivedAgeclass (people,young,adult,aged) VALUES (?,?,?,?)''',('died',count_young_died,count_adult_died,count_aged_died))
conn.commit()

cur.close()






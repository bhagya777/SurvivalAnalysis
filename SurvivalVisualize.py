import sqlite3
import matplotlib.pyplot as p
import numpy as np

conn = sqlite3.connect('file:titanic.db?mode=ro', uri=True)
cur = conn.cursor()

try:
    #taking data from a table from database
    cur.execute('SELECT people,male,female FROM SurvivedSex')
    results=cur.fetchall()
    passengers=[result[0] for result in results]
    male=[result[1] for result in results]
    female = [result[2] for result in results]

    #Plotting graph
    fig,ax=p.subplots()
    x=range(len(passengers))
    width=0.35
    ax.bar([i-width/2 for i in x],male,width,label='male')
    ax.bar([i+width/2 for i in x],female,width,label='female')
    ax.set_xticks(x)
    ax.set_xticklabels(passengers)
    ax.set_title('male, female, class survival')
    ax.set_xlabel('survival status')
    ax.set_ylabel('count')

    ax.legend()
    p.show()

except sqlite3.Error as e:
    print('Error',e)

try:
    cur.execute('SELECT * FROM SurvivedClass')
    results=cur.fetchall()
    passengers=[result[0] for result in results]
    first=[result[1] for result in results]
    second = [result[2] for result in results]
    third = [result[3] for result in results]

    fig,ax=p.subplots()
    x=np.arange(len(passengers))
    width=0.25
    ax.bar(x-width,first,width,label='first class')
    ax.bar(x,second,width,label='second class')
    ax.bar(x+width,third,width,label='third class')
    ax.set_xticks(x)
    ax.set_xticklabels(passengers)
    ax.set_title(' class survival')
    ax.set_xlabel('survival status')
    ax.set_ylabel('count')

    ax.legend()
    p.show()

except sqlite3.Error as e:
    print('Error',e)

try:
    cur.execute('SELECT * FROM SurvivedAgeclass')
    results=cur.fetchall()
    passengers=[result[0] for result in results]
    young=[result[1] for result in results]
    adult = [result[2] for result in results]
    aged = [result[3] for result in results]

    fig,ax=p.subplots()
    x=np.arange(len(passengers))
    width=0.25
    ax.bar(x-width,young,width,label='young')
    ax.bar(x,adult,width,label='adult')
    ax.bar(x+width,aged,width,label='aged')
    ax.set_xticks(x)
    ax.set_xticklabels(passengers)
    ax.set_title(' AgeClass survival')
    ax.set_xlabel('survival status')
    ax.set_ylabel('count')

    ax.legend()
    p.show()

except sqlite3.Error as e:
    print('Error',e)
conn.close()
import sqlite3
import matplotlib.pyplot as p
import numpy as np

conn = sqlite3.connect('file:titanic.db?mode=ro', uri=True)
cur = conn.cursor()

#first graph-plotting survival status w.r.t. sex
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

except sqlite3.Error as e:
    print('Error',e)

#second graph-plotting survival status w.r.t. class
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

except sqlite3.Error as e:
    print('Error',e)

#third graph-plotting survival status w.r.t. age class
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

except sqlite3.Error as e:
    print('Error',e)


#fourth graph (stacked grouped)-plotting survival status w.r.t. class and sex
try:
    cur.execute('SELECT * FROM SurvivedClass')
    results = cur.fetchall()
    passengers = [result[0] for result in results]
    firstm = [result[4] for result in results]
    secondm = [result[5] for result in results]
    thirdm = [result[6] for result in results]
    firstf = [result[7] for result in results]
    secondf = [result[8] for result in results]
    thirdf = [result[9] for result in results]

    fig, ax = p.subplots()
    x = np.arange(len(passengers))
    width = 0.25
    ax.bar(x - width,firstm, width, label='first class male', bottom=0)
    ax.bar(x, secondm, width, label='second class male', bottom=0)
    ax.bar(x + width, thirdm, width, label='third class male', bottom=0)
    ax.bar(x - width, firstf, width, label='first class female', bottom=firstm)
    ax.bar(x, secondf, width, label='second class female', bottom=secondm)
    ax.bar(x + width,thirdf, width, label='third class female', bottom=thirdm)
    ax.set_xticks(x)
    ax.set_xticklabels(passengers)
    ax.set_title(' class survival status w.r.t. sex')
    ax.set_xlabel('survival status')
    ax.set_ylabel('count')

    ax.legend()

except sqlite3.Error as e:
    print('Error', e)

#fifth graph (stacked grouped)-plotting survival status w.r.t. class and age class
try:
    cur.execute('SELECT * FROM SurvivedAgeclass')
    results = cur.fetchall()
    passengers = [result[0] for result in results]
    young1 = [result[4] for result in results]
    young2 = [result[5] for result in results]
    young3 = [result[6] for result in results]
    adult1 = [result[7] for result in results]
    adult2 = [result[8] for result in results]
    adult3 = [result[9] for result in results]
    aged1 = [result[10] for result in results]
    aged2 = [result[11] for result in results]
    aged3 = [result[12] for result in results]

    #making separate list to put in bottom object as it can't take integer values
    young_adult_survived_1 = young1[0]+adult1[0]
    young_adult_survived_2 = young2[0] + adult2[0]
    young_adult_survived_3 = young3[0] + adult3[0]
    young_adult_died_1 = young1[1] + adult1[1]
    young_adult_died_2 = young2[1] + adult2[1]
    young_adult_died_3 = young3[1] + adult3[1]
    young_adult_1=[young_adult_survived_1,young_adult_died_1]
    young_adult_2 = [young_adult_survived_2, young_adult_died_2]
    young_adult_3 = [young_adult_survived_3, young_adult_died_3]

    fig, ax = p.subplots()
    x = np.arange(len(passengers))
    width = 0.25
    ax.bar(x - width, young1, width, label='first class young', bottom=0)
    ax.bar(x, young2, width, label='second class young', bottom=0)
    ax.bar(x + width, young3, width, label='third class young', bottom=0)
    ax.bar(x - width, adult1, width, label='first class adult', bottom=young1)
    ax.bar(x, adult2, width, label='second class adult', bottom=young2)
    ax.bar(x + width, adult3, width, label='third class adult', bottom=young3)
    ax.bar(x - width, aged1, width, label='first class aged', bottom=young_adult_1)
    ax.bar(x, aged2, width, label='second class aged', bottom=young_adult_2)
    ax.bar(x + width, aged3, width, label='third class aged', bottom=young_adult_3)
    ax.set_xticks(x)
    ax.set_xticklabels(passengers)
    ax.set_title(' class survival status w.r.t. age class')
    ax.set_xlabel('survival status')
    ax.set_ylabel('count')

    ax.legend()

except sqlite3.Error as e:
    print('Error', e)

#sixth graph giving probability distribution in percentage
try:
    cur.execute('SELECT * FROM Probability')
    results = cur.fetchall()
    y = [result[0] for result in results]
    x = [result[1] for result in results]
    p.figure(figsize=(13,7))
    p.barh(y,x)
    p.ylabel('event')
    p.xlabel('probability percentage')
    p.title('Probability distribution  of survival')

except sqlite3.Error as e:
    print('Error', e)

p.show()
conn.close()
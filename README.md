Analyzing Survival data from the accident using python and sqlite3 and vizualizing the data using Matplotlib library and Numpy.

Note : The program is written in Python 3.10

The data of survival from titanic accident is given in file-'TitanicSurvival.csv'.
You should install the SQLite browser to view and modify the databases from:

http://sqlitebrowser.org/

The first step is to import data from .csv file into SQLite browser. You can do it directly by creating a new database('titanic.db') in browser and by using import option in the SQLite browser.
file->import-> Table from CSV file

The second step is to analyze data and getting inputs for creating various tables in database for visualization. The code is given in 'SurvivalAnalyze.py' file. You will get some output like this after running file:
output:
Loaded allpassengers 1309
no. of passengers survived 500
no. of passengers died 809
no. of male passengers survived 161
no.of female passengers survived 339...

And you can open 'titanic.db' file in SQLite browser. It will give you 4 new tables which are created in this step.
tables- SurvivedSex, SurvivedClass, SurvivedAgeclass, Probability

![p1](https://github.com/bhagya777/SurvivalAnalysis/assets/139783534/88e7f5f3-c1d0-4c9f-a0f8-fee67ecbc2a4)
![p2](https://github.com/bhagya777/SurvivalAnalysis/assets/139783534/8d61a2da-9e84-4006-8d94-6e2412e2d946)
![p3](https://github.com/bhagya777/SurvivalAnalysis/assets/139783534/29345a13-01bc-485d-8fb5-4cc9f3284bb7)
![p4](https://github.com/bhagya777/SurvivalAnalysis/assets/139783534/2247ae93-8f09-4b93-b87a-e5d6eabd916a)

Before moving to the third step, you should install 'matplotlib' and 'numpy' packages in python. 
commands-
pip install matplotlib
pip install matplotlib

The third step is to visualize data from the tables created in step two. The code is given in 'SurvivalVisualize,py' file. Run the code to get six graphs.
First graph gives visualization of the data from 'SurvivedSex' table. It gives the numbers of males and females; survived and died.
Second graph gives visualization of the data from 'SurvivedClass' table. It gives the numbers survived and died people from the first, second and third passenger class.
Third graph gives visualization of the data from 'SurvivedAgeclass' table. It gives the numbers of survived and died people from different age groups namely young, adult and aged.
Fourth graph gives visualization of the data from 'SurvivedClass' table. It gives the numbers survived and died males and females from the first, second and third passenger class.
Fifth graph gives visualization of the data from 'SurvivedAgeclass' table. It gives the numbers of survived and died people from different age groups namely young, adult and aged in first, second and third class.
Sixth graph gives visualization of the data from 'Probability' table. It gives the probabilities of survival in different events.



![ssf](https://github.com/bhagya777/SurvivalAnalysis/assets/139783534/dd1036b6-b579-4c59-a9a5-0a55033110b7)






















import pandas as pd
import numpy as np
import random
random.seed(5)
import datetime
import string
import os
os.getcwd()
os.chdir(r'C:\Users\dudul\OneDrive\Documents\Dudu\Programming\Py4Econ\Introduction_Python\3_Dataframe\data')
df = pd.read_excel("data.xlsx") # //

######################### Task 1 #########################
## Question 1:
df1 = []
for index, row in df.iterrows():
    if row["age"]> 25:
        if row["gender"] =="F":
            df1.append(row)
df1 = pd.DataFrame(df1,columns=df.columns)
print(df1)
df1.to_csv(r'C:\Users\dudul\OneDrive\Documents\Dudu\Programming\Py4Econ\Homework\Female_25.csv',encoding='utf-8-sig')

## Question 2:
df2 = []
for index, row in df.iterrows():
    if row["age"]< 23 and row["gender"] !="F":
            df2.append(row)
df2 = pd.DataFrame(df2,columns=df.columns)
print(df2)
df2.to_csv(r'C:\Users\dudul\OneDrive\Documents\Dudu\Programming\Py4Econ\Homework\Men_23.json',encoding='utf-8-sig')


######################### Task 2 #########################
## Question 1:
df3 = np.random.randint(50,60, size=20)
print(df3)

df3_odd=[]
for i in df3:
     if np.mod(i,2) != 0:
          df3_odd.append(i)
print(df3_odd)

df3_odd = list(filter(lambda i: (i%2 != 0), df3))
print(df3_odd)

## Question 2:
df3_even=[]
for i in df3:
     if np.mod(i,2) == 0:
          df3_even.append(i)
print(df3_even)

df3_even = list(filter(lambda i: (i%2 == 0), df3))
print(df3_even)

## Question 3:
df3_x10 = list(map(lambda i: i * 10, df3))
print(df3_x10)

## Question 4:
df3_even2 = [i if np.mod(i,2)==0 else i-1 for i in df3]
print(df3_even2)






     

## Question 2:
df.loc[24:27,['firstName','age']]

## Question 3:
res = df.groupby(['gender']).agg({'age': ["mean","max","min"], 'salary': ["mean","max","min"]})
res.columns
len(res.columns)
res.columns = ['age_Mean','age_Max','age_Min','sal_Mean','sal_Max', 'sal_Min']
print(res)

## Question 4:
table = pd.pivot_table(df, values=['age','salary'], index=['gender'], \
                       aggfunc={'age':["mean","max","min"], 'salary':["mean","max","min"]})
print(table)
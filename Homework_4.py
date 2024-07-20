import pandas as pd
import numpy as np
import random
random.seed(5)
import datetime
import string
import os
os.getcwd()
os.chdir(r'D:\Programming\Py4Econ\Introduction_Python\3_Dataframe\data')
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
df1.to_csv(r'D:\Programming\Py4Econ\Homework\Female_25.csv',encoding='utf-8-sig')

## Question 2:
df2 = []
for index, row in df.iterrows():
    if row["age"]< 23 and row["gender"] !="F":
            df2.append(row)
df2 = pd.DataFrame(df2,columns=df.columns)
print(df2)
df2.to_csv(r'D:\Programming\Py4Econ\Homework\Men_23.json',encoding='utf-8-sig')


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

## Question 5:
for i in df3:
    if i <= 52:  #1
        print(i, "<= 52")
    elif 53 <= i <= 55:
        print(i, "53-55")
    elif 56 <= i <= 58:
        print(i, "56-58")
    else:
        print(i,  ">=59")

## Question 6:
i = 50    
while i < 60:
    if i < 59:
        print(i)
    else:
        pass
    i += 1

## Question 7:
i = 50    
while i < 55:
    print(i)
    i += 1
######################### Task 3 #########################
## Question 1:  
list1=df["firstName"]
list2=df["lastName"]   
for i in zip(list1, list2):
    print(i)

## Question 2:
for i, item in enumerate(list1):
    print(i, item)

for count, value in enumerate(list2):
    print(count, value)   
 
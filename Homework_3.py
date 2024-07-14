import pandas as pd
import numpy as np
import random
random.seed(5)
import datetime
import string
import os
os.getcwd()
os.chdir(r'D:\\Programming\\Py4Econ\Introduction_Python\3_Dataframe\data')
df = pd.read_excel("data.xlsx") # //

######## Task 1 #########
## Question 1:
num_rows=50-len(df['id'])
new_rows_data = []
max_id = df['id'].max()

for i in range(num_rows):
    max_id += 1
    new_row = [
        max_id,                                                                                     # Column 1
        str(df['firstName'].sample().values[0]),                                                    # Column 2
        str(df['lastName'].sample().values[0]),                                                     # Column 3
        f"{''.join(random.choices(string.ascii_uppercase, k=2))}{random.randint(0, 99):02d}",       # Column 4
        random.randint(18, 60),                                                                     # Column 5
        random.randint(1, 40),                                                                      # Column 6
        round(random.normalvariate(df['salary'].mean(), df['salary'].std()), 1),                    # Column 7
        random.choice(["F", "M"]),                                                                  # Column 8
        datetime.date.fromtimestamp(
            random.uniform(
                datetime.datetime.timestamp(datetime.datetime(1990, 1, 1, 0, 0, 0)),
                datetime.datetime.timestamp(datetime.datetime.now())
            )
        ).strftime("%Y-%m-%d %H:%M:%S"),                                                            # Column 9
        random.choice(["left", "right"]),                                                           # Column 10
    ]
    new_rows_data.append(new_row)
new_rows_df = pd.DataFrame(new_rows_data, columns=df.columns)
df = pd.concat([df, new_rows_df], ignore_index=True)
print(df)

## Question 2:
df1 = df[(df["age"]>27) & (df["gender"] != "M")]
len(df1)
df1.to_csv(r'D:\\Programming\\Py4Econ\Homework\new_data.csv',encoding='utf-8-sig')

## Question 3:
df2 = df[(df["age"]<23) & (df["gender"] == "M")]
len(df2)
df2.to_json(r'D:\\Programming\\Py4Econ\Homework\new_data.json', indent=4,force_ascii=False)

######## Task 2 #########
## Question 1:
df.iloc[16,2:5]

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
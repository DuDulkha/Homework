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

######## Task 1 #########
## Question 1:
num_rows=50-len(df['id'])
new_rows_data = []
for i in range(num_rows):
    new_row = [
        df['id'].max()+=1,                                                                                                                  # Column 1
        str(df['firstName'].sample().values[0]),                                                                                            # Column 2            
        str(df['lastName'].sample().values[0]),                                                                                             # Column 3
        f"{''.join(random.choices(string.ascii_uppercase, k=2))}{random.randint(0, 99):02d}",                                               # Column 4
        random.randint(18, 60),                                                                                                             # Column 5
        random.randint(1, 40),                                                                                                              # Column 6
        round(random.normalvariate(df['salary'].mean(), df['salary'].std()),1),                                                                      # Column 7    
        random.choice(["F", "M"]),                                                                                                          # Column 8
        datetime.date.fromtimestamp( \                                                                                                      
                random.uniform(datetime.datetime.timestamp(datetime.datetime.now()), \
                               datetime.datetime.timestamp(datetime.datetime(1990, 1, 1, 0, 0, 0)))).strftime("%Y-%m-%d %H:%M:%S"),         # Column 9 
        random.choice(["left", "right"]),                                                                                                   # Column 10    
        ]
    new_rows_data.append(new_row)
    new_rows_df = pd.DataFrame(new_rows_data, columns=df.columns)
df = pd.concat([df, new_rows_df], ignore_index=True)
df

## Question 2:
df1 = df[(df["age"]>27) & (df["gender"] != "M")]
len(df1)
df1.to_csv(r'C:\Users\dudul\OneDrive\Documents\Dudu\Programming\Py4Econ\Homework\new_data.csv',encoding='utf-8-sig')

## Question 3:

######## Task 2 #########
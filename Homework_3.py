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
num_rows=40
new_rows_data = []
for i in range(num_rows):
    new_row = [
        df['id'].max()+=1, 
        str(df['firstName'].sample().values[0]),
        str(df['lastName'].sample().values[0]), 
        f"{''.join(random.choices(string.ascii_uppercase, k=2))}{random.randint(0, 99):02d}",     
        random.randint(18, 60),
        random.randint(1, 40),
        random.normalvariate(df['salary'].mean(), df['salary'].std()),
        random.choice(["F", "M"]),
        datetime.date.fromtimestamp( \
                random.uniform(datetime.datetime.timestamp(datetime.datetime.now()), \
                               datetime.datetime.timestamp(datetime.datetime(1990, 1, 1, 0, 0, 0)))).strftime("%Y-%m-%d %H:%M:%S"), \
        random.choice(["left", "right"]),
        ]
    new_rows_data.append(new_row)
    new_rows_df = pd.DataFrame(new_rows_data, columns=df.columns)
df = pd.concat([df, new_rows_df], ignore_index=True)
df

## Question 1:

######## Task 2 #########
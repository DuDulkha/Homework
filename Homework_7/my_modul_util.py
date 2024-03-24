import pandas as pd
import numpy as np


def data_prep_IFS():
    ''' Function to keep only interested variables from IFS database '''
    df=pd.read_csv('C:/Users/dudul/OneDrive/Documents/Dudu/Programming/Py4Econ/Introduction_Python/7_Data_cleaning/data/clean/IFS_short.csv',low_memory=False)
   
    #Keep only depo rate
    df=df[df['Indicator Name']=="Financial, Interest Rates, Lending Rate, Percent per annum"]
    df.to_csv('C:/Users/dudul/OneDrive/Documents/Dudu/Programming/Py4Econ/Homework/Homework_7/Lending.csv')
    #df.head()

def data_prep():
    '''Clean data from IFS, save in all frequancies'''
    df=pd.read_csv('C:/Users/dudul/OneDrive/Documents/Dudu/Programming/Py4Econ/Homework/Homework_7/Lending.csv',low_memory=False)
    df = df.drop(df.columns[0], axis=1)
    df = pd.melt(df, id_vars=['Country Name', 'Indicator Name'], var_name='period', value_name='LendingRate')
    df.columns = ['country','indicator','period','i_lend']
    df.drop(['indicator'],axis=1,inplace=True)

    #Cleaning outliers
    df.loc[df['i_lend']=='B','i_lend']=np.nan
    df['i_lend'] = pd.to_numeric(df['i_lend'])

    # Based on observation, set value above 50 to 50
    df.loc[df['i_lend']>50,'i_lend']=50
  

    # Create separation by frequency
    dfm = df[df['period'].str.contains('M')]
    dfq = df[df['period'].str.contains('Q')]
    dfy = df[df['period'].str.len() == 4]

    # Create data column from period
    dfm['year']=dfm['period'].str[:4]
    dfm['month']=dfm['period'].str[5:]
    dfq['year']=dfq['period'].str[:4]
    dfq['quarter']=dfq['period'].str[5:]

    dfm.to_csv('C:/Users/dudul/OneDrive/Documents/Dudu/Programming/Py4Econ/Homework/Homework_7/dfm.csv')
    dfq.to_csv('C:/Users/dudul/OneDrive/Documents/Dudu/Programming/Py4Econ/Homework/Homework_7/dfq.csv')
    dfy.to_csv('C:/Users/dudul/OneDrive/Documents/Dudu/Programming/Py4Econ/Homework/Homework_7/dfy.csv')
import pandas as pd
import numpy as np
import sys
sys.path.append("C:\\Users\\dudul\\OneDrive\\Documents\\Dudu\\Programming\\Py4Econ\\Homework\Homework_7")
import plotly.express as px
import my_modul_util as ut

# prepare data
ut.data_prep_IFS()
ut.data_prep()


df=pd.read_csv('/Homework_7/dfm.csv')

#Because of IFS data structure, data is repeated 3 times, keep only one
max=df.groupby(['country','period'],as_index=False)['i_lend'].max()
df=max.merge(df.drop_duplicates(subset=['country','period']),on=['country','period'],how='left',suffixes=['_max',''])
df.drop(['i_lend'],axis=1,inplace=True)
df=df.rename(columns={'i_lend_max':'i_lend'})

# Find yearly average and deviation from yearly average for each country
df['i_lend_avg']=df.groupby(['country','year'])['i_lend'].transform('mean')
df['diff']=df['i_lend'] -df['i_lend_avg']

# Create a line plot for each country
fig = px.line(df, x='period', y='i_lend', color='country', markers=True, line_shape="linear")

# Plot
fig.update_layout(
    title="Monthly Lending Interest Rate by Country",
    xaxis_title="Date",
    yaxis_title="Value",
)

# Show the plot
fig.show()
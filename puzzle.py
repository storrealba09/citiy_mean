#Import Libraries
import pandas as pd
import plotly.express as px
#Format floats on panda
pd.options.display.float_format = '${:,.2f}'.format
#Read and uppercase dataframe
df = pd.read_csv('Data+for+TreefortBnB+Puzzle.csv')
df['City'] = df['City'].str.upper()

#Group Dataframe by City and aggregate the price mean
grouped = df.groupby('City').agg({'$ Price':['mean']}).reset_index()

#Visualization formatting and execution
grouped.columns = ['City', 'Mean']
fig = px.bar(grouped, x = ('City'), y= ('Mean'))
fig.show()

import pandas as pd
import plotly.express as px

pd.options.display.float_format = '${:,.2f}'.format
df = pd.read_csv('Data+for+TreefortBnB+Puzzle.csv')
df['City'] = df['City'].str.upper()

grouped = df.groupby('City').agg({'$ Price':['mean']}).reset_index()

grouped.columns = ['City', 'Mean']

print(grouped)

grouped.to_csv('./grouped.csv')

fig = px.bar(grouped, x = ('City'), y= ('Mean'))
fig.show()

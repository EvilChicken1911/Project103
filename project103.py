import pandas as pd 
import plotly.express as px

df = pd.read_csv('C:/Users/Jonathan Wu/OneDrive/Desktop/New folder/data2.csv')
fig = px.scatter(df, x = "date", y = "cases", color = "country")
fig.show()
from inspect import stack
import streamlit as st
import pandas as pd
from main import query_db
import matplotlib.pyplot as plt
import seaborn as sns
from connection.sql_utils import flg_country_agg

df_report=query_db()

st.title("Challenge - Python Data Engineer")
st.write("Hey, welcome to the Python Data Engineer code challenge. In this challenge, we are interested in seeing your knowledge about data management and visualizations. We will give you some data, and your final objective is to show us specific metrics in some chart visualizations.")
st.write("The visualizations that we are expecting are:")


# Plotting data on pie chart
# ----------------------------------------------------------------------------------
st.write("Hired by technology")
fig = plt.figure(figsize= (12,9))
dfg= df_report.groupby("technology")["status_candidate"].count()
plt.pie(list(dfg.values), labels =list(dfg.index), autopct='%.1f%%')
st.pyplot(fig)
# ----------------------------------------------------------------------------------





total = len(df_report)
# Plotting data on horizontal bar chart
# ----------------------------------------------------------------------------------
st.write("Hired by year")
fig = plt.figure(figsize= (10,4))
dfg= pd.DataFrame({'count':df_report.groupby(["year_application"]).size()}).reset_index()
dfg['percentage']=(dfg['count']/total)*100
ax=sns.barplot(x =dfg['count'],y=dfg['year_application'],data=dfg,orient='h')
for i, v in enumerate(dfg['percentage']):
    ax.text(v + 0, i + 0.15, str("{0:.2f}%".format(v)), color='black', fontsize=8)
st.pyplot(fig)
# ----------------------------------------------------------------------------------
#https://stackoverflow.com/questions/54687788/adding-percentage-values-onto-horizontal-bar-charts-in-matplotlib




# Plotting data on bar chart
# ----------------------------------------------------------------------------------
st.write("Hired by seniority")
fig = plt.figure(figsize= (10,5))
ax=sns.countplot(data=df_report,x='seniority',order=df_report['seniority'].value_counts().index)
for p in ax.patches:
    percentage = f'{100 * p.get_height() / total:.1f}%\n'
    x = p.get_x() + p.get_width() / 2
    y = p.get_height()
    ax.annotate(percentage, (x, y), ha='center', va='center')
plt.tight_layout()
st.pyplot(fig)
# ----------------------------------------------------------------------------------





# Plotting data on Hires by country over years
# ----------------------------------------------------------------------------------
filter_countries=['United States of America','Brazil','Colombia','Ecuador']

st.write("Hires by country over years")
fig = plt.figure(figsize= (10,5))
df_report['flg_country'] = df_report['country'].apply(lambda x: flg_country_agg(x))
df_report=df_report.loc[df_report['country'].isin(filter_countries)]
table=pd.crosstab(df_report['year_application'],df_report['flg_country'])
table=table.div(table.sum(1).astype(float), axis=0)
ax=table.plot.bar(stacked=True,legend=None).figure
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),ncol=4)
st.pyplot(ax)
# ----------------------------------------------------------------------------------
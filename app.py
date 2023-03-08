import streamlit as st
import pandas as pd


url_data='data/candidates.csv/'



st.write("Hola mundo")

q1 = 'SELECT * FROM db_candidates.tb_hired_report'

def read_df1():
  df1 = pd.read_sql_query(q1, connection)
  return df1

read_df1()  

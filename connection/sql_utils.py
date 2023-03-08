import pandas as pd
import pymysql
from connection.config import dic_sql_connection 
from connection.config import dic_tables_config 


def create_server_connection(database=False):
    connection = None
    try:
        if database:
            connection = pymysql.connect(
                host=dic_sql_connection['host'],
                user=dic_sql_connection['user'],
                password=dic_sql_connection['pass'],
                database=dic_tables_config['database'])
        else:
            connection = pymysql.connect(
                host=dic_sql_connection['host'],
                user=dic_sql_connection['user'],
                password=dic_sql_connection['pass'])
        print("MySQL Database connection successful")
        
        return connection
    except ConnectionError as exc:
        raise RuntimeError('Failed to create the connection to the server') from exc

    
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except ConnectionError as exc:
        raise RuntimeError('Failed to execute query') from exc



def execute_list_tuples_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except ConnectionError as exc:
        raise RuntimeError('Failed to execute query to insert into the created table') from exc



def read_table(connection, query):
    df=None
    try:
        df=pd.read_sql(query,connection)
        print("Query successful")
        return df
    except ConnectionError as exc:
        raise RuntimeError('Failed to read table') from exc
        


def flg_country_agg(country):
    if country in ['United States of America','Brazil','Colombia','Ecuador']:
        return country
    else:
        return 'Otros'











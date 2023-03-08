import pandas as pd
from connection.sql_utils import create_server_connection,execute_query,read_table,execute_list_tuples_query
from connection.config import dic_tables_config
from connection.config import CREATE_CANDIDATE_DATABASE,CREATE_CANDIDATES_TABLE,SQL_INSERT_CANDIDATE_TABLE,CREATE_REPORT_TABLE



def setup_db():
    url_data='data/candidates.csv/'
    df_candidates= pd.read_csv(url_data+"candidates.csv",sep=';')

    connection = create_server_connection(database=False)
    execute_query(connection, CREATE_CANDIDATE_DATABASE)
    
    connection = create_server_connection(database=True)
    execute_query(connection, CREATE_CANDIDATES_TABLE)

    val=list(df_candidates.itertuples(index=False,name=None))
    execute_list_tuples_query(connection, SQL_INSERT_CANDIDATE_TABLE, val)

    execute_query(connection, CREATE_REPORT_TABLE)


def query_db():
    connection = create_server_connection(database=True)
    query = f'SELECT*FROM {dic_tables_config["table_report"]} where status_candidate="Hired"'
    return read_table(connection, query)


if __name__ == "__main__":
    setup_db()
    print(query_db())
    







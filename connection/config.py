

dic_sql_connection ={}
dic_sql_connection["user"]='root'
dic_sql_connection["pass"]='root'
dic_sql_connection["host"]='localhost'


dic_tables_config={}
dic_tables_config["database"] = "db_candidates"
dic_tables_config["table_candidates"] = "tb_candidates"
dic_tables_config["table_report"] = "tb_hired_report"

CREATE_CANDIDATE_DATABASE = f'CREATE DATABASE {dic_tables_config["database"]}'

CREATE_CANDIDATES_TABLE = """
CREATE TABLE tb_candidates (
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  email VARCHAR(100),
  application_date DATE,
  country VARCHAR(150),
  yoe INT,
  seniority VARCHAR(100),
  technology VARCHAR(100),
  code_challenge_score INT,
  technical_interview_score INT
  );
 """

SQL_INSERT_CANDIDATE_TABLE = '''
INSERT INTO tb_candidates (first_name, last_name, email, application_date, country, yoe, seniority, technology,code_challenge_score,technical_interview_score) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''

CREATE_REPORT_TABLE='''
CREATE TABLE db_candidates.tb_hired_report
SELECT
technology,
seniority,
country,
year(application_date) as year_application,
case
when code_challenge_score>=7 and technical_interview_score>=7 THEN 'Hired'
else 'No Hired'
END
AS status_candidate
FROM db_candidates.tb_candidates
'''
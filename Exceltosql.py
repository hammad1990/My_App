import pandas as pd
import sqlite3
from pandas import DataFrame
import sqlalchemy
import urllib
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from openpyxl import load_workbook
import pyodbc

df = pd.read_excel('Z:/M.hammad/PY/My_Apps/Excel files/new of suppliers.xlsx')
##df = pd.read_excel('C:/Users/Mohammed_Hammad/Documents/my python files/My_Apps/Excel files/new of suppliers.xlsx')
##df = pd.read_excel('X:\M.HAMMAD\PY\My_Apps\Excel files\condensorToSQL.xlsx')
##df = pd.read_excel('X:\M.HAMMAD\PY\My_Apps\Excel files\supplyToSQL.xlsx')

# df.head()

connection_string = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};SERVER=PEEDM-HAMAD;DATABASE=usersDB;Trusted_Connection=yes;use_unicode=True;charset="utf8"')
##connection_string = urllib.parse.quote_plus('Driver={ODBC Driver 17 for SQL Server};Server=DESKTOP-SR0QC2P\SQLEXPRESS;Database=usersDB;Trusted_Connection=yes;use_unicode=True;charset="utf8"')
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = sqlalchemy.create_engine(connection_url)
df.to_sql('suppliers', con=engine, if_exists='replace',index=False)
##df.to_sql('Condensor', con=engine, if_exists='replace',index=False)
##df.to_sql('Supply', con=engine, if_exists='replace',index=False)

# print(df)

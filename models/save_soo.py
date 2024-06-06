import pyodbc
from config import Config


class save_soo:
    def __init__(self,username,country,Project_Name,encoded_string,rev):


      conn = pyodbc.connect(Config.DATABASE_PARAMETER)
      cursor=conn.cursor()
      cursor.execute("INSERT  INTO SOO (name,country,project_name,soo_file,rev) VALUES (?,?,?,?,?)",(username,country,Project_Name,encoded_string,rev))
      conn.commit()
      conn.close()

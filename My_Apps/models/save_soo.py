import pyodbc


class save_soo:
    def __init__(self,username,country,Project_Name,encoded_string,rev):


      conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=PEEDM-HAMAD;'
                      'Database=usersDB;'
                      'Trusted_Connection=yes;')
      cursor=conn.cursor()
      cursor.execute("INSERT  INTO SOO (name,country,project_name,soo_file,rev) VALUES (?,?,?,?,?)",(username,country,Project_Name,encoded_string,rev))
      conn.commit()
      conn.close()

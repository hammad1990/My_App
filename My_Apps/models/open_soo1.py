import pyodbc


class open_soo1:
    def __init__(self,project_name,rev):
      self.SOO=[]
      self.rev=[]
      
      self.project_name=project_name
      self.rev=rev
      self.x=0
      self.get_soo_from_sql1()

    def get_soo_from_sql1(self):
      # print("htht")

      conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=PEEDM-HAMAD;'
                      'Database=usersDB;'
                      'Trusted_Connection=yes;')

      cursor=conn.cursor()
      
      query=f"SELECT * FROM SOO where project_name='{self.project_name}' AND rev='{self.rev}'"
      rows=cursor.execute(query)
      rows=rows.fetchall()
      if rows:
        print("soo exist in SQL2121")
        for row in rows:
          
          self.SOO=rows[0][3]
          self.rev=rows[0][5]
          print(self.SOO)
          print(self.rev)
          
        self.x=5

        
        return (self.x)
        
          
      else:
        self.x=6
        return (self.x)

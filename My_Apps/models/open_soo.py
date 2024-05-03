import pyodbc
import webbrowser
import base64

class open_soo:
    def __init__(self,existing_project):
      self.SOO=[]
      self.existing_project=existing_project
      self.get_soo_from_sql()

    def get_soo_from_sql(self):
      # print("htht")

      conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=PEEDM-HAMAD;'
                      'Database=usersDB;'
                      'Trusted_Connection=yes;')

      cursor=conn.cursor()
      
      query=f"SELECT * FROM SOO where project_name='{self.existing_project}'"
      # print(self.existing_project)
      rows=cursor.execute(query)
      rows=rows.fetchall()
      if rows:
        print("soo exist in SQL")
        for row in rows:
          self.SOO=rows[0][4]
          # print(self.SOO)

        
        
        
        dencoded_string = base64.b64decode(self.SOO)
        with open(f"Z:/M.HAMMAD/SOO OUTPUT/{self.existing_project}.pdf", 'wb') as outfile:
          outfile.write(dencoded_string)
        chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))   
        browser='chrome'

        #### open new chrome tab
        webbrowser.get(browser).open_new_tab(f"Z:/M.HAMMAD/SOO OUTPUT/{self.existing_project}.pdf")
          
    

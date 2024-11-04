import pyodbc
import webbrowser
import base64
from config import Config

class open_soo:
    def __init__(self,existing_project,username):
      self.SOO=[]
      self.existing_project=existing_project
      self.username=username
      self.get_soo_from_sql()

    def get_soo_from_sql(self):
      # print("htht")

      conn = pyodbc.connect(Config.DATABASE_PARAMETER)

      cursor=conn.cursor()
      
      query=f"SELECT * FROM SOO where project_name='{self.existing_project}'"
      # print(self.existing_project)
      rows=cursor.execute(query)
      rows=rows.fetchall()
      if rows:
        print(self.username)
        print("soo exist in SQL")
        for row in rows:
          self.SOO=rows[0][4]
          # print(self.SOO)

        
        
        
        dencoded_string = base64.b64decode(self.SOO)
        ## now we create new PDF and write the SOO that we got from SQL inside it
        with open(Config.SOO_OUTPUT+f"{self.existing_project}.pdf", 'wb') as outfile:
          outfile.write(dencoded_string)
        chrome_path=Config.chrome_path
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))   
        browser='chrome'

        #### open new chrome tab
        webbrowser.get(browser).open_new_tab(Config.SOO_OUTPUT+f"{self.existing_project}.pdf")
          
    

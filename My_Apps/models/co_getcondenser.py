import pyodbc


class getCondenser:
    def __init__(self,co_cond_model,co_cond_qty,co_cond_vee,co_cond_speed,co_voltage):
      
      self.co_cond_model=co_cond_model
      self.co_cond_qty=co_cond_qty
      self.co_cond_vee=co_cond_vee
      self.co_cond_speed=co_cond_speed
      self.co_voltage=co_voltage

      self.get_condenser_from_sql()
     
      

    def get_condenser_from_sql(self):
      # print("htht")

      conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=PEEDM-HAMAD;'
                      'Database=usersDB;'
                      'Trusted_Connection=yes;')

      cursor=conn.cursor()
      query=f"SELECT * FROM Condenser where Model='{self.co_cond_model}' AND Volt='{self.co_voltage}'"
      rows=cursor.execute(query)
      rows=rows.fetchone()
      # print(rows)
      if rows:
        self.Brand=rows[0]
        self.Model=rows[1]
        self.HP=rows[3]
        self.Amp=rows[4]
        self.Cable=rows[5]
        self.Contactor=rows[6]
        self.Breaker=rows[7]
        # print(self.Brand)
        # print(self.Model)
        # print(self.HP)
        # print(self.Amp)
        # print(self.Cable)
        # print(self.Contactor)
        # print(self.Breaker)
        return (self.Brand,self.Model,self.HP,self.Amp,self.Cable,self.Contactor,self.Breaker)


      
          
          

          
          
          
          
      
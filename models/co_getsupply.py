import pyodbc


class getSupply:
    def __init__(self,co_fans_type,co_fans_hp_220,co_fansvfd_220,co_voltage):
      
      self.co_fans_type=co_fans_type
      self.co_fans_hp_220=co_fans_hp_220
      self.co_fansvfd_220=co_fansvfd_220
      self.co_voltage=co_voltage
      # print(self.co_fans_hp_220)
      self.get_supply_from_sql()
     
      

    def get_supply_from_sql(self):
      # print("htht")

      conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                    'Server=PEEDM-HAMAD;'
                    'Database=usersDB;'
                    'Trusted_Connection=yes;')

      cursor=conn.cursor()
      query=f"SELECT * FROM Supply where HP='{self.co_fans_hp_220}' AND Volt='{self.co_voltage}'"
      rows=cursor.execute(query)
      rows=rows.fetchone()
      # print(rows)
      if rows:
        # print(rows)
        self.Brand=rows[0]
        self.HP=rows[1]
        self.Amp=rows[4]
        self.Cable=rows[5]
        self.Vfd=rows[6]
        self.Breaker=rows[7]
        # print(self.Brand)
        # print(self.HP)
        # print(self.Amp)
        # print(self.Cable)
        # print(self.Vfd)
        # print(self.Breaker)
        return (self.Brand,self.HP,self.Amp,self.Cable,self.Vfd,self.Breaker)
      else:
            print("noooo")

if __name__=='__main__':
  S=getSupply(co_fans_type='Supply',co_fans_hp_220='15HP',co_fansvfd_220='ACH580‐01‐047A[RECN3013022]',co_voltage='208V-3-60Hz')
  print(S.Brand)

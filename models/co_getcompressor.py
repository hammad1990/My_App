import pyodbc
from config import Config

class getCompressor:
    def __init__(self,CompNo,brand,model,hp,volt,ambient):
      
      self.CompNo=CompNo
      self.brand=brand
      self.model=model
      self.hp=hp
      self.volt=volt
      self.ambient=ambient
      # print(self.brand,self.model,self.hp,self.volt,self.ambient)

      self.get_compressor_from_sql()
     
      

    def get_compressor_from_sql(self):
      # print("htht")

      conn = pyodbc.connect(Config.DATABASE_PARAMETER)

      cursor=conn.cursor()
      if self.model=="VZH035CJANB"  or self.model=="VZH044CJANB/M" or self.model=="VZH065CJANB" or self.model=="VZH088BJANA/I/P06" or self.model=="VZH088CJAN" or self.model=="VZH088AGANA" or self.model=="VZH117AGANA":
        query=f"SELECT * FROM Compressor where Brand='{self.brand}' AND Model='{self.model}' AND HP='{self.hp}'AND Volt='{self.volt}'"
        rows=cursor.execute(query)
        rows=rows.fetchone()
        # print(rows)
        if rows:
          self.Amp=rows[4]
          self.PT=rows[5]
          self.Cablein=rows[7]
          self.Cableout=rows[8]
          self.CB=rows[10]
          self.VC=rows[13]
          # print(self.CompNo)
          # print(self.Amp)
          # print(self.PT)
          # print(self.Cablein)
          # print(self.Cableout)
          # print(self.CB)
          # print(self.VC)
          return (self.model,self.hp,self.CompNo,self.Amp,self.PT,self.Cablein,self.Cableout,self.VC,self.CB)


      elif int(self.ambient)>=105:
      
        query=f"SELECT * FROM Compressor where Brand='{self.brand}' AND Model='{self.model}' AND HP='{self.hp}'AND Volt='{self.volt}'"
        rows=cursor.execute(query)
        
        rows=rows.fetchone()
        # print(rows)
        if rows:
          self.Amp=rows[4]
          self.PT=rows[5]
          self.Cable=rows[6]
          self.Contactor=rows[9]
          if int(self.hp)< 15:
            self.MMS=rows[11]
            print(self.Amp)
            return (self.model,self.hp,self.CompNo,self.Amp,self.PT,self.Cable,self.Contactor,self.MMS)
          else:
            self.Breaker=rows[10]
            print(self.Amp)
            return (self.model,self.hp,self.CompNo,self.Amp,self.PT,self.Cable,self.Contactor,self.Breaker)
          # print(self.CompNo)
            
          # print(self.PT)
          # print(self.Cable)
          # print(self.Contactor)
          # print(self.MMS)
          
          
        
      elif int(self.ambient)<105:
      
        query=f"SELECT * FROM Compressor where Brand='{self.brand}' AND Model='{self.model}' AND HP='{self.hp}'AND Volt='{self.volt}'"
        rows=cursor.execute(query)
        
        rows=rows.fetchone()
        # print(rows)
        if rows:
          self.Amp=rows[4]
          self.PT=rows[5]
          self.Cable=rows[6]
          self.Contactor=rows[9]
          if int(self.hp)< 15:
            self.MMS=rows[11]
            print(self.Amp)
            return (self.model,self.hp,self.CompNo,self.Amp,self.PT,self.Cable,self.Contactor,self.MMS)
          else:
            self.Breaker=rows[10]
            print(self.Amp)
            return (self.model,self.hp,self.CompNo,self.Amp,self.PT,self.Cable,self.Contactor,self.Breaker)
          # print(self.CompNo)
          # print(self.Amp)
          # print(self.PT)
          # print(self.Cable)
          # print(self.Contactor)
          # print(self.MMS)
         
            
          

          
          
          
          
      
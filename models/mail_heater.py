from datetime import datetime,date,timedelta,time
from flask import session
import win32com.client as win32



class mail_heater:
    def __init__(self,username,heatercap,volt,stage,totalkw):
      olApp=win32.Dispatch('outlook.Application')
      
      mailItem=olApp.CreateItem(0)
      mailItem.Subject=datetime.now().strftime('%#d %b %Y %H:%M')
      # mailItem.BodyFormat=1
      # mailItem.Body="fffffff"
      mailItem.To=session["email"]
      mailItem.CC="m-hammad@petra-eng.com.jo"
      # mailItem.Display()
      
      mailItem.BodyFormat=2
      self.username=username
      self.heatercap=heatercap
      self.volt=volt
      self.stage=stage
      self.totalkw=totalkw
      mailItem.HTMLBody=f"""<h2 style="margin-top: 5px;color: red;">Dear {self.username}</h2>
        <p>you asked for heaters :{self.heatercap}<br>
        volt={self.volt}<br>
        stages={self.stage}<br>
        </p>
        <p>the applicable heater capacity for above condition is:{self.totalkw}</p>
        <p>please make sure to use this value in the job order</p>
      """

    

      mailItem.Send()
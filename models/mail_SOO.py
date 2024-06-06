from datetime import datetime
from flask import session
import win32com.client as win32


class mail_SOO:
    def __init__(self,username,path):
        self.username=username
        self.path=path
      #### email the attachemnt
        olApp=win32.Dispatch('outlook.Application')
      # olNS=olApp.GetNameSpace('MAPI')
        mailItem=olApp.CreateItem(0)
        mailItem.Subject=datetime.now().strftime('%#d %b %Y %H:%M')
        # mailItem.BodyFormat=1
        # mailItem.Body="fffffff"
        mailItem.To=session["email"]
        mailItem.CC="m-hammad@petra-eng.com.jo"
        
        mailItem.BodyFormat=2
        mailItem.HTMLBody=f"""<h2 style="margin-top: 5px;color: red;">Dear {self.username}</h2>
            <p>please find attached SOO.</p>
  
          """

        mailItem.Attachments.Add(self.path)
        mailItem.Display()
        
        mailItem.Send()
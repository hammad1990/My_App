from datetime import datetime
from flask import session
import win32com.client as win32
# import smtplib


class mail_RFQ:
    def __init__(self,emails1,path,inquiry_number):
        self.emails1=emails1
        self.path=path
        self.inquiry_number=inquiry_number
        # print(self.emails1)
      #### email the attachemnt
        olApp=win32.Dispatch('outlook.Application')
        mailItem=olApp.CreateItem(0)
        mailItem.Subject=f"Inquiry No. {self.inquiry_number}"
        # mailItem.Recipients.Add(''.join(self.emails1))-----------this methid is not correct
        mailItem.To=";".join([i for i in self.emails1 if isinstance(self.emails1, list) == True])
        mailItem.CC="m-hammad@petra-eng.com.jo"
        mailItem.BodyFormat=2
        mailItem.HTMLBody=f"""<h2 style="margin-top: 5px;color: Black;">Dear Madam/Sir</h2>
            <p>You are kindly requested to send us your best price and delivery date for attached.</p><br>
                                  """
  
        mailItem.Attachments.Add(self.path)
        mailItem.Display(True)
        
        # mailItem.Send()
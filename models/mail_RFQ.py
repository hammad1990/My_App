from datetime import datetime
from flask import session
import win32com.client as win32
from flask_mail import Mail, Message
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
        mailItem.CC="m-hammad@petra-eng.com.jo;procurementm@petra-eng.com.jo;m-harfeel@petra-eng.com.jo;B-ali@petra-eng.com.jo;k-ganim@petra-eng.com.jo;s-alwhiedi@petra-eng.com.jo;s-eid@petra-eng.com.jo;m-alnobani@petra-eng.com.jo"
        # mailItem.CC="m-hammad@petra-eng.com.jo"
        mailItem.BodyFormat=2
        mailItem.HTMLBody=f"""<p style="margin-top: 5px;">Dear Madam/Sir</p>
            <p>You are kindly requested to send us your best price and delivery date for attached.</p><br>
            <p>Best Regards</p>
            <p>Procurement Department</p>
                                  """
  
        mailItem.Attachments.Add(self.path)
        # mailItem.Display(True)

        
        mailItem.Send()


        
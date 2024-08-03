from ast import Mod
from flask import Blueprint,render_template,request,send_file,session,redirect,flash
from numpy import concatenate
from fpdf import FPDF,HTMLMixin
import pyodbc
from datetime import datetime,time
from models.add_count import add_count
from models.read_inquiry import read_inquiry
import time
import base64
from models.mail_RFQ import mail_RFQ
import os.path 
import pandas as pd
from config import Config

# import os

RFQ=Blueprint("RFQ",__name__,template_folder='templates',static_folder='static')


class PDF(FPDF,HTMLMixin):

  
  def __init__(self,inquiry_number,No_of_items,petra_codes,desc,qty,unit,suppliers1):
    super(PDF,self).__init__()
    self.inquiry_number=inquiry_number
    self.No_of_items=No_of_items
    self.petra_codes=petra_codes
    self.desc=desc
    self.qty=qty
    self.unit=unit
    self.suppliers1=suppliers1
    self.current_date = datetime.today().date()
  def header(self):
    
    # PETRA logo
    self.image(Config.all_images+"PETRA_LOGO.png",x=80,y=5,w=50)
    self.set_font('DejaVu', '', 8)  ## I USED THIS font type to handle UTF-8 character which is critical issue on FPDF module
    
    
    ## PROJECT NAME
    
    self.multi_cell(w=28,h= 4,txt= f"RFQ#:{self.inquiry_number}\nDate:{self.current_date}",border=1, align='L')
    self.set_xy(192, 8)
    self.cell(16,6,f'   Page{self.page_no()}/{{nb}}',align="C",border=1,ln=1)
    self.ln(11)
    
    
    
    
    
    
    
  # def footer(self):
  #   self.set_y(-8)
  #   self.set_font('Arial', 'I', 10)
  #   self.cell(0,10,f'Page{self.page_no()}/{{nb}}',align="C")




 

@RFQ.route("/RFQ",methods=["GET","POST"])#post means to post to server, get means to get from server.


def RFQ_func():
  # print("hereee")
  
  if "user"in session:
    username=session["user"]
  
  if request.method=="POST":

    add_count()
    No_of_items=[]
    petra_codes=[]
    desc=[]
    desc_list=[]
    qty=[]
    unit=[]
    supplier=[]
    emails=[]
    emails1=[]
    conn = pyodbc.connect(Config.DATABASE_PARAMETER)
    cursor=conn.cursor()
    
    query=f"SELECT Supplier FROM suppliers"
    rows=cursor.execute(query)
    rows=rows.fetchall()
    # conn.commit()
    # conn.close()
    if rows:
      
      for row in range (0,len(rows)):
        
        supplier.append(rows[row]) 
      supplier = [item for t in supplier for item in t]  #convert list of tubles coming from SQL to list


    inquiry= request.files['inquiry']
    # inquiry=os.path.abspath(inquiry)
    # print(inquiry)
    inquiry.save(Config.saved_inquiries+f"{(inquiry.filename)}")
    # inquiry.save('Z:/M.hammad/saved_inquiries/'(inquiry.filename))
    # inquiry=inquiry.filename
    full_file_path=(Config.saved_inquiries+f"{(inquiry.filename)}")
    print(full_file_path)
    # supplier=request.form['supplier'] ##### this data come from excel sheet

    if not inquiry:
      flash('No file selected', "error")
    
    else:
      if  inquiry.filename.endswith('xlsx') or inquiry.filename.endswith('xls'):
        print("yes, it ends with xlxs or xls")
        xx=read_inquiry(full_file_path)
        suppliers1=request.form['suppliers1'] 
       
        # print(type(xx.inquiry_number))

        # get supplier email if exist
        query=f"SELECT email1,email2,email3,email4,email5,email6,email7,email8 FROM suppliers WHERE Supplier='{suppliers1}'"
        rows=cursor.execute(query)
        rows=rows.fetchall()
        conn.commit()
        conn.close()
        if rows:
          for row in range (0,len(rows)):
            
            emails.append(rows[row]) 
          emails = [item for t in emails for item in t]  #convert list of tubles coming from SQL to list
          for x in range(0,len(emails)):
            if emails[x]is None:

              pass
            else:
              emails1.append(emails[x])

          if len(emails1)==0:

            print("final email=0")
            flash('No emails found for this supplier, please update the database', "error")
            return render_template("RFQ.html",username=username,supplier=supplier)  

        emails1=[string.replace("'","") for string in emails1]
        emails1=[string.strip() for string in emails1]


      else:
          print("not excel")
          flash('the file selected is not Excel, please recheck', "error")
          return render_template("RFQ.html",username=username,supplier=supplier) 
      


        #create PDF object
 
      pdf=PDF(xx.inquiry_number,xx.No_of_items,xx.petra_codes,xx.desc,xx.qty,xx.unit,suppliers1)
      pdf.alias_nb_pages()
      #set auto page break
      pdf.set_auto_page_break(auto=True,margin=3)

      ## I added THIS font type to handle UTF-8 character which is critical issue on FPDF module:
      pdf.add_font('DejaVu', '', Config.fonts+'DejaVuSans.ttf', uni=True)
      #add page
      pdf.add_page()

      ###########################
      
 
      pdf.ln(5)
      # pdf.accept_page_break()
        # Select font
      pdf.set_font('Arial', 'B', 12)
      #  title
      pdf.cell(190, 10, 'Request for quotation',border=False, ln=1, align='C')
      # Line break
      pdf.ln(2)
      pdf.set_font('Arial', '', 10)
      pdf.multi_cell(w=150,h= 4,txt= "Dear Sir/Madam\nKindly provide us your best price and delivery date for below items:",border=0, align='L')
      pdf.ln(3)
    

      pdf.set_font('Arial', 'B', 12)
      pdf.cell(0, 0,txt = '---------------------------------------------------------------------------------------------------------------------------------------', ln = 1, align = 'L',border =0)
      pdf.cell(10, 8,txt = 'Item', ln = 0, align = 'C',border =0)
      pdf.cell(30, 8,txt = 'Code', ln = 0, align = 'C',border =0)
      pdf.cell(120, 8,txt = 'Description', ln = 0, align = 'C',border =0)
      pdf.cell(18, 8,txt = 'QTY', ln = 0, align = 'C',border =0)
      pdf.cell(15, 8,txt = 'UOM', ln = 1, align = 'C',border =0)
      pdf.cell(0, 0,txt = '---------------------------------------------------------------------------------------------------------------------------------------', ln = 1, align = 'L',border =0)
      pdf.set_font('DejaVu', '', 8)## I USED THIS font type to handle UTF-8 character which is critical issue on FPDF module
      base_Line_height=10
      
    
      df = pd.DataFrame({'Item':xx.No_of_items,'Code': xx.petra_codes,'Description':xx.desc,'QTY':xx.qty,'UOM':xx.unit})
      print(len(df))
      for i in range(0,len(xx.No_of_items)):
        pdf.set_font('DejaVu', '', 8)
        pdf.cell(10, base_Line_height,txt=f"{df['Item'][i]}", ln = 0, align = 'C',border=0)
        pdf.cell(30, base_Line_height,txt = f"{df['Code'][i]}", ln = 0, align = 'C',border=0)
        y=pdf.get_y()
        x=pdf.get_x()
        pdf.multi_cell(w=120,h=6,txt= f"{df['Description'][i]}",border=0, align='L')
        y1=pdf.get_y()
        x1=pdf.get_x()
        pdf.set_xy(x+120,y)
        pdf.cell(18, base_Line_height,txt = f"{df['QTY'][i]}", ln = 0, align = 'C',border=0)
        pdf.cell(15, base_Line_height,txt = f"{df['UOM'][i]}", ln = 1, align = 'C',border=0)
        pdf.set_xy(x1,y1+1)
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 0,txt = '---------------------------------------------------------------------------------------------------------------------------------------', ln = 1, align = 'L',border =0)

    
      
      #  #### export pdf file
      pdf.output(Config.RFQs+f"RFQ#{xx.inquiry_number}.pdf")
      
      
 
    #### send the inquiry email
      mail_RFQ(emails1,Config.RFQs+f"RFQ#{xx.inquiry_number}.pdf",xx.inquiry_number)
      return render_template("RFQ.html",username=username,supplier=supplier)  
      
    
  else:
    supplier=[]
    conn = pyodbc.connect(Config.DATABASE_PARAMETER)
    cursor=conn.cursor()
    
    query=f"SELECT Supplier FROM suppliers"
    rows=cursor.execute(query)
    rows=rows.fetchall()
    # conn.commit()
    # conn.close()
    if rows:
      
      for row in range (0,len(rows)):
        
        supplier.append(rows[row]) 
      supplier = [item for t in supplier for item in t]  #convert list of tubles coming from SQL to list
 
    return render_template("RFQ.html",username=username,supplier=supplier)


    
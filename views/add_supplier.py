from flask import Blueprint,render_template,request,send_file,session,redirect,url_for,flash
from numpy import concatenate
from datetime import datetime,date,timedelta,time
from models.add_count import add_count
import pyodbc
import pandas as pd
from config import Config

add_supplier=Blueprint("add_supplier",__name__,template_folder='templates',static_folder='static')

def __init__(self,suppliers):
    super(self).__init__()
    


@add_supplier.route("/add_supplier",methods=["GET","POST"])#post means to post to server, get means to get from server.
def add_supplier_func():

    
    if "user"in session:
        username=session["user"]
    if request.method=="POST":
        supplier=[]
        final_emails=[]
        suppliers1=request.form['suppliers1'] 
        conn = pyodbc.connect(Config.DATABASE_PARAMETER)
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
          # print(emails)
          # print(len(emails))
          for x in range(0,len(emails)):
            if emails[x]is None:

              pass
            else:
              emails1.append(emails[x])
          # print(emails1)
          # return render_template("RFQ.html",username=username,supplier=supplier,final_emails=final_emails) 
          
    

          if len(emails1)==0:

            print("final email=0")
            flash('No emails found for this supplier, please update the database', "error")
            return render_template("RFQ.html",username=username,supplier=supplier,final_emails=final_emails)  
          
        # print(emails1)
        emails1=[string.replace("'","") for string in emails1]
        # print(emails1)
        emails1=[string.strip() for string in emails1]
        print(emails1)
        return render_template("add_supplier.html",supplier=supplier)
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
        return render_template("add_supplier.html",supplier=supplier)
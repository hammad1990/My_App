from flask import Blueprint,render_template,request,send_file,session,redirect,url_for,flash
from numpy import concatenate
from datetime import datetime,date,timedelta,time
from models.add_count import add_count
import pyodbc
import pandas as pd
from config import Config

add_supplier=Blueprint("add_supplier",__name__,template_folder='templates',static_folder='static')

def __init__(self):
    super(self).__init__()
    


@add_supplier.route("/add_supplier",methods=["GET","POST"])#post means to post to server, get means to get from server.
def add_supplier_func():

    
    if "user"in session:
        username=session["user"]
    # if request.method=="POST":
    if  'Save' in request.form:
        add_count()
        new_emails_list=[""] * 8
        the_new_supp_name=request.form['add_new_supplier']##### the new supplier name
        x_list=request.form.getlist('emails_texts[]')### get all emails entered

        


        # check if supplier name is already exists in database
        conn = pyodbc.connect(Config.DATABASE_PARAMETER)
        cursor=conn.cursor()
        query=f"select Supplier from suppliers where Supplier='{the_new_supp_name}'"
        rows=cursor.execute(query)
        rows=rows.fetchone()
        print(rows)
        # conn.commit()
        # conn.close()

        if rows is not None:
          print("Supplier name is already taken")
          flash("Supplier name is already taken...",'error')
          return render_template("add_supplier.html",username=username,new_emails_list=new_emails_list,the_new_supp_name=the_new_supp_name)
        else:
          print("new supplier name")
          for x in range (0,len(x_list)):
             new_emails_list[x]=x_list[x]
             
          query=f"INSERT  INTO suppliers (Supplier,email1,email2,email3,email4,email5,email6,email7,email8) VALUES (?,?,?,?,?,?,?,?,?)"
          val=(the_new_supp_name, new_emails_list[0],new_emails_list[1],new_emails_list[2],new_emails_list[3],new_emails_list[4],new_emails_list[5],new_emails_list[6],new_emails_list[7])

          # cursor.execute("INSERT  INTO suppliers (Supplier,email1,email2,email3,email4,email5,email6,email7,email8) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",("",the_new_supp_name, new_emails_list[0],"",new_emails_list[1],"",new_emails_list[2],"",new_emails_list[3],"",new_emails_list[4],"",new_emails_list[5],"",new_emails_list[6],"",new_emails_list[7],"" ))

          cursor.execute(query,val)
          conn.commit()
          conn.close()
        
        return render_template("add_supplier.html",username=username,new_emails_list=new_emails_list,the_new_supp_name=the_new_supp_name)
    
    elif  'Show' in request.form or 'Update' in request.form:
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

        #convert list of tubles coming from SQL to list:
        out = []
        for t in supplier:
          for item in t:
            out.append(item)
        
        supplier=out
        supplier_to_edit=request.form['suppliers1']
        print(supplier_to_edit)
        # get supplier email if exist
        query1=f"SELECT email1,email2,email3,email4,email5,email6,email7,email8 FROM suppliers WHERE Supplier='{supplier_to_edit}'"
        rows1=cursor.execute(query1)
        rows1=rows1.fetchall()
        print(rows1)
        conn.commit()
        conn.close()
        if rows1:
          for row in range (0,len(rows1)):
            emails.append(rows1[row]) 
          emails = [item for t in emails for item in t]  #convert list of tubles coming from SQL to list
          # print(emails)
          # print(len(emails))
          for x in range(0,len(emails)):
            if emails[x]is None:
              pass
            else:
              emails1.append(emails[x])
          if len(emails1)==0:
            print("final email=0")
            flash('No emails found for this supplier, please update the database', "error")
            return render_template("add_supplier.html",username=username,supplier=supplier,supplier_to_edit=supplier_to_edit)  
          
        # print(emails1)
        emails1=[string.replace("'","") for string in emails1]
        # print(emails1)
        emails1=[string.strip() for string in emails1]
        # print(emails1)
        return render_template("add_supplier.html",username=username,supplier=supplier,supplier_to_edit=supplier_to_edit,emails1=emails1)

    elif  'Update' in request.form:
        conn = pyodbc.connect(Config.DATABASE_PARAMETER)
        cursor=conn.cursor()
        query=f"Update Supplier FROM suppliers"

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

          #convert list of tubles coming from SQL to list:
          out = []
          for t in supplier:
            for item in t:
              out.append(item)
          
          supplier=out
        
        return render_template("add_supplier.html",username=username,supplier=supplier)
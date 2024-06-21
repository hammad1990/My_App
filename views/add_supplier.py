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
    if request.method=="POST":
        add_count()
        new_emails_list=[""] * 8
        print(new_emails_list)
        the_new_supp_name=request.form['add_new_supplier']##### the new supplier name
        x_list=request.form.getlist('emails_texts[]')### get all emails entered
        


        # add the new supplier+ emails to database
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
             
          # query=f"INSERT  INTO suppliers ("",Supplier,email1,Tele1,email2,Tele2,email3,Tele3,email4,Tele4,email5,Tele5,email6,Tele6,email7,Tele7,email8,Tele8) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
          # val=("",the_new_supp_name, new_emails_list[0],"",new_emails_list[1],"",new_emails_list[2],"",new_emails_list[3],"",new_emails_list[4],"",new_emails_list[5],"",new_emails_list[6],"",new_emails_list[7],"")

          cursor.execute("INSERT  INTO suppliers (0,Supplier,email1,Tele1,email2,Tele2,email3,Tele3,email4,Tele4,email5,Tele5,email6,Tele6,email7,Tele7,email8,Tele8) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",("",the_new_supp_name, new_emails_list[0],"",new_emails_list[1],"",new_emails_list[2],"",new_emails_list[3],"",new_emails_list[4],"",new_emails_list[5],"",new_emails_list[6],"",new_emails_list[7],"" ))

          # cursor.execute(query,val)
          conn.commit()
          conn.close()
        
        return render_template("add_supplier.html",username=username,new_emails_list=new_emails_list,the_new_supp_name=the_new_supp_name)
    else:
        
        return render_template("add_supplier.html",username=username)
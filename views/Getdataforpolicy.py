from flask import Blueprint,render_template,request,send_file,session,redirect,url_for,flash
from numpy import concatenate
from datetime import datetime,date,timedelta,time
from models.add_count import add_count
import pyodbc
import pandas as pd
from config import Config
import decimal

Getdataforpolicy=Blueprint("Getdataforpolicy",__name__,template_folder='templates',static_folder='static')
@Getdataforpolicy.route("/Getdataforpolicy",methods=["GET","POST"])#post means to post to server, get means to get from server.
def Getdataforpolicy_func():

  output_result=[]
  TWOPLACES = decimal.Decimal(10) ** -2
  # print("connected"
  if "user"in session:
      username=session["user"]
  if request.method=="POST":
    ### we need to check if we are running the code on PETRA pc or not:
    if Config.DATABASE_PARAMETER=='Driver={ODBC Driver 17 for SQL Server};Server=DESKTOP-SR0QC2P\SQLEXPRESS;Database=usersDB;Trusted_Connection=yes;use_unicode=True;charset="utf8"':
      flash('you are not on PETRA PC', "error")
      return render_template("find_code.html",username=username)
    else:
      ### Connection with Epicor server
      conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=SRV-ERP11DB;'
                        'Database=ERP11LIVE;'
                        'UID=Rep;'
                        'PWD=')


      cursor=conn.cursor()
      
      Suppliers_names=request.form['Suppliers_names'] 
      keywords=request.form['keywords'] 
      From_Date1=request.form['From_Date1'] 
      ff=datetime.strptime(From_Date1, "%Y-%m-%d").date()
      To_Date1=request.form['To_Date1'] 
      tt=datetime.strptime(To_Date1, "%Y-%m-%d").date()
      # print(keywords)
      
      # exec Sal.SpecialPODataforPartSupplier 'ABB,Danfos,Delta','Freq,VLT,VFD','2025-01-01','2025-12-31'
      query=("EXEC Sal.SpecialPODataforPartSupplier ?,?,?,?")
      cursor.execute(query,Suppliers_names,keywords,ff,tt)
      

      

      while cursor.nextset(): # this is needed to skip first record which is table header
        try: 
          rows = cursor.fetchall()
          # print("yesss")

        
          
          break
        except:
          rows=""
          # print("problemm")
          
      
      if rows:
            print("there is rows")
            print(len(rows))
            # print(rows)
          

            for row in range (0,len(rows)):
              if rows[row][0] in output_result: #check if the record is already exist , then avoid adding it to final list.
                continue
              else:
                output_result.append(rows[row]) 
                output_result[row][6]=float(output_result[row][6]) #change float to string to make it easy to format
                output_result[row][6]="{:.2f}".format(output_result[row][6]) #format decimal value for PO total to show 2 digits after point .
                output_result[row][6]=f"{float(output_result[row][6]):,.2f}" #format decimal value for PO total to show , .
                if output_result[row][4]==0:
                   output_result[row][4]="closed"
                else:
                   output_result[row][4]="open"
                   
                
                  
            # print (type(output_result[0][6]))   
            print(output_result)    
            return render_template("Getdataforpolicy.HTML",username=username,output_result=output_result,Suppliers_names=Suppliers_names,keywords=keywords,From_Date1=From_Date1,To_Date1=To_Date1)   


      else:
        flash('no results, check the entry fields', "error")
        output_result=("No data")
        return render_template("Getdataforpolicy.HTML",username=username)

      conn.commit()
      conn.close()
      add_count()
      

    # if "GetData_button" in request.form:
      
    #     return render_template("GetItemData.HTML",username=username,output_result=output_result)
      

  else:

      
        return render_template("Getdataforpolicy.HTML",username=username)
    



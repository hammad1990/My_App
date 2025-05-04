from flask import Blueprint,render_template,request,send_file,session,redirect,url_for,flash
from numpy import concatenate
from datetime import datetime,date,timedelta,time
from models.add_count import add_count
import pyodbc
import pandas as pd
from config import Config

GetItemData=Blueprint("GetItemData",__name__,template_folder='templates',static_folder='static')
@GetItemData.route("/GetItemData",methods=["GET","POST"])#post means to post to server, get means to get from server.
def GetItemData_func():

  output_result=[]
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
      
      Supplier_Name=request.form['Supplier_Name'] 
      Description=request.form['Description'] 
      From_Date=request.form['From_Date'] 
      ff=datetime.strptime(From_Date, "%Y-%m-%d").date()
      To_Date=request.form['To_Date'] 
      tt=datetime.strptime(To_Date, "%Y-%m-%d").date()
      print(Description)
      
      # exec SSRS_GetPOVendorPartDescDateBetween 'DANFOSS FZCO','FREQUENCY INVERTOR','2024-01-01','2024-12-31'
      query=("EXEC SSRS_GetPOVendorPartDescDateBetween ?,?,?,?")
      cursor.execute(query,Supplier_Name,Description,ff,tt)
      

      

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
            # print(len(rows))
          

            for row in range (0,len(rows)):
              if rows[row][0] in output_result: #check if the record is already exist , then avoid adding it to final list.
                continue
              else:
                output_result.append(rows[row][0]) 
            output_result[0]=format(output_result[0],",")    
            print(output_result)    
            return render_template("GetItemData.HTML",username=username,output_result=output_result,Supplier_Name=Supplier_Name,Description=Description,From_Date=From_Date,To_Date=To_Date)   


      else:
        flash('no results, check the entry fields', "error")
        output_result=("No data")
        return render_template("GetItemData.HTML",username=username)

      conn.commit()
      conn.close()
      add_count()
      

    # if "GetData_button" in request.form:
      
    #     return render_template("GetItemData.HTML",username=username,output_result=output_result)
      

  else:

      
        return render_template("GetItemData.HTML",username=username)
    



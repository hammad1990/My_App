from flask import Blueprint,render_template,request,send_file,session,redirect,url_for,flash
from numpy import concatenate
from datetime import datetime,date,timedelta,time
from models.add_count import add_count
import pyodbc
import pandas as pd
from config import Config

find_code=Blueprint("find_code",__name__,template_folder='templates',static_folder='static')
@find_code.route("/find_code",methods=["GET","POST"])#post means to post to server, get means to get from server.
def find_code_func():
  search_words_list=[]
  code=[]
  desc=[]
  demand=[]
  onhand=[]
  uom=[]
  cost=[]
  currency=[]
  supplier=[]
  supplierid=[]
  origin=[]
  lastpo=[]
  podate=[]


  
  # print("connected")
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
      epicor=request.form.get('epicor')
      search_words=request.form['find_code'] 
      print(search_words)
      if epicor=="epicor":  ##### check if we search by epicor code
        query=("EXEC SSRS_ProcurmentPartSupplier ?,?,?,?,?")
        cursor.execute(query,"","","","",search_words)
      else:
        if "+" in search_words:
          # print("+ found")
          search_words_list=search_words.split('+')
          # print(search_words_list)
          if len(search_words_list)==2:
              query=("EXEC SSRS_ProcurmentPartSupplier ?,?,?,?,?")
              cursor.execute(query,search_words_list[0],search_words_list[1],"","","")
          elif len(search_words_list)==3:
              query=("EXEC SSRS_ProcurmentPartSupplier ?,?,?,?,?")
              cursor.execute(query,search_words_list[0],search_words_list[1],search_words_list[2],"","")
          elif len(search_words_list)==4:
              query=("EXEC SSRS_ProcurmentPartSupplier ?,?,?,?,?")
              cursor.execute(query,search_words_list[0],search_words_list[1],search_words_list[2],search_words_list[3],"")

        else:
            query=("EXEC SSRS_ProcurmentPartSupplier ?,?,?,?,?")
            cursor.execute(query,search_words,"","","","")


      while cursor.nextset(): # this is needed to skip first record which is table header
        try: 
          rows = cursor.fetchall()
          # print("yesss")

        
          
          break
        except:
          rows=""
          # print("problemm")
          
      
      if rows:
            # print("there is rows")
            # print(len(rows))

            for row in range (0,len(rows)):
              if rows[row][0] in code: #check if the record is already exist , then avoid adding it to final list.
                continue
              else:
                code.append(rows[row][0]) 
                desc.append(rows[row][1]) 
                lastpo.append(rows[row][2]) 
                supplierid.append(rows[row][3])
                supplier.append(rows[row][4])
                podate.append(rows[row][5])
                cost.append(float(rows[row][6]))
                currency.append(rows[row][7])
                uom.append(rows[row][8])
                origin.append(rows[row][9])
                onhand.append(float(rows[row][10]))
                demand.append(float(rows[row][11]))
      else:
        flash('no results', "error")

      conn.commit()
      conn.close()
      add_count()

    if "Search_code" in request.form:
      
        return render_template("find_code.html",username=username,search_words=search_words,code=code,desc=desc,\
                              lastpo=lastpo,supplierid=supplierid,supplier=supplier,podate=podate,cost=cost,currency=currency,uom=uom,origin=origin,onhand=onhand,demand=demand)
      
    elif "open_it_as_excel" in request.form:
        add_count()
        print("exceeelllll")
        data={'code':code,'desc':desc,'demand':demand,'onhand':onhand,'uom':uom,'cost':cost,'currency':currency,'supplier':supplier,'suppliedid':supplierid,'origin':origin,'lastpo':lastpo}
        df1 = pd.DataFrame(data)
        
        # df1.to_excel("Z:/M.hammad/find codes outputs/search.xlsx") 
        
        # return send_file("Z:/M.hammad/find codes outputs/search.xlsx",as_attachment=True)
        # here i will download it excel sheet without need to save it first(we need to test it ??)
        return send_file(df1.to_excel("search.xlsx") ,as_attachment=True)

  else:

      
      return render_template("find_code.html",username=username)
    



from flask import Blueprint,render_template,request,send_file,session,redirect,url_for
from numpy import concatenate
from fpdf import FPDF
from models.open_soo import open_soo
import pyodbc
from config import Config

sequence1=Blueprint("sequence1",__name__,template_folder='templates',static_folder='static')
@sequence1.route("/sequence1",methods=["GET","POST"])#post means to post to server, get means to get from server.
def sequence_func1():
  Pnames=[]
  Countries=[]
  UserNames=[]
  Revisions=[]
  print("sequence1  page")
  if "user"in session:
      username=session["user"]
  
  if  'New_Project' in request.form:
    # print("ffffffffffffff")
    return redirect (url_for('sequence.sequence_func'))
  
  # if  'Search_Project' in request.form: 
  #   conn = pyodbc.connect(Config.DATABASE_PARAMETER)

  #   cursor=conn.cursor()
    
  #   query=f"SELECT * FROM SOO"
  #   rows=cursor.execute(query)
  #   rows=rows.fetchall()
  #   conn.commit()
  #   conn.close()
  #   if rows:
  #     for row in range (0,len(rows)):
        
  #       UserNames.append(rows[row][1]) 
  #       Countries.append(rows[row][2]) 
  #       Pnames.append(rows[row][3]) 
  #       Revisions.append(rows[row][5]) 
      
  #     # print(Countries)
  #   return render_template("sequence1.html",username=username,UserNames=UserNames,Pnames=Pnames,Countries=Countries,Revisions=Revisions)
  else:
    
    
    return render_template("sequence1.html")

@sequence1.route("/sequence1/<pname>",methods=["GET","POST"])#post means to post to server, get means to get from server.
def sequence_func11(pname):
  if "user"in session:
      username=session["user"]
  open_soo(pname,username)

  # return render_template("sequence1.html")
  return redirect(url_for("sequence1.sequence_func1"))

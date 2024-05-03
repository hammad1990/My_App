from ast import Mod
import math
from flask import Blueprint,render_template,request,send_file,session,redirect,url_for
from numpy import concatenate
from fpdf import FPDF
import webbrowser
import codecs
from datetime import datetime,date,timedelta,time
from models.add_count import add_count
from models.mail_SOO import mail_SOO
from models.save_soo import save_soo
from models.open_soo import open_soo
import pyodbc
import base64

sequence1=Blueprint("sequence1",__name__,template_folder='templates',static_folder='static')
@sequence1.route("/sequence1",methods=["GET","POST"])#post means to post to server, get means to get from server.
def sequence_func1():
  Pnames=[]
  Countries=[]
  UserNames=[]
  Revisions=[]
  if "user"in session:
      username=session["user"]
  
  if  'New_Project' in request.form:
    # print("ffffffffffffff")
    return redirect (url_for('sequence.sequence_func'))
  
   
  else:
    
    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=PEEDM-HAMAD;'
                      'Database=usersDB;'
                      'Trusted_Connection=yes;')

    cursor=conn.cursor()
    
    query=f"SELECT * FROM SOO"
    rows=cursor.execute(query)
    rows=rows.fetchall()
    conn.commit()
    conn.close()
    if rows:
      for row in range (0,len(rows)):
        
        UserNames.append(rows[row][1]) 
        Countries.append(rows[row][2]) 
        Pnames.append(rows[row][3]) 
        Revisions.append(rows[row][5]) 
      
      # print(Countries)
    return render_template("sequence1.html",username=username,UserNames=UserNames,Pnames=Pnames,Countries=Countries,Revisions=Revisions)

@sequence1.route("/sequence1/<pname>",methods=["GET","POST"])#post means to post to server, get means to get from server.
def sequence_func11(pname):
  open_soo(pname)

  # return render_template("sequence1.html")
  return redirect(url_for("sequence1.sequence_func1"))

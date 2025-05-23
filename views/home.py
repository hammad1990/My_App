from flask import Blueprint,render_template,request,session,redirect,url_for
import pyodbc
from config import Config

home=Blueprint("home",__name__,template_folder='templates',static_folder='static')

@home.route("/home",methods=["GET","POST"]) 
def home_func():
    all_users=[]
    all_counts=[]
    print("home page")
    if "user"in session:
        username=session["user"]
        section=session["section"]
        conn = pyodbc.connect(Config.DATABASE_PARAMETER)
        cursor=conn.cursor()
        query=f"SELECT * FROM users1"
        rows=cursor.execute(query)
        
        rows=rows.fetchall()
        conn.commit()
        conn.close()
        # print(rows)
        for row in range (0, len(rows)):
          # print(rows[row][1])
          all_users.append(rows[row][1])      #get all names from DB
          all_counts.append(rows[row][4])       #get all counts from DB


        # print(all_users)
        # print(all_counts)
        return render_template("home.html",username=username,all_users=all_users,all_counts=all_counts)
        
    else:
        return redirect(('login'))
    

    
 
   
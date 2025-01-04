from itertools import count
from flask import Blueprint,render_template,request,redirect,flash,url_for,session
import pyodbc
from datetime import datetime,date,timedelta,time
from config import Config







login=Blueprint("login",__name__,template_folder='templates',static_folder='static') 
@login.route("/login",methods=["GET","POST"]) 
@login.route("/",methods=["GET","POST"]) 
def login_func():
    current_date1 = datetime.today().date()
    session["current_date1"]=current_date1
    # print("log in page")
    if  'Login' in request.form:
        # print("log in page1")
        session["count-day"]=0
        session["count-week"]=0
        Lm= request.form['Lemail']
        Lp= request.form['Lpassword']
        
        conn = pyodbc.connect(Config.DATABASE_PARAMETER)
        print("log in page2")

       

        cursor=conn.cursor()
        # print("log in page3")
        query=f"SELECT * FROM users1 where email='{Lm}' AND password='{Lp}'"
        rows=cursor.execute(query)
        rows=rows.fetchall()
        # print(len(rows))

        if rows:
            # for row in rows:
                # print(row)
            # print("ok")
            username=rows[0][1]       #get the name from the record
            id=rows[0][0]             #get the id from the record
            email=rows[0][2]          # get the email
            section=rows[0][5]          # get the section

            print(username)
            # session = {'counter':0}
            session["id"]=id
            session["user"]=username
            session["email"]=email
            session["section"]=section
            
          
         
            return render_template("home.html")
            # return render_template('home.html',Rsection=session["section"],username=session["user"])
            # return redirect(url_for("home.home_func"))
       
        else:
            print("Incorrect email or password")
            flash('Incorrect email or password',"error")
            return render_template("login.html")
    elif  'Register' in request.form:
      print("start register")
      Rn= request.form['Rname']
      Rm= request.form['Remail']
      Rp= request.form['Rpassword']
      Rsection= request.form['Rsection']
      conn = pyodbc.connect(Config.DATABASE_PARAMETER)

      cursor=conn.cursor()
      query=f"SELECT * FROM users1 where name='{Rn}' OR email='{Rm}'"
      rows=cursor.execute(query)
      rows=rows.fetchone()
      # print(rows)

      if rows is not None:
        flash("That username or email is already taken...",'error')
        return render_template('login.html')
      else:
      
      
        cursor.execute("INSERT  INTO users1 (name,email,password,section) VALUES (?,?,?,?)",(Rn,Rm,Rp,Rsection))
        conn.commit()
        conn.close()

      print(Rsection)
      # return redirect(url_for("home.home_func"),Rsection=Rsection)
      return render_template("login.html",Rsection=Rsection)

    else:
        
        return render_template("login.html")
    
    
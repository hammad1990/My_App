from datetime import datetime,date,timedelta,time
import pyodbc
from flask import session


class add_count:
    def __init__(self):
      id=session["id"]
      # print(type(id))
      current_date1=session["current_date1"]
      # print("current_date1=" ,type(current_date1))
      current_date1=datetime.strptime(current_date1, '%a, %d %b %Y %H:%M:%S GMT') ##### convert strin to datetime format
      current_date1=current_date1.date()##### convert strin to datetime format
      # print("current_date1=" ,current_date1)
      current_date2 = datetime.today().date()
      # print("current_date2=" ,current_date2)


      if (current_date2==current_date1):
        session['count-day']+=1
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                        'Server=PEEDM-HAMAD;'
                        'Database=usersDB;'
                        'Trusted_Connection=yes;')
        cursor=conn.cursor()
        query=('''\
              set identity_insert users1 on;
              UPDATE users1
              SET count  =?
              WHERE id=?
              set identity_insert users1 off;
              ''')
        values=(session['count-day'],session["id"])
        cursor.execute(query,values)
        conn.commit()
        conn.close()
      else:
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=PEEDM-HAMAD;'
                              'Database=usersDB;'
                              'Trusted_Connection=yes;')
        cursor=conn.cursor()
        query=f"SELECT * FROM users1 where id='{id}'"
        rows=cursor.execute(query)
        rows=rows.fetchall()
        session["count-week"]+=rows[0][4]  #get the daily counts for this ID
        session['count-day']=0
        session['count-day']+=1
        # print("hereee")
        # print(session["count-week"])
        query=('''\
              set identity_insert users1 on;
              UPDATE users1
              SET count  =?
              WHERE id=?
              set identity_insert users1 off;
              ''')
        values=(session['count-day'],id)
        cursor.execute(query,values)
        # print("hereee22")
        conn.commit()
        conn.close()
        # print("hereee33")
        session["current_date1"]=current_date2
        # print("hereee44")
#################### ends counts#################
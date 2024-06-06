
from calendar import month
from itertools import count
import math
from flask import Blueprint,render_template,request,session,redirect
from models.Get_Heater import heat11
from models.mail_heater import mail_heater
from models.add_count import add_count








heater=Blueprint("heater",__name__)
@heater.route("/heater",methods=["GET","POST"])  #post means to post to server, get means to get from server.
def selection():
  
  if "user"in session:
      username=session["user"]
      section=session["section"]
        
  if request.method=="POST":
    heatercap=request.form['heatercap'] 
    volt=request.form['volt']
    stage=request.form['stage']
    heatercap=float(heatercap)
    volt=int(volt)
    stage=int(stage)
    # print(stage)
    
    st=heat11(heatercap,stage,volt)
    
    st1=st.st1
    st2=st.st2
    st3=st.st3
    st4=st.st4
    st5=st.st5
    st6=st.st6

    sum1=0  
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0

    for x1 in range(0,len(st1)):
        sum1+= st1[x1]
    for x2 in range(0,len(st2)):
        sum2+= st2[x2]
    for x3 in range(0,len(st3)):
        sum3+= st3[x3]
    for x4 in range(0,len(st4)):
        sum4+= st4[x4]
    for x5 in range(0,len(st5)):
        sum5+= st5[x5]
    for x6 in range(0,len(st6)):
        sum6+= st6[x6]
    mat=[
        st1,
        st2,
        st3,
        st4,
        st5,
        st6
    ]
    
    totalkw=sum1+sum2+sum3+sum4+sum5+sum6
    heatercap=float(heatercap)
    totalkw=float(totalkw)  
  if 'Run' in request.form:

    add_count()
   
    return render_template("heater.html",mat=mat, sum1=sum1,sum2=sum2,sum3=sum3,sum4=sum4,sum5=sum5,sum6=sum6,totalkw=totalkw,heatercap=heatercap,volt=volt,username=username,Rsection=section)
############# send email##########
  elif "Send Email" in request.form:
    add_count()
    mail_heater(username,heatercap,volt,stage,totalkw)
    return render_template("heater.html",mat=mat, sum1=sum1,sum2=sum2,sum3=sum3,sum4=sum4,sum5=sum5,sum6=sum6,totalkw=totalkw,heatercap=heatercap,volt=volt,username=username,Rsection=section)
#############end send email##########  
  else:
     
    return render_template("heater.html",username=username,Rsection=section)
      

   
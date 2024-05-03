from flask import Blueprint,render_template,request,session,redirect,url_for,session

logout=Blueprint("logout",__name__,template_folder='templates',static_folder='static')
 
@logout.route("/logout") 
def logout_func():
    session.pop('user',None)
    return redirect('login')
   
    

    
  
   

from flask import Blueprint,render_template,request,session,redirect,url_for,session
from models.read_excel_R1 import read_excel
from models.write_excel_R0 import write_excel
# from werkzeug import secure_filename


pointlist=Blueprint("pointlist",__name__,template_folder='templates',static_folder='static')
 
@pointlist.route("/pointlist", methods=["GET","POST"]) 
def pointlist_func():
    
    if "user"in session:
        username=session["user"]
    else:
        return redirect('login')
    
    if request.method=="POST":
        main_list= request.files['main file']
        alaa_list= request.files['project file']
        print (type(main_list))
        
        
        

        if main_list and alaa_list:
            print(main_list)
            print(alaa_list)
            final_names=read_excel(main_list,alaa_list).final_names
            final_type=read_excel(main_list,alaa_list).final_type
            final_object_id=read_excel(main_list,alaa_list).final_object_id
            final_device_id=read_excel(main_list,alaa_list).final_device_id
            final_object_name=read_excel(main_list,alaa_list).final_object_name
            final_read_write=read_excel(main_list,alaa_list).final_read_write
            final_unit=read_excel(main_list,alaa_list).final_unit
            final_min=read_excel(main_list,alaa_list).final_min
            final_max=read_excel(main_list,alaa_list).final_max
            final_normal_state=read_excel(main_list,alaa_list).final_normal_state
            final_desc=read_excel(main_list,alaa_list).final_desc
            write_excel(final_names,final_type,final_object_id,final_device_id,final_object_name,final_read_write,final_unit,final_min,final_max,final_normal_state,final_desc)


        # f.save(secure_filename(f.filename))
        return render_template ("pointlist.html",username=username)
    else:
        return render_template ("pointlist.html",username=username)

            
            
            
            
            

        
from flask import Blueprint,render_template,request,session,url_for
# from datetime import datetime,date,timedelta,time
from models.co_getcompressor import getCompressor
from models.co_getcondenser import getCondenser
from models.co_getsupply import getSupply
from models.co_getwheel import getWheel
from models.add_count import add_count
from models.Create_excel_component import Create_excel_component
from flask import send_file

components=Blueprint("components",__name__,template_folder='templates',static_folder='static')

@components.route("/components",methods=["GET","POST"]) 
def components_func():
  if "user"in session:
        username=session["user"]
  if request.method=="POST":
    add_count()
    
    co_project_no=request.form['co_project_no']##### Project_Number
    co_item_model=request.form['co_item_model']##### unit model PPH/WPPH
    co_item_qty=request.form['co_item_qty']##### QTY
    co_item_no=request.form['co_item_no']##### ITEM NO
    co_item_ref=request.form['co_item_ref']##### ITEM REF
    co_ambient=request.form['co_ambient']##### ITEM AMBIENT
    co_voltage=request.form['co_voltage']##### ITEM VOLTAGE
    co_cond_model=request.form['co_cond_model']##### cond fans
    co_fans_type=request.form.getlist('co_fans_type[]')#####  fans types
    compressors={}
    condensers={}
    supply={}
    CompNo=[]
    SupplyNo=[]
    
    print(co_fans_type)
    
    
    
    co_comp_brand=request.form.getlist('co_comp_brand[]')
    # ///////////////////////////////208V COMPRESSORS////////////////////////////////////////
    if co_voltage=="208V-3-60Hz" or co_voltage=="220V-3-60Hz" or co_voltage=="230V-3-60Hz" :
      
      co_comp_hp_220=request.form.getlist('co_comp_hp_220[]')
      co_comp_220=request.form.getlist('co_comp_220[]')
      if co_comp_hp_220 and co_comp_220:
        # print(len(co_comp_brand))
        for x in range (0,len(co_comp_brand)):
          CompNo.append(x+1)
          comp_data=getCompressor(CompNo[x],co_comp_brand[x],co_comp_220[x],co_comp_hp_220[x],co_voltage,co_ambient)
          CompModel=comp_data.model
          if CompModel=="VZH035CJANB"  or CompModel=="VZH044CJANB/M" or CompModel=="VZH065CJANB" or CompModel=="VZH088BJANA/I/P06" or CompModel=="VZH088CJAN":
            # print(CompModel)
            compressors.update({f'CompNo:{x+1}':[co_comp_brand[x],CompModel,comp_data.CompNo,comp_data.hp,comp_data.Amp,comp_data.PT,comp_data.Cablein,comp_data.Cableout,comp_data.VC,comp_data.CB]})
          else:
             if int(comp_data.hp) < 15:
            # print(CompModel)
              compressors.update({f'CompNo:{x+1}':[co_comp_brand[x],CompModel,comp_data.CompNo,comp_data.hp,comp_data.Amp,comp_data.PT,comp_data.Cable,comp_data.Contactor,comp_data.MMS]})
             else:
               compressors.update({f'CompNo:{x+1}':[co_comp_brand[x],CompModel,comp_data.CompNo,comp_data.hp,comp_data.Amp,comp_data.PT,comp_data.Cable,comp_data.Contactor,comp_data.Breaker]})
   
  #  ///////////////////////460V COMPRESSORS///////////////////
    elif co_voltage=="460V-3-60Hz" or co_voltage=="480V-3-60Hz":   
      co_comp_hp_460=request.form.getlist('co_comp_hp_460[]')
      co_comp_460=request.form.getlist('co_comp_460[]') 
      if co_comp_hp_460 and co_comp_460:
        for x in range (0,len(co_comp_brand)):
          CompNo.append(x+1)
          comp_data=getCompressor(CompNo[x],co_comp_brand[x],co_comp_460[x],co_comp_hp_460[x],co_voltage,co_ambient)
          CompModel=comp_data.model
          if CompModel=="VZH088AGANA"  or CompModel=="VZH117AGANA" :
            # print(CompModel)
            compressors.update({f'CompNo:{x+1}':[co_comp_brand[x],CompModel,comp_data.CompNo,comp_data.hp,comp_data.Amp,comp_data.PT,comp_data.Cablein,comp_data.Cableout,comp_data.VC,comp_data.CB]})
          else:
             if int(comp_data.hp) < 15:
            # print(CompModel)
              compressors.update({f'CompNo:{x+1}':[co_comp_brand[x],CompModel,comp_data.CompNo,comp_data.hp,comp_data.Amp,comp_data.PT,comp_data.Cable,comp_data.Contactor,comp_data.MMS]})
             else:
               compressors.update({f'CompNo:{x+1}':[co_comp_brand[x],CompModel,comp_data.CompNo,comp_data.hp,comp_data.Amp,comp_data.PT,comp_data.Cable,comp_data.Contactor,comp_data.Breaker]})

################################ condenser####################################
    if  co_cond_model !=" " and co_cond_model !="No Condenser Fans":
      
      co_cond_qty=request.form['co_cond_qty']##### cond fans QTY
      co_cond_vee=request.form['co_cond_vee']##### cond COIL VEE
      co_cond_speed=request.form['co_cond_speed']##### cond COIL speed
      condenser_data=getCondenser(co_cond_model,co_cond_qty,co_cond_vee,co_cond_speed,co_voltage)
      condensers={'Brand':condenser_data.Brand,'model':co_cond_model,'HP':condenser_data.HP,'qty':co_cond_qty,'FLA':condenser_data.Amp,'Cable':condenser_data.Cable,'Contactor':condenser_data.Contactor,'Breaker':condenser_data.Breaker,'vee':co_cond_vee,'speed':co_cond_speed}
      # print(condeser_data)
      # print(co_cond_qty)
      # print(co_cond_vee)
     
    else:
      print("no cond fans ")
      # print(condensers)
      condensers={'Brand':"NOTHING"}
      # Create_excel_component(co_project_no,co_item_model,co_item_qty,co_item_no,co_item_ref,co_ambient,co_voltage,compressors,condensers)
################################ supply ####################################
    if  co_fans_type !="--" :
      # 
        co_fans_qty=request.form.getlist('co_fans_qty[]')##### fans QTY
        co_fansvfd=request.form.getlist('co_fansvfd[]')##### vfds
        # print(co_fans_qty)
        # print(co_fansvfd_220)
        for w in range (0,len(co_fans_type)):
          SupplyNo.append(w+1)
          if co_fans_type[w]=="E.wheel":
            co_wheel_model=request.form.getlist('co_ew_model[]')##### wheel
            fans_data=getWheel(co_wheel_model,co_voltage)
            supply.update({co_fans_type[w]:[fans_data.Brand,fans_data.HP,co_fans_qty[w],fans_data.Amp,fans_data.Cable,fans_data.Vfd,fans_data.Breaker]})
        # print(supply)
        # Create_excel_component(co_project_no,co_item_model,co_item_qty,co_item_no,co_item_ref,co_ambient,co_voltage,compressors,condensers,supply)
        # return render_template("components.html",username=username)
      
          else :
            co_fans_hp=request.form.getlist('co_fans_hp[]')##### fans HP
        # co_fans_qty=request.form.getlist('co_fans_qty[]')##### fans QTY
        # co_fansvfd=request.form.getlist('co_fansvfd[]')##### vfds
        # print(co_fans_qty)
        # print(co_fansvfd_220)
        # for w in range (0,len(co_fans_type)):
            SupplyNo.append(w+1)
            fans_data=getSupply(co_fans_type[w],co_fans_hp[w],co_fansvfd[w],co_voltage)
            supply.update({co_fans_type[w]:[fans_data.Brand,fans_data.HP,co_fans_qty[w],fans_data.Amp,fans_data.Cable,fans_data.Vfd,fans_data.Breaker]})
        # print(supply)
        Create_excel_component(co_project_no,co_item_model,co_item_qty,co_item_no,co_item_ref,co_ambient,co_voltage,compressors,condensers,supply)


        # LOC1=f"Z:/M.HAMMAD/components output/{co_project_no} {co_item_model} item{co_item_no}.xlsx"
        LOC1=url_for(f"components output/{co_project_no} {co_item_model} item{co_item_no}.xlsx")


        return send_file(LOC1,as_attachment=True)### THIS SEND FILE ONLY WORKS OK WHEN IT'S USED IN VIEW FUNCTION, WHILE OTHER MODULES NOT SHOWING DOWNLOAD PROCESS
        # return render_template("components.html",username=username)
    

      
      
  

  else:
 
    return render_template("components.html",username=username)
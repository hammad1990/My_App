
from ast import Mod

from flask import Blueprint,render_template,request,send_file,session,redirect,flash
from numpy import concatenate
from fpdf import FPDF

from datetime import datetime,date,timedelta,time
from models.add_count import add_count
from models.mail_SOO import mail_SOO
from models.save_soo import save_soo
from models.open_soo1 import open_soo1
import time
import base64




sequence=Blueprint("sequence",__name__,template_folder='templates',static_folder='static')

class PDF(FPDF):

  
  def __init__(self,Project_Name,country,rev):
    super(PDF,self).__init__()
    self.pn=Project_Name
    self.country=country
    self.current_date = datetime.today().date()
    self.rev=rev
  def header(self):
    
    # PETRA logo
    self.image("Z:/M.HAMMAD/PY/My_Apps/static/imgs/PETRA_LOGO.png",x=80,y=5,w=50)
    self.ln(1)
    ## PROJECT NAME
    self.set_font('Arial', 'B', 8)
    self.multi_cell(w=60,h= 4,txt= f"Project Name:{self.pn}\nCountry:{self.country}\nDate:{self.current_date}\nRev:{self.rev}",border=1, align='L')
    
    
    
    self.ln(1)
      # Select font
    self.set_font('Arial', 'B', 15)
    #  title
    self.cell(190, 10, 'Sequence Of Operation',border=False, ln=1, align='C')
    # Line break
    self.ln(1)
    
    
  def footer(self):
    self.set_y(-8)
    self.set_font('Arial', 'I', 10)
    self.cell(0,10,f'Page{self.page_no()}/{{nb}}',align="C")




 

@sequence.route("/sequence",methods=["GET","POST"])#post means to post to server, get means to get from server.


def sequence_func():
  SOO=[]
  
 

  if "user"in session:
      username=session["user"]
  
 

  if request.method=="POST":
    
    
    sensors_list=[]
    protections_list=[]
    cool_modes_list=[]
    heat_modes_list=[]
    heat1_modes_list=[]
    heat2_modes_list=[]
    heatpump_modes_list=[]
    defrost_modes_list=[]
    Dampers_modes_list=[]
    Model=request.form['Model']  ##pph/DSP
    Controller=request.form['Controller']
    Control=request.form['Control']  ###fresh
    Mode=request.form['Mode'] #####cool /heat
    Heater=request.form['Heater'] #####dehum
    Dampers=request.form['Dampers'] #####Dampers
    Steam=request.form['Steam'] ####yes/no
    Exhaust=request.form['Exhaust'] ####yes/no
    Supply=request.form['Supply'] ####STD/EC/VFD
    protections=request.form['Protections'] #### MMS
    Project_Name=request.form['Project_Name']##### Project_Name
    country=request.form['country']##### country
    rev=request.form['rev']##### rev
    custom_sequence_title=request.form['custom_sequence_title']##### custom_sequence_title
    custom_sequence=request.form['custom_sequence']##### custom_sequence
    
    
   
    # custom_sequence_title1=request.form['custom_sequence_title1']##### custom_sequence_title1
    # custom_sequence_title2=request.form['custom_sequence_title2']##### custom_sequence_title2
    # custom_sequence1=request.form['custom_sequence1']##### custom_sequence1
    # custom_sequence2=request.form['custom_sequence2']##### custom_sequence1
    special_sensors=request.form['special_sensors']##### special_sensors
    options=request.form.getlist('fn') #### options
    sensors=""
    # print(custom_sequence_title)
    # print(Project_Name)
  # print(Mode)
  # print(Heater)
  # print(Steam)
  # print(Exhaust)
  # print(protections)
  # print(options)
    
    if open_soo1(Project_Name,rev).x== 5:
      flash('SOO with same name & Rev No. is already exist', "error")
      print("yesssssssssss")
      return render_template("sequence.html",username=username) 
    else:
      flash('SOO not exist', "error")
      print("noooooooooo")


    
  
  #############USED SENSORS######
    if Control=="Fresh":
      #  print("HERE111222")
      # if Exhaust=="STD Exhaust" or Exhaust== "Exhaust VFD with PT" or  Exhaust== "Exhaust EC fan motor":
      if Exhaust!="None":
          
          if Mode=="Cooling only":
            
            if Steam=="Steam_No":
                # print("no steam")
                if Heater=="Dehumidifiction(Reheat)" :
                  sensors="RAT+H+SAT+OAT"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
                      # print(sensors_list)
                      
                elif Heater=="Heating & Dehumidifiction" :
                  sensors="RAT+H+SAT+OAT"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
                elif Heater=="Heating":
                  sensors="RAT+SAT+OAT"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
                
                    
                
          
                  
                      
                
            else:
                sensors="RAT+H+SAT+OAT"
                with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
                      # print("HERE3")
                      # print(sensors_list)
################ HP##########################
          else:
              if Steam=="Steam_No":
                if Heater=="Supplement for Heat pump & Dehumidification":
                  sensors="RAT+H+SAT+OAT+DEF"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
                else:
                  sensors="RAT+DEF+SAT+OAT"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
              else:
                  sensors="RAT+H+SAT+OAT+DEF"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                        t=k.read()
                        sensors_list.append(t)
############ FRESH+NO EXHAUST####################################
      else:
          if Mode=="Cooling only":
            if Steam=="Steam_No":
                if Heater=="Dehumidifiction(Reheat)" or Heater=="Heating & Dehumidifiction":
                  sensors="ROOMT+H+SAT+OAT"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
                else:
                  # print("ffffff")
                  sensors="ROOMT+SAT+OAT"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
            else:
                sensors="ROOMT+H+SAT+OAT"
                with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
################ HP##########################
          else:
              if Steam=="Steam_No":
                if Heater=="Supplement for Heat pump & Dehumidification":
                  sensors="ROOMT+H+SAT+OAT+DEF"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
                else:
                  sensors="ROOMT+DEF+SAT+OAT"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
              else:
                  sensors="ROOMT+H+SAT+OAT+DEF"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                        t=k.read()
                        sensors_list.append(t)


############## non fresh############################
    else:
      if Mode=="Cooling only":
            if Steam=="Steam_No":
                if Heater=="Dehumidifiction(Reheat)" or Heater=="Heating & Dehumidifiction":
                  sensors="RAT+H+SAT+OAT"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
                elif Heater=="Heating":
                  sensors="RAT+SAT+OAT"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
                else:
                  sensors="RAT+SAT+OAT"
                  # print("ffffffffffff")
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
            else:
                sensors="RAT+H+SAT+OAT"
                with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
################ HP##########################
      else:
            if Steam=="Steam_No":
                if Heater=="Supplement for Heat pump & Dehumidification":
                  sensors="RAT+H+SAT+OAT+DEF"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
                else:
                  sensors="RAT+DEF+SAT+OAT"
                  with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)
            else:
                sensors="RAT+H+SAT+OAT+DEF"
                with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"+sensors+".txt","r") as k:
                      t=k.read()
                      sensors_list.append(t)

    # print(sensors_list)

    if special_sensors:
      sensors_list[0]=special_sensors
      # print(sensors_list)
      
    

    #############END  USED SENSORS######

    ############# protections##########
    with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/protections/"+"STD"+".txt","r") as q8:
                      t8=q8.read()
                      protections_list.append(t8)
                      
    if protections=="STD":
      pass
      
    elif protections=="CB FOR ALL POWER":
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/protections/"+protections+".txt","r") as q9:
                      t9=q9.read()
                      protections_list.append(t9)
                      
    elif protections=="CB FOR COMP+CFM":
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/protections/"+protections+".txt","r") as q1:
                      t=q1.read()
                      protections_list.append(t)
                      
                      

    elif protections=="CB FOR COMP":
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/protections/"+protections+".txt","r") as q1:
                      t=q1.read()
                      protections_list.append(t)
                      
                      

    elif protections=="CB+OL FOR ALL POWER":
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/protections/"+protections+".txt","r") as q1:
                      t=q1.read()
                      protections_list.append(t)  
                      
                      

    elif protections=="CB+OL FOR ALL MOTORS":
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/protections/"+protections+".txt","r") as q1:
                      t=q1.read()
                      protections_list.append(t) 
                      
                        

    elif protections=="CB+OL FOR COMP":
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/protections/"+protections+".txt","r") as q1:
                      t=q1.read()
                      protections_list.append(t) 
                      
                                      
    
    else:
      protections="CB+OL FOR COMP+CFM"
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/protections/"+protections+".txt","r") as q9:
                      t9=q9.read()
                      protections_list.append(t9)
                      
                      

    ############# end protections##########

    ############# start modes##########

    ################# cooling only##############
    if Control=="Fresh":
      coolig_mode="COOLF"
    else:
      coolig_mode="COOLR"

    with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/modes/"+coolig_mode+".txt","r") as q10:
                      t10=q10.read()
                      cool_modes_list.append(t10)
    ##################### heat pump#######################
    if Mode=="Heat pump":
      heatpump_mode="HEATPUMP"

      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/modes/"+heatpump_mode+".txt","r") as q10a:
                      t10a=q10a.read()
                      heatpump_modes_list.append(t10a)
    
      defrost_mode="DEFROST"

      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/modes/"+defrost_mode+".txt","r") as q10b:
                      t10b=q10b.read()
                      defrost_modes_list.append(t10b)

    ################## heater #########################
    if Heater=="Heating":
      heating_mode="HEATER FOR HEAT"
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/modes/"+heating_mode+".txt","r") as q10:
                      t10=q10.read()
                      heat_modes_list.append(t10)
    elif Heater=="Dehumidifiction(Reheat)":
      heating_mode="HEATER FOR DEHUM"
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/modes/"+heating_mode+".txt","r") as q10:
                      t10=q10.read()
                      heat_modes_list.append(t10)
    
    elif Heater=="Heating & Dehumidifiction":
      heating_mode1="HEATER FOR HEAT"
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/modes/"+heating_mode1+".txt","r") as q10:
                      t10=q10.read()
                      heat1_modes_list.append(t10)
      
      heating_mode2="HEATER FOR DEHUM"
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/modes/"+heating_mode2+".txt","r") as q11:
                      t11=q11.read()
                      heat2_modes_list.append(t11)

    elif Heater=="Supplement for Heat pump":
      heating_mode="HP HEATER SUPPLEMENT"
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/modes/"+heating_mode+".txt","r") as q10:
                      t10=q10.read()
                      heat_modes_list.append(t10)
    
    elif Heater=="Supplement for Heat pump & Dehumidification":
      heating_mode1="HP HEATER SUPPLEMENT"
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/modes/"+heating_mode1+".txt","r") as q10:
                      t10=q10.read()
                      heat_modes_list.append(t10)
      heating_mode2="HEATER FOR DEHUM"
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/modes/"+heating_mode2+".txt","r") as q11:
                      t11=q11.read()
                      heat2_modes_list.append(t11)

    ############ dampers ##############
    if Dampers=="Mixing":
      Dampers_mode="Mixing box"
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/options/"+Dampers_mode+".txt","r") as q30:
                      t30=q30.read()
                      Dampers_modes_list.append(t30)
                      
    elif Dampers=="Economizer":
      Dampers_mode="Economizer"
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/options/"+Dampers_mode+".txt","r") as q30:
                      t30=q30.read()
                      Dampers_modes_list.append(t30)

    ############# end modes#################


    # CREATE new txt file for sensors
    if special_sensors:
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors.txt","w") as k1:
        for s1 in range (0,len(sensors_list)):
          q=sensors_list[s1].replace("\r","")
          k1.write(q)
    else:
      with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors.txt","w") as k1:
        for s1 in range (0,len(sensors_list)):
            k1.write(sensors_list[s1]+"\n")
    
    # CREATE new txt file for protections
    with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/protections.txt","w") as k2:
      for s2 in range (0,len(protections_list)):
          k2.write(protections_list[s2])
    
    # CREATE new txt file for cooling mode
    with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/cooling_mode.txt","w") as k3:
      for s3 in range (0,len(cool_modes_list)):
          k3.write(cool_modes_list[s3])
    
    # CREATE new txt file for heating mode
    with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/heating_mode.txt","w") as k4:
      for s4 in range (0,len(heat_modes_list)):
          k4.write(heat_modes_list[s4])

    # CREATE new txt file for heating mode (heat+dehum)
    with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/heating_mode1.txt","w") as k5:
      for s5 in range (0,len(heat1_modes_list)):
          k5.write(heat1_modes_list[s5])

    with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/heating_mode2.txt","w") as k6:
      for s6 in range (0,len(heat2_modes_list)):
          k6.write(heat2_modes_list[s6])

    # CREATE new txt file for (heatpump+supplementary)
    with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/heatpump_mode.txt","w") as k7:
      for s7 in range (0,len(heatpump_modes_list)):
          k7.write(heatpump_modes_list[s7])
      for s8 in range (0,len(heat_modes_list)):
          k7.write(heat_modes_list[s8])
    
      
    
    
    # CREATE new txt file for defrost
    with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/defrost_mode.txt","w") as k8:
      for s8 in range (0,len(defrost_modes_list)):
          k8.write(defrost_modes_list[s8])
    
    # convert txt file to pdf

    #create PDF object
    
    # pdf = PDF(orientation = 'P', unit = 'mm', format='A4')
    pdf=PDF(Project_Name,country,rev)
    pdf.alias_nb_pages()
    #set auto page break
    pdf.set_auto_page_break(auto=True,margin=18)
    #add page
    pdf.add_page()

    ###########################
    pdf.set_font('Arial', 'B', 15)
    pdf.cell(0,20,txt=Model,ln=1,align='C')
    pdf.ln(2)

    if Controller=='Carel':
      pdf.image("Z:/M.HAMMAD/PY/My_Apps/static/imgs/PCO_LOGO.png",x=40,w=130,h=80)
    else:
        pdf.image("Z:/M.HAMMAD/PY/My_Apps/static/imgs/POL.PNG",x=40,w=130,h=80)

    


    ################################
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0,20,txt='Used Sensors',ln=1,align='L')

    pdf.set_font('Arial', '', 10)
    f3 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors.txt", "r")
    for x11 in f3:
      pdf.cell(0, 10,txt = x11, ln = 1, align = 'L')
    ################################
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0,20,txt='Protections',ln=1,align='L')
    

    pdf.set_font('Arial', '', 10)
    f4 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/protections.txt", "r")
    for x12 in f4:
      pdf.cell(0, 10,txt = x12, ln = 1, align = 'L')
    ################################
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0,20,txt='Unit start-up',ln=1,align='L')
    

    pdf.set_font('Arial', '', 10)
    f5 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/STARTUP.txt", "r")
    for x13 in f5:
      pdf.cell(0, 10,txt = x13, ln = 1, align = 'L')
    ################################
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0,20,txt='System start-up',ln=1,align='L')
    

    pdf.set_font('Arial', '', 10)
    f5 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/SYSTEMSTART.txt", "r")
    for x13 in f5:
      pdf.cell(0, 10,txt = x13, ln = 1, align = 'L')

    ################################
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0,20,txt='Unit\'s operations modes',ln=1,align='L')
    

    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0,8,txt='Cooling Mode:',ln=1,align='L')

    pdf.set_font('Arial', '', 10)
    f6 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/cooling_mode.txt", "r")
    for x14 in f6:
      pdf.cell(0, 10,txt = x14, ln = 1, align = 'L')
    pdf.image("Z:/M.HAMMAD/PY/My_Apps/static/imgs/COMPRESSORS_FUNCTION.png",x=50,w=80)

    if Mode=="Cooling only" and Heater=="Heating":
      pdf.set_font('Arial', 'B', 10)
      pdf.cell(0,8,txt='Heating Mode:',ln=1,align='L')
      pdf.set_font('Arial', '', 10)
      f7 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/heating_mode.txt", "r")
      for x15 in f7:
          pdf.cell(0, 10,txt = x15, ln = 1, align = 'L')
    elif Mode=="Cooling only" and Heater=="Dehumidifiction(Reheat)":
      pdf.set_font('Arial', 'B', 10)
      pdf.cell(0,8,txt='Dehumidifiction Mode:',ln=1,align='L')
      pdf.set_font('Arial', '', 10)
      f7 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/heating_mode.txt", "r")
      for x15 in f7:
          pdf.cell(0, 10,txt = x15, ln = 1, align = 'L')
    elif Mode=="Cooling only" and Heater=="Heating & Dehumidifiction":
      pdf.set_font('Arial', 'B', 10)
      pdf.cell(0,8,txt='Heating Mode:',ln=1,align='L')
      pdf.set_font('Arial', '', 10)
      f7 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/heating_mode1.txt", "r")
      for x15 in f7:
          pdf.cell(0, 10,txt = x15, ln = 1, align = 'L')
      
      pdf.set_font('Arial', 'B', 10)
      pdf.cell(0,8,txt='Dehumidifiction Mode:',ln=1,align='L')
      pdf.set_font('Arial', '', 10)
      f8 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/heating_mode2.txt", "r")
      for x16 in f8:
          pdf.cell(0, 10,txt = x16, ln = 1, align = 'L')
    

    elif Mode=="Heat pump" and Heater=="Supplement for Heat pump" :
      pdf.set_font('Arial', 'B', 10)
      pdf.cell(0,8,txt='Heat pump Mode:',ln=1,align='L')
      pdf.set_font('Arial', '', 10)
      f7 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/heatpump_mode.txt", "r")
      for x15 in f7:
          pdf.cell(0, 10,txt = x15, ln = 1, align = 'L')

      pdf.set_font('Arial', 'B', 10)
      pdf.cell(0,8,txt='Defrost Mode:',ln=1,align='L')
      pdf.set_font('Arial', '', 10)
      f8 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/defrost_mode.txt", "r")
      for x16 in f8:
          pdf.cell(0, 10,txt = x16, ln = 1, align = 'L')
      
      # print("tete")
    

    elif Mode=="Heat pump" and Heater=="Supplement for Heat pump & Dehumidification" :
      pdf.set_font('Arial', 'B', 10)
      pdf.cell(0,8,txt='Heat pump Mode:',ln=1,align='L')
      pdf.set_font('Arial', '', 10)
      f7 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/heatpump_mode.txt", "r")
      for x15 in f7:
          pdf.cell(0, 10,txt = x15, ln = 1, align = 'L')

      pdf.set_font('Arial', 'B', 10)
      pdf.cell(0,8,txt='Defrost Mode:',ln=1,align='L')
      pdf.set_font('Arial', '', 10)
      f8 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/defrost_mode.txt", "r")
      for x16 in f8:
          pdf.cell(0, 10,txt = x16, ln = 1, align = 'L')
      

      pdf.set_font('Arial', 'B', 10)
      pdf.cell(0,8,txt='Dehumidifiction Mode:',ln=1,align='L')
      pdf.set_font('Arial', '', 10)
      f9 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/heating_mode2.txt", "r")
      for x17 in f9:
          pdf.cell(0, 10,txt = x17, ln = 1, align = 'L')
    
      
      

    elif Mode=="Heat pump"  :
      pdf.set_font('Arial', 'B', 10)
      pdf.cell(0,8,txt='Heat pump Mode:',ln=1,align='L')
      pdf.set_font('Arial', '', 10)
      f7 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/heatpump_mode.txt", "r")
      for x15 in f7:
          pdf.cell(0, 10,txt = x15, ln = 1, align = 'L')
      pdf.set_font('Arial', 'B', 10)
      pdf.cell(0,8,txt='Defrost Mode:',ln=1,align='L')
      pdf.set_font('Arial', '', 10)
      f8 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/defrost_mode.txt", "r")
      for x16 in f8:
          pdf.cell(0, 10,txt = x16, ln = 1, align = 'L')

    else:
      pass 
      
      




    ################################
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0,20,txt='Compressors timing',ln=1,align='L')

    pdf.set_font('Arial', '', 10)
    f7 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/COMPRESSORSTIMING.txt", "r")
    for x15 in f7:
      pdf.multi_cell(0,10,txt=x15,border = 0,align='L')
    
    ################################
    if Supply=="Supply VFD with PT":
      pdf.set_font('Arial', 'B', 12)
      pdf.cell(0,20,txt='Supply fan speed control ',ln=1,align='L')

      pdf.set_font('Arial', '', 10)
      f7a1 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/options/VFD on supply(PT).txt", "r")
      for x15a1 in f7a1:
          pdf.multi_cell(0,10,txt=x15a1,border = 0,align='L')
      
      
    elif Supply=="Supply EC fan motor":
      pdf.set_font('Arial', 'B', 12)
      pdf.cell(0,20,txt='Supply fan speed control ',ln=1,align='L')

      pdf.set_font('Arial', '', 10)
      f7a1 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/options/EC.txt", "r")
      for x15a1 in f7a1:
          pdf.multi_cell(0,10,txt=x15a1,border = 0,align='L')
      
      
    else:
      pass

    ################################
    if Exhaust=="Exhaust VFD with PT":
      pdf.set_font('Arial', 'B', 12)
      pdf.cell(0,20,txt='Exhaust fan speed control ',ln=1,align='L')

      pdf.set_font('Arial', '', 10)
      f7a1 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/options/VFD on return(PT).txt", "r")
      for x15a1 in f7a1:
          pdf.multi_cell(0,10,txt=x15a1,border = 0,align='L')
    
    elif Exhaust=="Exhaust EC fan motor":
      pdf.set_font('Arial', 'B', 12)
      pdf.cell(0,20,txt='Exhaust fan speed control ',ln=1,align='L')

      pdf.set_font('Arial', '', 10)
      f7a1 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/options/EC.txt", "r")
      for x15a1 in f7a1:
          pdf.multi_cell(0,10,txt=x15a1,border = 0,align='L')
    
    elif Exhaust=="STD Exhaust":
      pdf.set_font('Arial', 'B', 12)
      pdf.cell(0,20,txt='Exhaust fan',ln=1,align='L')

      pdf.set_font('Arial', '', 10)
      f7a1 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/options/Exhaust-Return.txt", "r")
      for x15a1 in f7a1:
          pdf.multi_cell(0,10,txt=x15a1,border = 0,align='L')
    else:
      pass
    ################################

      
    ################################
    if Steam=="Steam_Yes":
      pdf.set_font('Arial', 'B', 12)
      pdf.cell(0,20,txt='Steam Humidifier ',ln=1,align='L')

      pdf.set_font('Arial', '', 10)
      f7a1 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/options/Steam.txt", "r")
      for x15a1 in f7a1:
          pdf.multi_cell(0,10,txt=x15a1,border = 0,align='L')
          # pdf.cell(0, 10,txt = x15, ln = 1, align = 'L')
      
    ################################
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0,20,txt='Condenser Fans ',ln=1,align='L')

    pdf.set_font('Arial', '', 10)
    f7a = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/CONDENSERFANS.txt", "r")
    for x15a in f7a:
      pdf.multi_cell(0,10,txt=x15a,border = 0,align='L')
      # pdf.cell(0, 10,txt = x15, ln = 1, align = 'L')

    ##############################
    if Dampers=="Mixing":
      pdf.set_font('Arial', 'B', 12)
      pdf.cell(0,20,txt='Mixing box',ln=1,align='L')

      pdf.set_font('Arial', '', 10)
      f7a1 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/options/Mixing box.txt", "r")
      for x15a1 in f7a1:
          pdf.multi_cell(0,10,txt=x15a1,border = 0,align='L')
    elif Dampers=="Economizer":
      pdf.set_font('Arial', 'B', 12)
      pdf.cell(0,20,txt='Economizer',ln=1,align='L')

      pdf.set_font('Arial', '', 10)
      f7a1 = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/options/Economizer.txt", "r")
      for x15a1 in f7a1:
          pdf.multi_cell(0,10,txt=x15a1,border = 0,align='L')
    else:
      pass
    ################################
    

    # print(options)
    if options:
      pdf.set_font('Arial', 'B', 12)
      pdf.cell(0,20,txt='Unit options',ln=1,align='L')
      for e in options:
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(0,8,txt=e,ln=1,align='L')

        pdf.set_font('Arial', '', 10)
        with open("Z:/M.HAMMAD/PY/My_Apps/static/txt/options/"+e+".txt","r") as f:
            z=f.read()
            # pdf.cell(0,10,txt=z,ln=1,align='L')
            pdf.multi_cell(0,10,txt=z,border = 0,align='L')
        if e=="Extended Keypad(PGD)":
            pdf.image("Z:/M.HAMMAD/PY/My_Apps/static/imgs/PGD.png",w=90,h=60)
            pdf.image("Z:/M.HAMMAD/PY/My_Apps/static/imgs/RJ12.png",w=90,h=80)
        if e=="TH Tune":
            pdf.image("Z:/M.HAMMAD/PY/My_Apps/static/imgs/THTUNE.png",w=60,h=60)
        
        if e=="Extended Keypad":
            pdf.image("Z:/M.HAMMAD/PY/My_Apps/static/imgs/POL_KEYPAD.PNG",w=90,h=60)


    if custom_sequence:
      pdf.set_font('Arial', 'B', 10)
      pdf.cell(0,20,txt=custom_sequence_title,ln=1,align='L')
      pdf.ln(1)
      pdf.set_font('Arial', '', 10)
      pdf.multi_cell(200,6,custom_sequence,border = 0,align='L')
    
    

    ################################
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0,20,txt='Alarm Management',ln=1,align='L')

    pdf.set_font('Arial', '', 10)
    f7a = open("Z:/M.HAMMAD/PY/My_Apps/static/txt/ALARMMANAGEMENT.txt", "r")
    for x15a in f7a:
      pdf.multi_cell(0,10,txt=x15a,border = 0,align='L')
      # pdf.cell(0, 10,txt = x15, ln = 1, align = 'L')
          
      

    

    ###############################

    #### export pdf file
    pdf.output(f"Z:/M.HAMMAD/SOO OUTPUT/{Project_Name}-{country}.pdf")
    #### convert PDF file to binary to save it in SQL
    time.sleep(2)
    with open(f"Z:/M.HAMMAD/SOO OUTPUT/{Project_Name}-{country}.pdf", "rb") as pdf_file:
      encoded_string = base64.b64encode(pdf_file.read())
    
    ##save it to SQL
    save_soo(username,country,Project_Name,encoded_string,rev)
    

        
  if  'Send Email' in request.form:
    add_count()
    mail_SOO(username,f"Z:/M.HAMMAD/SOO OUTPUT/{Project_Name}-{country}.pdf")
    return render_template("sequence.html",username=username) 

  elif  'Generate SOO' in request.form:
    add_count()
    ### DOWNLOAD THE FILE
    return send_file(f"Z:/M.HAMMAD/SOO OUTPUT/{Project_Name}-{country}.pdf",as_attachment=True)
  
         
  else:
 
    return render_template("sequence.html",username=username)
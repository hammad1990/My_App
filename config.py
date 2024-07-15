import os
DEBUG=True
SECRET_KEY='111'  # this is used for flash messages
PORT=5000
class Config:
    
    
    #we must put below variables in class in order to allow me call it from anywhere.
    #Note that we changed the Driver from: "SQL Native ..etc" , to "ODBC Driver 17 for SQL Server"
    #and i can find this string inside ODBC Data source 32 file/driver tap/go down
    
    #MY LAPTOP DATA BASE:
    # DATABASE_PARAMETER='Driver={ODBC Driver 17 for SQL Server};Server=DESKTOP-SR0QC2P\SQLEXPRESS;Database=usersDB;Trusted_Connection=yes;use_unicode=True;charset="utf8"'
    
    #PETRA DATA BASE:
    DATABASE_PARAMETER='Driver={SQL Server Native Client 11.0};Server=PEEDM-HAMAD;Database=usersDB;Trusted_Connection=yes;use_unicode=True;charset="utf8"'

    #GOOGLE CHROME PATH IN my laptop(open_soo.py):
    # chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

    #GOOGLE CHROME PATH IN PETRA(open_soo.py):
    chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    #all_images IMAGE IN my laptop(sequence.py):
    # all_images="C:/Users/Mohammed_Hammad/Documents/my python files/My_Apps/static/imgs/"

    #all_images  IN PETRA(sequence.py):
    all_images="Z:/M.HAMMAD/PY/My_Apps/static/imgs/"



    #all_txt in laptop(sequence.py):
    # all_txt="C:/Users/Mohammed_Hammad/Documents/my python files/My_Apps/static/txt/"

    #all_txt in PETRA(sequence.py):
    all_txt="Z:/M.HAMMAD/PY/My_Apps/static/txt/"


     #text sensors in laptop(sequence.py):
    # all_sensors="C:/Users/Mohammed_Hammad/Documents/my python files/My_Apps/static/txt/sensors/"

    #text sensors in PETRA(sequence.py):
    all_sensors="Z:/M.HAMMAD/PY/My_Apps/static/txt/sensors/"

    #text protections in laptop(sequence.py):
    # all_protections="C:/Users/Mohammed_Hammad/Documents/my python files/My_Apps/static/txt/protections/"

    #text protections in PETRA(sequence.py):
    all_protections="Z:/M.HAMMAD/PY/My_Apps/static/txt/protections/"

    #text modes in laptop(sequence.py):
    # all_modes="C:/Users/Mohammed_Hammad/Documents/my python files/My_Apps/static/txt/modes/"

    #text modes in PETRA(sequence.py):
    all_modes="Z:/M.HAMMAD/PY/My_Apps/static/txt/modes/"

     #text options in laptop(sequence.py):
    # all_options="C:/Users/Mohammed_Hammad/Documents/my python files/My_Apps/static/txt/options/"

    #text options in PETRA(sequence.py):
    all_options="Z:/M.HAMMAD/PY/My_Apps/static/txt/options/"


    ### now we will create dynamic files for below variabales:::::::::
    
    # CREATE new txt file for sensors(works on any pcs)
    sensors= os.path.join(os.getcwd(),'static\\txt','sensors.txt')

    # CREATE new txt file for protections(works on any pcs)
    protections= os.path.join(os.getcwd(),'static\\txt','protections.txt')
    # CREATE new txt file for modes(works on any pcs)
    modes= os.path.join(os.getcwd(),'static\\txt\\')

   



    #SOO OUTPUT in laptop(sequence.py):
    # SOO_OUTPUT="C:/Users/Mohammed_Hammad/Documents/my python files/SOO OUTPUT/"

    #SOO OUTPUT in PETRA(sequence.py):
    SOO_OUTPUT="Z:/M.HAMMAD/SOO OUTPUT/"

    #saved_inquiries in laptop(RFQ.py):
    # saved_inquiries="C:/Users/Mohammed_Hammad/Documents/my python files/saved_inquiries/"

    #saved_inquiries in PETRA(RFQ.py):
    saved_inquiries="Z:/M.HAMMAD/saved_inquiries/"

    #RFQ in laptop(RFQ.py):
    # RFQs="C:/Users/Mohammed_Hammad/Documents/my python files/RFQs/"

    #RFQ in PETRA(RFQ.py):
    RFQs="Z:/M.HAMMAD/RFQs/"

    #fonts in laptop:
    # fonts="C:/Users/Mohammed_Hammad/Documents/my python files/My_Apps/static/fonts/"

    #fonts in PETRA:
    fonts="Z:/M.hammad/PY/My_Apps/static/fonts/"

    #downloaded Excel from searching codes in PETRA(find_code.py):
    Downloaded_excel="C:/Users/m-hammad/Downloads/"

    #downloaded Excel from searching codes in Laptop(find_code.py):
    # Downloaded_excel="C:/Users/m-hammad/Downloads/"
   

   

    
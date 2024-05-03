import pyodbc

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=SRV-ERP11DB;'
                      'Database=ERP11LIVE;'
                      'UID=Rep;'
                       'PWD=')


cursor=conn.cursor()
print("connected")
query=("EXEC SSRS_ProcurmentPartSupplier ?,?,?,?")
cursor.execute(query,"abb","","","")

while cursor.nextset():
    try: 
        rows = cursor.fetchall()
        print("yesss")

        break
    except:
        print("problemm")
    
        
                        
      

conn.commit()
conn.close()
if rows:
    print("there is rows")
    print(rows[0])
else:
    print("No rows")
    

from flask import Flask

### always import the blueprint name, not the file name nor the function name
from views import *







app=Flask(__name__,instance_relative_config=True)
app.config.from_object('config')
# app.config["UPLOAD_FOLDER"]="Z:/M.hammad"

app.register_blueprint(sequence)
app.register_blueprint(sequence1)
app.register_blueprint(home)
app.register_blueprint(heater)
app.register_blueprint(login)
# app.register_blueprint(register)
app.register_blueprint(pointlist)
app.register_blueprint(pointlist2)
app.register_blueprint(logout)
app.register_blueprint(components)
app.register_blueprint(RFQ)
app.register_blueprint(find_code)
app.register_blueprint(add_supplier)
# app.register_blueprint(test1)





if __name__=="__main__":
    app.run(debug=app.config['DEBUG'],host='0.0.0.0',port=app.config['PORT'],threaded=True)
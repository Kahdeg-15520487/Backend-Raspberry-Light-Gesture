from flask import request
from flask_api import FlaskAPI

Lights = {'1': False, '2': False}

app = FlaskAPI(__name__)

#check status
@app.route('/', methods=["GET"])
def api_get_all():
    return Lights
    # result = {k: represent_light_state(k) for k, v in Lights.items()}
    # return result
    
#check status
@app.route('/<id>/', methods=["GET"])
def api_get_one(id):
    return  {
                "id": id,
                #"state": represent_light_state(id)
                "state": Lights[id]
            }
  
#toggle a light
@app.route('/toggle/<id>/', methods=["GET"])
def api_toggle_light(id):
    if request.method == "GET":
        if id in Lights:
            Lights[id] = not Lights[id]
            #print(id + " is " + represent_light_state(id))
    return  {
                "id": id,
                #"state": represent_light_state(id)
                "state": Lights[id]
            }

#turn a light on
@app.route('/on/<id>/', methods=["GET"])
def api_turnon_light(id):
    if request.method == "GET":
        if id in Lights:
            Lights[id] = True
            #print(id + " is " + represent_light_state(id))
    return  {
                "id": id,
                #"state": represent_light_state(id)
                "state": Lights[id]
            }

#turn a light off
@app.route('/off/<id>/', methods=["GET"])
def api_turnoff_light(id):
    if request.method == "GET":
        if id in Lights:
            Lights[id] = False
            #print(id + " is " + represent_light_state(id))
    return  {
                "id": id,
                #"state": represent_light_state(id)
                "state": Lights[id]
            }

def represent_light_state(id):
    return ("on" if Lights[id] else "off")

if __name__ == "__main__":
    app.run()
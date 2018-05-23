from flask import Flask, render_template, request #Import for the web stuf
import json
import threading
import lakeboot as led

#Gloabl Variable for current Pattern
CURRENT_PATTERN = "No Pattern Running"

app = Flask(__name__)

def loopPattern(type):
    """Gets Called as a multiprocess and loops the code"""
    if type == 'T':
        led.runTheater()
    elif type  == "B":
        led.startUp()
    elif type == "S":
        led.staticColor(255,255,255)


@app.route("/")
def index():
    templateData = {
        'title' : 'Led Pattern Status',
        'pattern' : CURRENT_PATTERN,
    }
    return render_template('index.html',**templateData)

@app.route("/<deviceName>/")
def action(deviceName):
    CURRENT_PATTERN = "Changing"
    if deviceName == 'stop':
        CURRENT_PATTERN = 'No Pattern Running'
        led.MASTER_LOOP = False
        led.turnOff()

    if deviceName == 'bootup':
        if led.MASTER_LOOP ==  True:
            led.MASTER_LOOP = False
        led.turnOff()
        CURRENT_PATTERN = 'Bootup'
        led.MASTER_LOOP = True
        t = threading.Thread(target=loopPattern, args=("B"))
        t.daemon = True
        t.start()

    if deviceName == 'TheaterChase':
        if led.MASTER_LOOP == True:
            led.MASTER_LOOP = False
        led.turnOff()
        CURRENT_PATTERN = "Theater Chase"
        led.MASTER_LOOP = True
        t = threading.Thread(target=loopPattern, args=("T"))
        t.daemon = True
        t.start()
    
    if deviceName == 'StaticColor':
        if led.MASTER_LOOP == True:
            led.MASTER_LOOP = False
        led.turnOff()
        CURRENT_PATTERN = "Static Color"
        t = threading.Thread(target=loopPattern, args=("S"))
        t.daemon = True
        t.start()

    templateData = {
        'title' : 'LED Pattern Status',
        'pattern' : CURRENT_PATTERN,
    }
    return render_template('index.html', **templateData)

@app.route("/brightnessUpdate", methods=['POST'])
def brightnessUpdate():
    newBrightness = request.form.get('bright', 127, type=float)
    print("Hello")
    print(newBrightness)
    led.STRIP.setBrightness(newBrightness)

if __name__ == "__main__":
    led.startUp()
    app.run(host='0.0.0.0', port=80, debug=True)

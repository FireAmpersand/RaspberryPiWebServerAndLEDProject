from flask import Flask, render_template, request #Import for the web stuf
import json
import threading
import python.leds as led

#Gloabl Variable for current Pattern
CURRENT_PATTERN = "No Pattern Running"

app = Flask(__name__)

def loopPattern(type):
    """Gets Called as a multiprocess and loops the code"""
    if type == 'T':
        led.runTheater()
    elif type  == "B":
        led.runColorCycle()
    elif type == "S":
        led.staticColor(255,255,255)
    elif type == "R":
        led.runRave()
    elif type == "P":
        led.pong()


@app.route("/")
def index():
    templateData = {
        'title' : 'Led Pattern Status',
        'pattern' : CURRENT_PATTERN,
    }
    return render_template('index.html',**templateData)

@app.route("/<deviceName>/", methods=['GET', 'POST'])
def action(deviceName):
    CURRENT_PATTERN = "Changing"
    if request.method == 'POST':
        #led.turnOff()
        newBright = int(request.form['bright'])
        print("Setting the new brightness to: " + str(newBright))
        led.STRIP_BRIGHTNESS = newBright
        led.newBrightness()
         
    if deviceName == 'stop':
        CURRENT_PATTERN = 'No Pattern Running'
        led.MASTER_LOOP = False
        led.turnOff()

    if deviceName == 'bootup':
        if led.MASTER_LOOP ==  True:
            led.MASTER_LOOP = False
        led.turnOff()
        CURRENT_PATTERN = 'Color Cycle'
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

    if deviceName == 'Rave':
        if led.MASTER_LOOP == True:
            led.MASTER_LOOP = False
        led.turnOff()
        CURRENT_PATTERN = "Rave"
        led.MASTER_LOOP = True
        t = threading.Thread(target=loopPattern, args=("R"))
        t.daemon = True
        t.start()


    if deviceName == 'Pong':
        if led.MASTER_LOOP == True:
            led.MASTER_LOOP = False
        led.turnOff()
        CURRENT_PATTERN = "Pong"
        led.MASTER_LOOP = True
        t = threading.Thread(target=loopPattern, args=("P"))
        t.daemon = True
        t.start()

    templateData = {
        'title' : 'LED Pattern Status',
        'pattern' : CURRENT_PATTERN,
    }
    return render_template('index.html', **templateData)

@app.route('/brightnessUpdate', methods=['GET','POST'])
def brightnessUpdate():
    templateData = {
        'tilte' : 'LED Pattern Status',
        'pattern' : CURRENT_PATTERN,
    }
    print('In brightness')

    return render_template('index.html', **templateData)

if __name__ == "__main__":
    #led.startUp()
    app.run(host='0.0.0.0', port=80, debug=True)

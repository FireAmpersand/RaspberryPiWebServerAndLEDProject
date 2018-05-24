from flask import Flask, render_template, request #Import for the web stuf
import json
import threading
import python.leds as led

#Gloabl Variable for current Pattern
CURRENT_PATTERN = "No Pattern Running"

#Starting the flask app
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
    """The Defualt web page on the server"""
    templateData = {
        'title' : 'Led Pattern Status',
        'pattern' : CURRENT_PATTERN,
    }
    return render_template('index.html',**templateData)

@app.route("/<deviceName>/", methods=['GET', 'POST'])
def action(deviceName):
    """The Main route path for the server. Animations get selected here"""
    CURRENT_PATTERN = "Changing"
    
    #If The client is sending data back, run this if chunk. 
    if request.method == 'POST':
        #led.turnOff()
        
        #Getting the new brightness value from the Javascript, and printing the new value.
        newBright = int(request.form['bright'])
        print("Setting the new brightness to: " + str(newBright))
        
        #Changing the gloabl brightness variable and telling the leds to update themselves.
        led.STRIP_BRIGHTNESS = newBright 
        led.newBrightness()
         
    #Checks to see what the user has requested to be run.
    #Stops all patterns and turns the lights off
    if deviceName == 'stop':
        CURRENT_PATTERN = 'No Pattern Running'
        led.MASTER_LOOP = False
        led.turnOff()

    #Runs random patterns with random colors (Name needs to change)    
    if deviceName == 'bootup':
        
        #If There is already a pattern running, turn the lights and Master loop off
        if led.MASTER_LOOP ==  True:
            led.MASTER_LOOP = False
            led.turnOff()
        CURRENT_PATTERN = 'Color Cycle'
        
        #Restarting the Master Loop
        led.MASTER_LOOP = True
        
        #Threading to allow it to run in the background
        t = threading.Thread(target=loopPattern, args=("B"))
        t.daemon = True
        t.start()

    #Runs the Theater Chase Animation    
    if deviceName == 'TheaterChase':
        
       #If There is already a pattern running, turn the lights and Master loop off
       if led.MASTER_LOOP == True:
           led.MASTER_LOOP = False
           led.turnOff()
       CURRENT_PATTERN = "Theater Chase"
    
       #Restarting the Master Loop
       led.MASTER_LOOP = True
    
       #Threading to allow it to run in the background
       t = threading.Thread(target=loopPattern, args=("T"))
       t.daemon = True
       t.start()
   
    #Sets all the leds to one static color
    if deviceName == 'StaticColor':
        
       #If There is already a pattern running, turn the lights and Master loop off 
       if led.MASTER_LOOP == True:
           led.MASTER_LOOP = False
           led.turnOff()
       CURRENT_PATTERN = "Static Color"
    
       #Threading to allow it to run in the background
       t = threading.Thread(target=loopPattern, args=("S"))
       t.daemon = True
       t.start()

    #Runs the Rave Animation, Flashing lights
    if deviceName == 'Rave':
        
        #If There is already a pattern running, turn the lights and Master loop off
        if led.MASTER_LOOP == True:
            led.MASTER_LOOP = False
            led.turnOff()
        CURRENT_PATTERN = "Rave"
        
        #Restarting the Master Loop
        led.MASTER_LOOP = True
        
        #Threading to allow it to run in the background
        t = threading.Thread(target=loopPattern, args=("R"))
        t.daemon = True
        t.start()

    #Runs the animation pong, ball bounces back and forth    
    if deviceName == 'Pong':
        
        #If There is already a pattern running, turn the lights and Master loop off 
        if led.MASTER_LOOP == True:
            led.MASTER_LOOP = False
            led.turnOff()
        CURRENT_PATTERN = "Pong"
        
        #Restarting the Master Loop
        led.MASTER_LOOP = True
        
        #Threading to allow it to run in the background
        t = threading.Thread(target=loopPattern, args=("P"))
        t.daemon = True
        t.start()

    #Creating a dictionary to send back to the webpage to use variables from this side.    
    templateData = {
        'title' : 'LED Pattern Status',
        'pattern' : CURRENT_PATTERN,
    }
    return render_template('index.html', **templateData)

if __name__ == "__main__":
    #led.startUp()
    app.run(host='0.0.0.0', port=80, debug=True)

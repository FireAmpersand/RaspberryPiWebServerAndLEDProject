from flask import Flask, render_template, request #Import for the web stuf
import json
import threading
import python.internalLEDs as iLED #Import for the inside leds
import python.externalLEDs as eLED #Import for the outside leds

#Gloabl Variable for current Pattern
CURRENT_INSIDE_PATTERN = "No Pattern Running"
CURRENT_OUTSIDE_PATTERN = "No Pattern Running"

#Starting the flask app
app = Flask(__name__)

def loopPattern(type):
    """Gets Called as a multiprocess and loops the code"""
    if type == 'A':
        iLED.runColorCycle()
    elif type == 'B':
        eLED.runColorCycle()
    elif type == 'C':
        iLED.runTheater()
    elif type == 'D':
        eLED.runTheater()
    elif type == 'E':
        iLED.staticColor(255,255,255)
    elif type == 'F':
        eLED.staticColor(255,255,255)
    elif type == 'G':
        iLED.runRave()
    elif type == 'H':
        eLED.runRave()
    elif type == 'I':
        iLED.pong()
    elif type == 'J':
        iLED.runCanadaDayAnimation()
    elif type == 'K':
        eLED.runCanadaDayAnimation()
    elif type == 'L':
        iLED.staticColor(0,255,0)
    elif type == 'M':
        eLED.staticColor(0,255,0)
    elif type == 'N':
        iLED.runTheaterGreen()
    elif type == 'O':
        eLED.runTheaterGreen()


@app.route("/")
def index():
    """The Defualt web page on the server"""
    templateData = {
        'title' : 'Led Pattern Status',
        'patternInside' : CURRENT_INSIDE_PATTERN,
        'patternOutside' : CURRENT_OUTSIDE_PATTERN,
        'lightToggle' : iLED.MOVIE_LIGHT,
    }
    return render_template('index.html',**templateData)

@app.route("/<deviceName>/", methods=['GET', 'POST'])
def action(deviceName):
    """The Main route path for the server. Animations get selected here"""
    
    #If The client is sending data back, run this if chunk. 
    if request.method == 'POST':
        #led.turnOff()
        
        #Getting the new brightness value from the Javascript, and printing the new value.
        newBright = int(request.form['bright'])
        print("Setting the new brightness to: " + str(newBright))
        
        #Changing the gloabl brightness variable and telling the leds to update themselves.
        iLED.STRIP_BRIGHTNESS = newBright 
        iLED.newBrightness()
         
    #Checks to see what the user has requested to be run.
    #Toggles the lights above the projector
    if deviceName == 'ToggleMovie':
       if iLED.MOVIE_LIGHT == True:
          iLED.MOVIE_LIGHT = False
          iLED.turnOffMovie()
       else:
          iLED.MOVIE_LIGHT = True
    
    #Stops all patterns and turns the lights off for the inside lights only
    if deviceName == 'StopInside':
        CURRENT_INSIDE_PATTERN = 'No Pattern Running'
        iLED.MASTER_LOOP = False
        iLED.turnOff()
        
    #Stops all patterns and turns the lights off for the outside lights only
    if deviceName == 'StopOutside':
        CURRENT_OUTSIDE_PATTERN = 'No Pattern Running'
        eLED.MASTER_LOOP = False
        eLED.turnOff()
        

    #Runs random patterns with random colors   
    #Inside Command
    if deviceName == 'ColorCycleInside':
        
        #If There is already a pattern running, turn the lights and Master loop off
        if iLED.MASTER_LOOP ==  True:
            iLED.MASTER_LOOP = False
            iLED.turnOff()
        CURRENT_INSIDE_PATTERN = 'Color Cycle'
        
        #Restarting the Master Loop
        iLED.MASTER_LOOP = True
        
        #Threading to allow it to run in the background
        t = threading.Thread(target=loopPattern, args=("A"))
        t.daemon = True
        t.start()
     
    #Outside Command
    if deviceName == 'ColorCycleOutside':
        
        #If There is already a pattern running, turn the lights and Master loop off
        if eLED.MASTER_LOOP ==  True:
            eLED.MASTER_LOOP = False
            eLED.turnOff()
        CURRENT_OUTSIDE_PATTERN = 'Color Cycle'
        
        #Restarting the Master Loop
        eLED.MASTER_LOOP = True
        
        #Threading to allow it to run in the background
        t = threading.Thread(target=loopPattern, args=("B"))
        t.daemon = True
        t.start()

    #Runs the Theater Chase Animation
    #Inside Command
    if deviceName == 'TheaterChaseInside':
        
       #If There is already a pattern running, turn the lights and Master loop off
       if iLED.MASTER_LOOP == True:
           iLED.MASTER_LOOP = False
           iLED.turnOff()
       CURRENT_INSIDE_PATTERN = "Theater Chase"
    
       #Restarting the Master Loop
       iLED.MASTER_LOOP = True
    
       #Threading to allow it to run in the background
       t = threading.Thread(target=loopPattern, args=("C"))
       t.daemon = True
       t.start()
    
    #Outside Command
    if deviceName == 'TheaterChaseOutside':
        
       #If There is already a pattern running, turn the lights and Master loop off
       if eLED.MASTER_LOOP == True:
           eLED.MASTER_LOOP = False
           eLED.turnOff()
       CURRENT_OUTSIDE_PATTERN = "Theater Chase"
    
       #Restarting the Master Loop
       eLED.MASTER_LOOP = True
    
       #Threading to allow it to run in the background
       t = threading.Thread(target=loopPattern, args=("D"))
       t.daemon = True
       t.start()
    
    #Runs the Theater Chase Animation
    #Inside Command
    if deviceName == 'TheaterChaseGreenInside':
        
       #If There is already a pattern running, turn the lights and Master loop off
       if iLED.MASTER_LOOP == True:
           iLED.MASTER_LOOP = False
           iLED.turnOff()
       CURRENT_INSIDE_PATTERN = "Theater Chase"
    
       #Restarting the Master Loop
       iLED.MASTER_LOOP = True
    
       #Threading to allow it to run in the background
       t = threading.Thread(target=loopPattern, args=("N"))
       t.daemon = True
       t.start()
    
    #Outside Command
    if deviceName == 'TheaterChaseGreenOutside':
        
       #If There is already a pattern running, turn the lights and Master loop off
       if eLED.MASTER_LOOP == True:
           eLED.MASTER_LOOP = False
           eLED.turnOff()
       CURRENT_OUTSIDE_PATTERN = "Theater Chase"
    
       #Restarting the Master Loop
       eLED.MASTER_LOOP = True
    
       #Threading to allow it to run in the background
       t = threading.Thread(target=loopPattern, args=("O"))
       t.daemon = True
       t.start()
   
    #Sets all the leds to one static color
    #Inside Command
    if deviceName == 'StaticColorInside':
        
       #If There is already a pattern running, turn the lights and Master loop off 
       if iLED.MASTER_LOOP == True:
           iLED.MASTER_LOOP = False
           iLED.turnOff()
       CURRENT_INSIDE_PATTERN = "Static Color"
    
       #Threading to allow it to run in the background
       t = threading.Thread(target=loopPattern, args=("E"))
       t.daemon = True
       t.start()
    
    #Outside Command
    if deviceName == 'StaticColorOutside':
        
       #If There is already a pattern running, turn the lights and Master loop off 
       if eLED.MASTER_LOOP == True:
           eLED.MASTER_LOOP = False
           eLED.turnOff()
       CURRENT_OUTSIDE_PATTERN = "Static Color"
    
       #Threading to allow it to run in the background
       t = threading.Thread(target=loopPattern, args=("F"))
       t.daemon = True
       t.start()
    
    #Sets all the leds to one static color
    #Inside Command
    if deviceName == 'StaticColorGreenInside':
        
       #If There is already a pattern running, turn the lights and Master loop off 
       if iLED.MASTER_LOOP == True:
           iLED.MASTER_LOOP = False
           iLED.turnOff()
       CURRENT_INSIDE_PATTERN = "Static Color"
    
       #Threading to allow it to run in the background
       t = threading.Thread(target=loopPattern, args=("L"))
       t.daemon = True
       t.start()
    
    #Outside Command
    if deviceName == 'StaticColorGreenOutside':
        
       #If There is already a pattern running, turn the lights and Master loop off 
       if eLED.MASTER_LOOP == True:
           eLED.MASTER_LOOP = False
           eLED.turnOff()
       CURRENT_OUTSIDE_PATTERN = "Static Color"
    
       #Threading to allow it to run in the background
       t = threading.Thread(target=loopPattern, args=("M"))
       t.daemon = True
       t.start()

    #Runs the Rave Animation, Flashing lights
    #Inside Command
    if deviceName == 'RaveInside':
        
        #If There is already a pattern running, turn the lights and Master loop off
        if iLED.MASTER_LOOP == True:
            iLED.MASTER_LOOP = False
            iLED.turnOff()
        CURRENT_INSIDE_PATTERN = "Rave"
        
        #Restarting the Master Loop
        iLED.MASTER_LOOP = True
        
        #Threading to allow it to run in the background
        t = threading.Thread(target=loopPattern, args=("G"))
        t.daemon = True
        t.start()
       
    #Outside Command
    if deviceName == 'RaveOutside':
        
        #If There is already a pattern running, turn the lights and Master loop off
        if eLED.MASTER_LOOP == True:
            eLED.MASTER_LOOP = False
            eLED.turnOff()
        CURRENT_OUTSIDE_PATTERN = "Rave"
        
        #Restarting the Master Loop
        eLED.MASTER_LOOP = True
        
        #Threading to allow it to run in the background
        t = threading.Thread(target=loopPattern, args=("H"))
        t.daemon = True
        t.start()

    #Runs the animation pong, ball bounces back and forth    
    if deviceName == 'Pong':
        
        #If There is already a pattern running, turn the lights and Master loop off 
        if iLED.MASTER_LOOP == True:
            iLED.MASTER_LOOP = False
            iLED.turnOff()
        CURRENT_INSIDE_PATTERN = "Pong"
        
        #Restarting the Master Loop
        iLED.MASTER_LOOP = True
        
        #Threading to allow it to run in the background
        t = threading.Thread(target=loopPattern, args=("I"))
        t.daemon = True
        t.start()

    if deviceName == 'CanadaInside':
        
        #If There is already a pattern running, turn the lights and Master loop off 
        if iLED.MASTER_LOOP == True:
            iLED.MASTER_LOOP = False
            iLED.turnOff()
        CURRENT_INSIDE_PATTERN = "Canada Day"
        
        #Restarting the Master Loop
        iLED.MASTER_LOOP = True
        
        #Threading to allow it to run in the background
        t = threading.Thread(target=loopPattern, args=("J"))
        t.daemon = True
        t.start()
        
    if deviceName == 'CanadaOutside':
        
        #If There is already a pattern running, turn the lights and Master loop off 
        if eLED.MASTER_LOOP == True:
            eLED.MASTER_LOOP = False
            eLED.turnOff()
        CURRENT_OUTSIDE_PATTERN = "Canada Day"
        
        #Restarting the Master Loop
        eLED.MASTER_LOOP = True
        
        #Threading to allow it to run in the background
        t = threading.Thread(target=loopPattern, args=("K"))
        t.daemon = True
        t.start()
        
    #Creating a dictionary to send back to the webpage to use variables from this side.    
    templateData = {
        'title' : 'LED Pattern Status',
        'patternInside' : "Placeholder Text",
        'patternOutside' : "Placeholder Text",
        'lightToggle' :iLED.MOVIE_LIGHT,
    }
    return render_template('index.html', **templateData)

if __name__ == "__main__":
    iLED.startUp()
    app.run(host='0.0.0.0', port=80, debug=True)

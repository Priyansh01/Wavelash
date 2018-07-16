import pyrebase
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

config = {
    "apiKey": "AIzaSyCqMIQKYw4ul4DCb3WRYu5hlIltNKgNMns",
  "authDomain": "intellih-3917b.firebaseapp.com",
  "databaseURL": "https://intellih-3917b.firebaseio.com/",
  "storageBucket": "gs://intellih-3917b.appspot.com/",
  "serviceAccount": "/home/pi/Project/Pyrebase/intellih-3917b-firebase-adminsdk-8dxjx-087469c3a1.json"
     }
firebase = pyrebase.initialize_app(config)
print ("Configured")
db= firebase.database()

def init_pins():
    GPIO.output(5,GPIO.LOW)
    GPIO.output(6,GPIO.LOW)
    GPIO.output(9,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)

    return

def bedroom():
    light_br = db.child("bedroom").child("light").get()
    fan_br = db.child("bedroom").child("fan").get()
    if(int(light_br.val()))==1:
        GPIO.output(9,1)
        
    elif(int(light_br.val()))==0:
        GPIO.output(9,0)
        
    if(int(fan_br.val()))==1:
        GPIO.output(11,1)
    elif(int(fan_br.val()))==0:
        GPIO.output(11,0)

def drawingroom():
    light_dr = db.child("drawingroom").child("light").get()
    fan_dr = db.child("drawingroom").child("fan").get()
    if(int(light_dr.val()))==1:
        GPIO.output(5,1)
    elif(int(light_dr.val()))==0:
        GPIO.output(5,0)
        
    if(int(fan_dr.val()))==1:
        GPIO.output(6,1)
    elif(int(fan_dr.val()))==0:
        GPIO.output(6,0)
    
def main():
    init_pins()

    while True:
        bedroom()
        drawingroom()

main()

import pyrebase
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.IN)
GPIO.setup(16,GPIO.IN)
GPIO.setup(18,GPIO.IN)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


def pir_outer():
    i=GPIO.input(4)
    if i==1:    #When output from motion sensor is LOW
        GPIO.output(19, 1)  #Turn OFF LED  
        print("updated on intruder detection")
            
    elif i==0:  #When output from motion sensor is HIGH
        GPIO.output(19, 0)  #Turn ON LED 
        print("updated on no detection")

    return i

def room_location():
    pir_out=GPIO.input(18)
    pir_in=0
    if pir_out==0:
        GPIO.output(26, 0)
             
    elif pir_out==1:
        print ("Outer Pir = 1")
        time.sleep(1)
        pir_in = GPIO.input(16)
        if pir_in==1:
            GPIO.output(26,1)
            print("User is present in room")
    return pir_in
    
    
config = {
    "apiKey": "AIzaSyCqMIQKYw4ul4DCb3WRYu5hlIltNKgNMns",
  "authDomain": "intellih-3917b.firebaseapp.com",
  "databaseURL": "https://intellih-3917b.firebaseio.com/",
  "storageBucket": "gs://intellih-3917b.appspot.com/",
  "serviceAccount": "/home/pi/Project/Pyrebase/intellih-3917b-firebase-adminsdk-8dxjx-087469c3a1.json"
     }

def main():
    firebase = pyrebase.initialize_app(config)
    print ("Configured")
    db = firebase.database()
    GPIO.output(19, 0)
    GPIO.output(26,0)
    while True:
        i=pir_outer()
        j=room_location()
        db.child("pir").update({"pir_out":i})
        db.child("pir").update({"pir_in":j})

main()



        

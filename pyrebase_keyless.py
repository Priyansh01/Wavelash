import pyrebase
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(15,GPIO.OUT)
pwm = GPIO.PWM(15,50)
pwm.start(2)

config = {
    "apiKey": "AIzaSyCqMIQKYw4ul4DCb3WRYu5hlIltNKgNMns",
  "authDomain": "intellih-3917b.firebaseapp.com",
  "databaseURL": "https://intellih-3917b.firebaseio.com/",
  "storageBucket": "gs://intellih-3917b.appspot.com/",
  "serviceAccount": "/home/pi/Project/Pyrebase/intellih-3917b-firebase-adminsdk-8dxjx-087469c3a1.json"
     }

firebase = pyrebase.initialize_app(config)
print ("Configured")
db = firebase.database()


while True:
    keyless = db.child("keyless").get()
    if (int(keyless.val())==1):
        pwm.ChangeDutyCycle(12)
        time.sleep(3)
        print ("Door Unlocked")
        db.update({"keyless":"0"})
        pwm.ChangeDutyCycle(2)
    

    

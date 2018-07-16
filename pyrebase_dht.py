import Adafruit_DHT as Adafruit_DHT
import serial
import pyrebase

def lightSensor():
    ser = serial.Serial('/dev/ttyACM0',9600)
    data = ser.readline()
    list_with_b = data.split()
    
    return list

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

    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11,21)  # GPIO27 (BCM notation)
        print ("Humidity = {} %; Temperature = {} C".format(humidity, temperature))
        db.child("sensors").update({"temperature":temperature})
        db.child("sensors").update({"humidity":humidity})
        print("values sent")

main()

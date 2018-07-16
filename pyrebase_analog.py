import serial
import time
import pyrebase

config = {
    "apiKey": "AIzaSyCqMIQKYw4ul4DCb3WRYu5hlIltNKgNMns",
  "authDomain": "intellih-3917b.firebaseapp.com",
  "databaseURL": "https://intellih-3917b.firebaseio.com/",
  "storageBucket": "gs://intellih-3917b.appspot.com/",
  "serviceAccount": "/home/pi/Project/Pyrebase/intellih-3917b-firebase-adminsdk-8dxjx-087469c3a1.json"
     }

def lightSensor():
    ser = serial.Serial('/dev/ttyACM0',9600)
    data = ser.readline()
    list = data.split()
    return list
    #return gas_list[1],light_list[1]

def main():
    firebase = pyrebase.initialize_app(config)
    print ("Configured")
    db = firebase.database()
    while True:
        myList = lightSensor()
        print (myList)
        print (myList[1])
        print (myList[0])
        gas_new=str(myList[0])
        gas_list=gas_new.split('\'')
        print (gas_list[1])
        light_new=str(myList[1])
        light_list=light_new.split('\'')
        print (light_list[1])
        db.child("sensors").update({"gas":gas_list[1]})
        db.child("sensors").update({"light":light_list[1]})
        print("values sent")

main()

    #gas_val,light_val = lightSensor()
    #print (gas_val)
    #print (light_val)


#gas=str(list[0])
 #   gas_list=gas.split('b')
  #  light=str(list[1])
   # light_list=gas.split('b')
    #time.sleep(1)

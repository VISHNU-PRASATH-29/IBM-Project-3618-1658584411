import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

#vishnu IBM
organization = "r5gra1"
deviceType = "Dora"
deviceId = "30"
authMethod = "token"
authToken = "12345678"

#Gpio

def mycommandCallback(cmd):
    print("Command Received: %s" %cmd.data['command'])
    status = cmd.data['command']
    if status=="lighton":
        print("LED is ON")
    elif status=="lightoff":
        print("LED is OFF")
    else:
        print("please send proper command")
try:
    deviceOptions = {"org":organization,"type":deviceType,"id":deviceId,"auth-method":authMethod,"auth-token":authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)

except Exception as e:
    print("Caught exception connecting device: %s" %str(e))
    sys.exit()

#CONNECCT
deviceCli.connect()

while True:
    temp=random.randint(0,100)
    hum=random.randint(0,100)

    data={'temp':temp,'hum':hum}

    def myOnPublishCallback():
        print("Published Temperature = %s C"%temp,"Humidity = %s %%" %hum, "to IBM Watson")

    success = deviceCli.publishEvent("IoTSensor","json",data,qos=0, on_publish=myOnPublishCallback)
    if not success:
        print("Not connected to IoTF")
    time.sleep(10)

    deviceCli.commandCallback = mycommandCallback

#Disconnect

deviceCli.disconnect()



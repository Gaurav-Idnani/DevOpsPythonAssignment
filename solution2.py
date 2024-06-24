#install all libraries using pip install <library name>
import psutil
import time
import keyboard

#global variable initialised to serve as a flag to record a key press by user
keyPressCheck = False
def keyPressEventHandler(event):
    print ('User Intervention Detected.Stopping CPU Monitoring')
    global keyPressCheck 
    keyPressCheck= True



def monitor_cpu_usage():
    print("Monitoring CPU usage ...")
    threshold = int(input("Please enter the CPU Uaage threshold you would like to set for monitoring: "))
    #event handler declared here to allow user to first provide the input successfully
    keyboard.on_press(keyPressEventHandler)
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold:{cpu_usage}%")
            if keyPressCheck:
                break

            time.sleep(1)
    
    except Exception as e:
        print("We ran into an issue while checking CPU Usage:"+e)


monitor_cpu_usage()


# Q2. As a DevOps engineer, it is crucial to monitor the health and performance of servers. Write a Python program to monitor the health of the CPU. Few pointers to be noted:
# The program should continuously monitor the CPU usage of the local machine. 
# If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.
# The program should run indefinitely until interrupted.
# The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.

# Hint:
# The psutil library in Python can be used to retrieve system information, including CPU usage. You can install it using pip install psutil.
# Use the psutil.cpu_percent() method to get the current CPU usage as a percentage.

# Expected Output:
# Monitoring CPU usage...
# Alert! CPU usage exceeds threshold: 85%
# Alert! CPU usage exceeds threshold: 90%
# ... (continues until interrupted) 

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


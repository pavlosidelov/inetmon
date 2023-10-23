#Internet Availability Monitoring Service
#By: @pavlosidelov
#Pavlo Sidelov
#www.sidelov.com

#Installing requests library if not available
import os
os.system('pip install requests')
os.system('pip3 install requests')

#Initializing libraries
import requests
import time
from datetime import datetime

#----------CONFIGURATION START--------------------
#Change this Log file name to whatever you want
LOG_FILE = "internet_status_log.txt"

#Change this URL to enything else you want to check availability
CHECK_URL = "https://www.google.com"

#Change this interval to whatever you want
CHECK_INTERVAL = 5  # seconds
#----------CONFIGURATION END--------------------

#Logging events
def log_event(event, status):
    with open(LOG_FILE, 'a') as f:
        now = datetime.now()
        log_entry = f"{now.strftime('%Y-%m-%d, %H:%M:%S')}, {event}, {status}\n"
        f.write(log_entry)

#Checking internet availability
def check_internet():
    try:
        now = datetime.now()
        requests.get(CHECK_URL, timeout=2)
        print("Response: ", now.strftime('%Y-%m-%d, %H:%M:%S'))
        return True
    except requests.ConnectionError:
        print("No response...")
        return False
    except requests.Timeout:
        print("Timeout...")
        return False

#Main function
def main():
    #Get the current time
    now = datetime.now()
    internet_was_down = False
    #Log the service start
    log_event("Event", "Service Started")

    #Check internet availability and log the status
    while True:
        #Interrupt the service by pressing Ctrl+C
        try:
            #Check internet availability and log the status
            now = datetime.now()
            # Check internet availability
            has_internet = check_internet()
            # Log the internet availability
            if not has_internet and not internet_was_down:
                log_event("Event", "Internet Down")
                print("Internet is down: ", now.strftime('%Y-%m-%d, %H:%M:%S'))
                internet_was_down = True
                # Generate system beep sound

            elif has_internet and internet_was_down:
                log_event("Event", "Internet Restored")
                print("Internet is restored: ", now.strftime('%Y-%m-%d, %H:%M:%S'))
                internet_was_down = False

            # Sleep for the check interval
            time.sleep(CHECK_INTERVAL)
        except KeyboardInterrupt:
            log_event("Event", "Service Stopped")
            print("Service stopped.")
            break
        except Exception as e:
            print("EXCEPTION! : ", e)
            continue


#Run the main function
if __name__ == "__main__":
    print("------------------------------------------------")
    print("Internet Availability Monitoring Service")
    print("By: @pavlo_sidelov")
    print("Logging to file: ", LOG_FILE)
    print("Checking URL: ", CHECK_URL)
    print("Checking interval: ", CHECK_INTERVAL, " seconds")
    print("Press Ctrl+C to stop the service.")
    print("------------------------------------------------")
    print("Starting the service...")
    main()
    print("Service stopped.")

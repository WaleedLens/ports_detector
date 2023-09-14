'''
 This is the Main file for Ports Spikes detection.
 The idea behind this project is to counter suspicious spikes of requests which could damage the system.
 In This project User is required to define ports that he wants to monitor , in this monitoring proccess the system would monitor and detect any sudden spike in requests to certain service
 (Port of that service should be provided by the user). In case of successfull detection of suspecious spikes to a service, the system will take counter acts based on user preference; This includes:
 
 1- Alert system admins through (email,sms message,slack/discord)
 
 2- Shutdown the service 

'''
from colorama import Fore
import re
from monitor.monitor_controller import MonitorController 
from service.service_controller import ServiceController
from db.psql_client import PostgresqlClient
def __init__():
    print("########################### Welcome to Waleed System ###########################")
    print("Please Select Any option ")
    options_dict = options() 
    for a in options_dict:
        print(a)
    
    
    option = input(Fore.YELLOW+"Select -> ")
    validate_input(option)
    
    process_option(options_dict.get(list(options_dict.keys())[int(option)]))



def process_option(option):
    print("This is option")
    
    obj = PostgresqlClient()
    obj.connect()


def options():
    options_list = {
        "1: Show monitored services" : MonitorController,
        "2: Add new service":ServiceController,
        "3: Edit service" : ServiceController,
        "4: Insights Of services" : MonitorController
    }
    return options_list



def validate_input(option):
    validate = re.match(r'^([\s\d]+)$', option)
    if not validate:
        raise ValueError("You must provide numbers available in the options only")
    return validate

if __name__ == "__main__":
    __init__()
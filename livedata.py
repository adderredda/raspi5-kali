import psutil
import os
from colorama import Fore, Style
from time import sleep

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_sensor_data():
    sensors_data = os.popen('sensors').read()
    return sensors_data

while True:
    cpu_usage = get_cpu_usage()
    sensor_data = get_sensor_data()

    # Clear the screen before displaying the most recent data
    print("\033[H\033[J")
    
    print(Fore.RED + f"CPU Usage: {cpu_usage}%" + Style.RESET_ALL)
    print(Fore.RED + sensor_data + Style.RESET_ALL)

    sleep(.5)

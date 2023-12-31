"""
A inventory script to collect hardware information of the current local host to file.
Works on MS Windows  semoi-automatically and offline.
"""

import os
import wmi
import subprocess
import psutil
 
def uniqueFilename(path):
    filename, extension = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1
    return path


with open(uniqueFilename("host.txt"),"w") as filereport:
    # Ask for manual information
    room = input("Room:")
    filereport.write(f"Room: {room}\n")
    invnr = input("Inventory Number:")
    filereport.write(f"InventoryNr: {invnr}\n")
    # Collect remaining information
    cwmi = wmi.WMI()   
    host = cwmi.Win32_ComputerSystem()[0]
    filereport.write(f"Name: {host.Name}\n")
    filereport.write(f"Manufacturer: {host.Manufacturer}\n")
    filereport.write(f"Model: {host. Model}\n")
    filereport.write(f"SystemFamily: {host.SystemFamily}\n")
    biossn=subprocess.check_output('wmic bios get serialnumber').decode("utf-8").replace('SerialNumber  \r\r\n','').replace('      \r\r\n\r\r\n', '')
    filereport.write(f"Bios SN: {biossn}\n")
    username=psutil.users()[0][0]
    filereport.write(f"User currently: {username}\n")
    filereport.write("===Users===\n")
    folders=[]
    for f in os.scandir(os.path.expandvars('%USERPROFILE%\..')):
        if f.is_dir():
            if f.name not in ['All Users','Default', 'Default User','Public']:
                folders.append(f)
    folders.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    for folder in folders:
        filereport.write(f"Profile: {folder.name}\n")
    filereport.write("===NICs===\n")
    filereport.write(str(psutil.net_if_addrs()))
    print("Saved!")
    
   

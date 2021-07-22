import pprint
import re

ipv4 = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

def validate_ip(ip_add):
    if(re.search(ipv4, ip_add)):
        lines = f.readlines()
        for line in lines:
            if ip in line:
                pprint(line)
    else:
        print("Invalid IP address\n")

logfile = input("Please enter log file path: ")
try:    
    f = open(logfile, "r")
except OSError:
    print("Invalid file path\n")
    exit()
ip = input("Please enter the IP Address: ")

validate_ip(ip)

f.close()

# Written by Daniel Rochester

import socket


class Bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


print(Bcolors.HEADER + "This is a simple port scanning tool." + Bcolors.ENDC)
ip = input(Bcolors.OKBLUE + "Enter the IP to scan: " + Bcolors.ENDC)
ports = input(Bcolors.OKBLUE + "Enter the range of ports to scan (ex 0-100): " + Bcolors.ENDC)
print()
ports = ports.split("-")
try:
    low = int(ports[0]) # These are the port numbers to check
    high = int(ports[1])
except Exception:
    print(Bcolors.WARNING + "[-] Invalid port values." + Bcolors.ENDC)
    exit()

# If the values are not in the right order, this flips the two values
if low > high:
    temp = high
    high = low
    low = temp

if low < 0 or high < 0:
    print(Bcolors.WARNING + "[-] Invalid port range entered." + Bcolors.ENDC)
    exit()

# This checks to make sure the ip entered is of a normal length
ipLength = len(ip)
if ipLength > 15 or ipLength < 7:
    print(Bcolors.WARNING + "[-] An invalid IP was entered." + Bcolors.ENDC)
    exit()

for i in range(low, high+1, 1):
    soc = socket.socket()
    responseCode = soc.connect_ex((ip, i))  # This attempts to connect on the specified port, and returns a value
    if responseCode == 0:  # If the returned value is 0, the connection is possible
        print(Bcolors.OKGREEN + "Port", str(i), "is" + Bcolors.BOLD + " OPEN." + Bcolors.ENDC)
    else:
        print("Port", str(i), "is" + Bcolors.FAIL + " CLOSED." + Bcolors.ENDC)

soc.close()

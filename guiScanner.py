#!/usr/bin/env python3

from appJar import gui
import array
import socket

def scan(ip, ports, arr):
	ports = ports.split("-")
	try:
	    low = int(ports[0]) # These are the port numbers to check
	    high = int(ports[1])
	except Exception:
	    print("[-] Invalid port values.")
	    exit()

	# If the values are not in the right order, this flips the two values
	if low > high:
	    temp = high
	    high = low
	    low = temp

	if low < 0 or high < 0:
	    print("[-] Invalid port range entered.")
	    exit()

	# This checks to make sure the ip entered is of a normal length
	ipLength = len(ip)
	if ipLength > 15 or ipLength < 7:
	    print("[-] An invalid IP was entered.")
	    exit()

	for i in range(low, high+1, 1):
	    soc = socket.socket()
	    responseCode = soc.connect_ex((ip, i))  # This attempts to connect on the specified port, and returns a value
	    if responseCode == 0:  # If the returned value is 0, the connection is possible
	        arr.append(i)

	soc.close()



def press(button):
	if button == "Cancel":
		app.stop()
	else:
		ip = app.getEntry("IP Address: ")
		range = app.getEntry("Range (xx-xx): ")
		if(arrLen > 0):
			i = 0
			while i < arrLen:
				labelString = str(arr[i])
				app.removeLabel(labelString)
				i += 1
		arr = []
		scan(ip, range, arr)
		arrLen = len(arr)
		if(arrLen > 0):
			i = 0
			while i < arrLen:
				labelString = str(arr[i])
				app.addLabel(labelString)
				i += 1



app = gui("Testing Window", "600x200")
app.startFrame("LEFT", row=0, column=0)
app.setBg("white")
app.setSticky("NEW")
app.setStretch("COLUMN")
app.startLabelFrame("Details")
app.setSticky("ew")
app.addLabelEntry("IP Address: ")
app.addLabelEntry("Range (xx-xx): ")
app.stopLabelFrame()
app.addButtons(["Begin", "Cancel"], press)
app.stopFrame()
app.startFrame("RIGHT", row=0, column=1)
app.setBg("white")
app.setSticky("NEW")
app.setStretch("COLUMN")
app.addLabel("OPEN PORTS")
app.setLabelBg("OPEN PORTS", "light green")
app.startScrollPane("PORTS")
app.setFocus("IP Address: ")

app.go()

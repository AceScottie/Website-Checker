import sys
import time
from time import ctime
import urllib2 
from urllib2 import HTTPError
import datetime
import socket
from Tkinter import *
import thread

state = False
tkopen = False
attempt = 0

def tk():
	global tkopen
	tkopen = True
	app = Tk()
	app.protocol('WM_DELETE_WINDOW', close(app))
	app.title("Website Check v0.2")
	app.geometry("200x50+500+200")
	w = Label(app, text="Website is now availble")
	w.pack()
	app.mainloop()
	
def close(app):
  global tkopen
  app.withdraw()
  tkopen = False


def main():
	lasttime = "never"
	global attempt
	status = 0
	Error = ''
	nowtime = ctime().split()[3]
	global state
	site = "http://" + "www.watchcartoononline.com"
	try:
		status = urllib2.urlopen(site, timeout = 5).getcode()
	
	except urllib2.URLError, e:
		Error = e
		pass
		
	except socket.timeout, e:
		Error = e
		pass
	
	attempt +=1
	
	if status == 200:
		print ("Website is up.")
		lasttime = nowtime
		state = True
	else:
		state = False
		if status == 0:
			status = Error
			
		print ("Error Stite is down: Return %s. Attempts = %s" %(status, attempt))
		print ("last checked - %s" %nowtime)
		
	print ("Website %s was last up - %s" %(site, lasttime))
	sys.stdout.flush()
	return state
		
def start():
	global tkopen
	while True:
		main()
		if state == True:
			if tkopen == False:
				tk()
		time.sleep(5)

if __name__ == '__main__':
	start()
	

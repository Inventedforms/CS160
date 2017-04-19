#!/usr/bin/python
from uuid import getnode as get_mac
import psycopg2, globals
mac = get_mac()

def show_video():
	print """
		 <video width='320' height='576' preload controls> 
		 	<source src='../temp/alan/test.mp4' type='video/mp4'>
		 	Your browser does not support the video tag. 
		 </video>
		 """

try:
	conn = psycopg2.connect(globals.credentials) 
	cur = conn.cursor()
	mac = get_mac()
	cur.execute("SELECT Username FROM user_login WHERE MAC_Address = (%s)", [str(mac)])
	user = cur.fetchone()
	if user is None:
		print "Location:userlogin.cgi\r\n"
	else:
		print "Content-Type: text/html\r\n\r\n"    # HTML is following   
		print # blank line, end of headers
		print """      
		<!doctype html>                  
		 <html>
		 	<head>
		 		<title>User page!</title>
		 	</head>
		 <p>
		 Uploaded videos:</br>
		 """
		
		print """
		 Hi %s
		 Upload videos here. The system will only accept valid video formats (mp3, mp4, avi, mov, etc).
		 	<form enctype=multipart/form-data 
		 	id=video name=video method=post action=/cgi-bin/submission.cgi>
		 	<label for='file'>Filename:</label>
		 	<input type='file' name='file' id = 'file'/>
		 	<br />
		 	<input type='submit' name='submit' value='Submit' />
		 </form>
		 <form id=logout name=logout method=post action=/cgi-bin/logout.cgi>
		 <input type='submit' name='submit' value='Logout' />
		 <input type='hidden' name ='username' value ='username' />
		 </form>
		 </p>
		 </html>
		""" % user[0]
	cur.close()
	conn.close()
except Exception, e:
	globals.printerror(msg)
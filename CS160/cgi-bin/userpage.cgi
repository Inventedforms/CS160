#!/usr/bin/python
from uuid import getnode as get_mac
import psycopg2, globals
mac = get_mac()

def show_video(width, height, videoname, username):
	print "<video width='%s' height='%s' preload controls>" % (width, height)
	print "<source src='../temp/%s' type='video/mp4'>" % videoname
	print "Your browser does not support the video tag." 
	print "</video>"
	print "<form id=delete name=delete method=post action=/cgi-bin/removevideo.cgi>"
	print "<input type='submit' name='submit' value='Delete Video' />"
	print "<input type='hidden' name ='username' value ='%s' />" % username
	print "<input type='hidden' name ='videoname' value ='%s' />" % videoname
	print "</form>"

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
		 <html>
		 	<head>
		 		<title>User page!</title>
		 	</head>
		 <p>
		 Hi %s </br>
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
		""" % user[0]
		
		print "Uploaded videos:"
		print "<p>"
		#Loop through and display all videos
		metadata = "SELECT resolution, video_name FROM video_metadata WHERE Owner = (%s)"
		cur.execute(metadata, [user[0]])
		res = cur.fetchall()
		if not res:
			print "No uploaded videos. Upload something!"
		else:
			for data in res:
				dimensions = data[0][1:-1].split(",")
				#print dimensions
				show_video(dimensions[0], dimensions[1],data[1][19:],user)
		print "</p>"
		print "</html>"
	cur.close()
	conn.close()
except Exception, e:
	globals.printerror(msg)
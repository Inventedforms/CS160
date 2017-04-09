#!/usr/bin/python
from uuid import getnode as get_mac
import psycopg2
mac = get_mac()
user = ""
try:
	conn = psycopg2.connect("dbname='cs160' user='postgres' host='localhost' password = 'student'") 
	cur = conn.cursor()
	mac = get_mac()
	cur.execute("SELECT Username FROM user_login WHERE MAC_Address = (%s)", [str(mac)])
	user = cur.fetchone()
	if user is None:
		print "Location:userlogin.cgi\r\n"
	else:
		print "Content-Type: text/html\r\n\r\n"    # HTML is following   
		print                        # blank line, end of headers
		print "<html>"
		print "<head>"
		print "<title>User page!</title>"
		print "</head>"
		print "<p>"
		print "Hi " + user[0]
		print '<form enctype="multipart/form-data" id="video" name="video" method="post" action="/cgi-bin/submission.cgi">'
		print "<label for='file'>Filename:</label>"
		print "<input type='file' name='file' id='file'/>"
		print "<br />"
		print "<input type='submit' name='submit' value='Submit' />"
		print "</form>"
		print '<form id="logout" name="logout" method="post" action="/cgi-bin/logout.cgi">'
		print "<input type='submit' name='submit' value='Logout' />"
		print "<input type='hidden' name = 'username' value =(username) />"
		print "</form>"
		print "</p>"
		print "</html>"
	cur.close()
	conn.close()
except:
	msg = ""
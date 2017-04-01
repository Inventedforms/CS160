#!/usr/bin/python
from furl import furl
from uuid import getnode as get_mac
#import psycopg2
mac = get_mac()
msg = ""
#try:
#	conn = psycopg2.connect("dbname='cs160' user='cs160' host='localhost' password='student'")
#	c = conn.cursor()
#except:
#	msg = "error"
print "Content-Type: text/html\r\n\r\n"    # HTML is following   
print                        # blank line, end of headers
print "<html>"
print "<head>"
print "<title>User page!</title>"
print "</head>"
videos = ["video1","video2","video3","video4"]
print "<p>"
print '<form enctype="multipart/form-data" id="video" name="video" method="post" action="/cgi-bin/submission.cgi">'
print "<label for='file'>Filename:</label>"
print "<input type='file' name='file' id='file'/>"
print "<br />"
print msg
print "<input type='submit' name='submit' value='Submit' />"
print "</form>"
print '<form id="logout" name="logout" method="post" action="/cgi-bin/logout.cgi">'
print "<input type='submit' name='submit' value='Logout' />"
print "</form>"
#print os.environ["REMOTE_ADDR"];
print "</p>"
print "</html>"

#!/usr/bin/python
from furl import furl
from uuid import getnode as get_mac
mac = get_mac()
print "Content-Type: text/html\r\n\r\n"    # HTML is following   
print                        # blank line, end of headers
print "<html>"
print "<head>"
print "<title>User page!</title>"
print "</head>"
videos = ["video1","video2","video3","video4"]
print "<p>"
print "<form id='login' method='post' name='login' action='/cgi-bin/submission.cgi'>"
print "<label for='file'>Filename:</label>"
print "<input type='file' name='file' id='file' />"
print "<br />"
print mac
print "<input type='submit' name='submit' value='Submit' />"
print "</form>"

#print os.environ["REMOTE_ADDR"];
print "</p>"
print "</html>"

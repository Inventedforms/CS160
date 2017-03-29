#!/usr/bin/python

#import cgi, cgitb 
#from furl import furl
from uuid import getnode as get_mac

#form = cgi.FieldStorage()

#cgitb.enable()


mac = get_mac()
if mac == 5:
  #140737678160619:
  print "Location:userpage.cgi\r\n"
else:
  print "Content-Type: text/html\r\n\r\n"    # HTML is following   
  print                        # blank line, end of headers
  print "<html>"
  print "<head>"
  print "<title>User Login</title>"
  print "</head>"
  print "<form id='login' method='post' name='login' action='/cgi-bin/loginscript.cgi'>"
  print "<p>Returning users:</p>"
  print "<p>Username:<br>"
  print "<input id='username' type='text' name='username'>"
  print "</p>"
  print "<p>Password:<br>"
  print "<input id='password' type='password' name='password'>"
  print "</p>"
  print "<p>"
  print "<input id='login' type='submit' value='Login' name='Login'>"
  print "</p>"
  print "</form>"
  print "<button onclick='register()'>Register</button>"
  print "<script>"
  print "function register() {window.location.href ='/userreg.html'}"
  print "</script>"
  print "</html>"

 
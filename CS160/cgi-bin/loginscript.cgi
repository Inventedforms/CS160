#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, os
from furl import furl
from uuid import getnode as get_mac
#from hashlib import blake2

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# For debugging
cgitb.enable()
#conn = psycopg2.connect()
#cur = conn.cursor()
#h = blake2b(digest_size=16)
#Get data from fields
#url = furl(os.environ["REQUEST_URI"])
#print url.add({"user": "2"}).url
#check(username, password)
mac = get_mac()
if  mac == 140737678160619:
	print "Location:userpage.cgi\r\n"
else:
	print "Content-Type: text/html\r\n\r\n"    # HTML is following   
	print                        # blank line, end of headers
	print "<html>"
	print "<head>"
	print "<title>Welcome</title>"
	print "</head>"
	print "<p>"
	print "SOMETHING"
	if "username" not in form or "password" not in form:
		print "Problem detected"
	else:	
		username = form.getvalue('username')
		password = form.getvalue('password')
		print "Hello " + form.getvalue('username')
		print "Your password is: " + form.getvalue('password')

	print "</p>"
	print "</html>"

    #return urlunsplit((scheme, netloc, path, new_query_string, fragment))
#def hash(password, sal){
#	h = blake2b(digest_size=16, salt=sal)
#	h.update(password)
#	return h.hexdigest()
#}

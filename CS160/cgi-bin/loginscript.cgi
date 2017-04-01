#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, os, psycopg2, bcrypt
from furl import furl
from uuid import getnode as get_mac

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# For debugging
cgitb.enable()
mac = get_mac()
if "username" not in form or "password" not in form:
	print "Content-Type: text/html\r\n\r\n"    # HTML is following   
	print                        # blank line, end of headers
	print "<html>"
	print "Incomplete information entered."
	print "</html>"
else:	
	username = form.getvalue('username')
	password = form.getvalue('password')
	print "Content-Type: text/html\r\n\r\n"    # HTML is following   
	print                        # blank line, end of headers
	print "<html>"
	try:
		conn = psycopg2.connect("dbname='cs160' user='cs160' host='localhost' password='student'")
		c = conn.cursor()
		query = "SELECT * FROM user_profile WHERE username=(%s)"
		c.execute(query, [str(username)])
		user = c.fetchone()
		if user is None:
			print "No such user"
		else:
			hashed = user[1]
			if(bcrypt.checkpw(password, hashed)):
				#store a session for the user, redirect them to user page
				print "Location:userpage.cgi\r\n"
			else:
				print "Authentication failure"
		conn.commit()
		c.close()
		conn.close()
	except:
		print "cannot connect"
	print "</html>"
	#	print "cannot connect"
	#try:
		#conn = psycopg2.connect("dbname='alan' user='alan' host='localhost' password='student'")
		#if(bcrypt.checkpw(password, hashed)):
	#		print "Location:userpage.cgi\r\n"
	#	else:
	#except:
#return urlunsplit((scheme, netloc, path, new_query_string, fragment))


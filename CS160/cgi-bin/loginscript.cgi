#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, os, psycopg2, bcrypt, datetime
from uuid import getnode as get_mac

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# For debugging
cgitb.enable()
msg = ""
if "username" not in form or "password" not in form:
	msg = "Incomplete information entered."
else:	
	username = form.getvalue('username')
	password = form.getvalue('password')
	try:
		conn = psycopg2.connect("""
			dbname='cs160' user='cs160' host='localhost' password='student'
			""")
		c = conn.cursor()
		query = "SELECT * FROM user_profile WHERE username=(%s)"
		c.execute(query, [str(username)])
		user = c.fetchone()
		if user is None:
			msg = "No such user"
		else:
			hashed = user[1]
			if(bcrypt.checkpw(password, hashed)):
				#store a session for the user, redirect them to user page
				ip = os.environ["REMOTE_ADDR"]
				mac = get_mac()
				session = "INSERT INTO user_login (Username, Login_date, Login_ip, MAC_address) VALUES (%s %s %s %s)"
				c.execute(session, [username, datetime.datetime, ip, str(mac)])
				print "Location:userpage.cgi\r\n"
			else:
				msg = "Authentication failure"
		conn.commit()
		c.close()
		conn.close()
	except Exception, e:
		msg  = str(e)
print "Content-Type: text/html\r\n\r\n"    # HTML is following   
print                        # blank line, end of headers
print "<html>"
print msg
print "</html>"

#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb, os, psycopg2, bcrypt, datetime, ipaddress
from uuid import getnode as get_mac

# Create instance of FieldStorage
form = cgi.FieldStorage()
# For debugging
cgitb.enable()
msg = "yay"
if "username" not in form or "password" not in form:
	msg = "Incomplete information entered."
else:
	username = form.getvalue('username')
	password = form.getvalue('password')
	try:
		conn = psycopg2.connect("""
			dbname='cs160' user='postgres' host='localhost' password = 'student'
			""")
		c = conn.cursor()
		query = "SELECT * FROM user_profile WHERE username=(%s)"
		c.execute(query, [username])
		user = c.fetchone()
		if user is None:
			msg = "No such user"
		else:
			hashed = str(user[1])
			if(bcrypt.checkpw(password, hashed)):
				#store a session for the user, redirect them to user page
				ip = os.environ["REMOTE_ADDR"]
				mac = get_mac()
				clear = """
				DELETE FROM user_login WHERE Username=(%s)
				"""
				session = """
				INSERT INTO user_login (Username,Login_date, Login_ip, MAC_address) VALUES (%s,now(), %s, %s)
				"""
				c.execute(clear, [username])
				c.execute(session, [username,ip, str(mac)])
				#c.execute("INSERT INTO user_login (Login_date) VALUES (now()) WHERE Username=%s ", [username])
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

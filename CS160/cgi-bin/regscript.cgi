#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, psycopg2, bcrypt, os
from uuid import getnode as get_mac
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# For debugging
cgitb.enable()
crappy_passwords = {'password', '12345', '123456' ,'qwerty' ,'12345678', 'letmein'}
#Get data from fields
message = ""

def printerror(msg):
	print "Content-Type: text/html\r\n\r\n"    # HTML is following   
	print                        # blank line, end of headers
	print "<html>"
	print "<head>"
	print "<title>Welcome</title>"
	print "</head>"
	print "<p>"
	print msg
	print "</p>"
	print "</html>"	

if "username" not in form or "p1" not in form or "p2" not in form:
	printerror("Please pick a username and password.")
else:	
	try:
		conn = psycopg2.connect("""
			dbname='cs160' user='postgres' host='localhost' password = 'student'
			""")
		cur = conn.cursor()
		username = form.getvalue('username')
		pw = form.getvalue('p1')
		pw2 = form.getvalue('p2')
		usernametaken = "SELECT * FROM user_profile WHERE username=(%s)"
		cur.execute(usernametaken, [str(username)])
		if cur.fetchone() is not None:
			printerror("Username already taken.")
		if pw <> pw2:
			printerror("Passwords don't match.")
		elif pw in crappy_passwords:
			printerror("Pick a better password.")
		else:
			fname = form.getvalue('fname')
			lname = form.getvalue('lname')
			if fname is None:
				fname = ""
			if lname is None:
				lname = ""
			message =  "Hello " + fname + " " + lname
			hashed = bcrypt.hashpw(pw, bcrypt.gensalt())
			check = """
			INSERT INTO user_profile (Username, Password, F_name, L_name)
			VALUES (%s, %s, %s, %s)
			"""
			cur.execute(check, [str(username), hashed, str(fname), str(lname)])
			#Create a table for this user's videossub
			ip = os.environ["REMOTE_ADDR"]
			mac = get_mac()
			session = "INSERT INTO user_login (Username, Login_date, Login_ip, MAC_address) VALUES (%s, now(), %s, %s)"
			c.execute(session, [username, str(ip), str(mac)])
			#print str(type(datetime.datetime.now()))
			print "Location:userpage.cgi\r\n"
		conn.commit()
		cur.close()
		conn.close()
	except Exception, e:
		printerror(str(e))

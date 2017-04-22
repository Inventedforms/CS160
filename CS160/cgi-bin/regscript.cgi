#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, psycopg2, bcrypt, os
import globals
from uuid import getnode as get_mac
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# For debugging
cgitb.enable()
crappy_passwords = {'password', '12345', '123456' ,'qwerty' ,'12345678', 'letmein', '54321'}
#Get data from fields
message = ""

if "username" not in form or "p1" not in form:
	printerror("Please pick a username and password.")
elif ("p1" in form) != ("p2" in form):
	printerror("Make sure you enter your password twice!")
else:	
	try:
		conn = psycopg2.connect(globals.credentials)
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
			#wipe current session. I should make this into a callable method.
			string = "SELECT * FROM user_login WHERE MAC_Address=(%s) AND Login_ip=(%s)"
			info = [str(mac), ip]
			cur.execute(string, info)
			if cur.fetchone() is not None:
				cur.execute("DELETE FROM user_login WHERE MAC_Address=(%s) AND Login_ip=(%s)",info)
			
			session = "INSERT INTO user_login (Username, Login_date, Login_ip, MAC_address) VALUES (%s, now(), %s, %s)"
			cur.execute(session, [username, ip, str(mac)])
			#print str(type(datetime.datetime.now()))
			print "Location:userpage.cgi\r\n"
		conn.commit()
		cur.close()
		conn.close()
	except Exception as e:
		globals.printerror(str(e))

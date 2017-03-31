#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, psycopg2, bcrypt
#from hashlib import blake2

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# For debugging
cgitb.enable()
crappy_passwords = {'password', '12345', '123456' ,'qwerty' ,'12345678'}
#Get data from fields

print "Content-Type: text/html\r\n\r\n"    # HTML is following   
print                        # blank line, end of headers
print "<html>"
print "<head>"
print "<title>Welcome</title>"
print "</head>"
print "<p>"
if "username" not in form or "p1" not in form or "p2" not in form:
	print "Please pick a username and password."
else:	
	try:
		conn = psycopg2.connect("dbname='alan' user='alan' host='localhost' password='student'")
		cur = conn.cursor()
		username = form.getvalue('username')
		pw = form.getvalue('p1')
		pw2 = form.getvalue('p2')
		usernametaken = "SELECT * FROM user_profile WHERE username=(%s)"
		cur.execute(usernametaken, [str(username)])
		if cur.fetchone() is not None:
			print "Username already taken"
		if pw != pw2:
			print "Passwords don't match."
		elif pw in crappy_passwords:
			print ("Pick a better password.")
		else:
			fname = form.getvalue('fname')
			lname = form.getvalue('lname')
			if fname is None:
				fname = ""
			if lname is None:
				lname = ""
			print "Hello " + fname + " " + lname
			hashed = bcrypt.hashpw(pw, bcrypt.gensalt())
			check = """
			INSERT INTO user_profile (usrname, password, f_name, l_name)
			VALUES (%s, %s, %s, %s)
			"""
			cur.execute(check, [str(username), hashed, str(fname), str(lname)])
			print "User " + username + " successfully registered."
		conn.commit()
		cur.close()
		conn.close()
	except:
		print "error"
print "</p>"
print "</html>"

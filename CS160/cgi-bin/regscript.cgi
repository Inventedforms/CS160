#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, psycopg2
#from hashlib import blake2

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# For debugging
cgitb.enable()
#conn = psycopg2.connect()
#cur = conn.cursor()
#h = blake2b(digest_size=16)
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
	print "Incomplete form"
else:
	username = form.getvalue('username')
	pw = form.getvalue('p1')
	pw2= form.getvalue('p2')
	if pw != pw2:
		print "Passwords don't match."
	elif pw in crappy_passwords:
		print ("Pick a better password.")
	#check(username, password)
	else:
		try:
			conn = psycopg2.connect("dbname='alan' user='alan' host='localhost' password='student'")
			print "Hello " + username
			print "Your password is: " + pw
			c = conn.cursor()
			print "We made it!"
		except:
			print "cannot connect"
print "</p>"
print "</html>"

#def hash(password, sal){
#	h = blake2b(digest_size=16, salt=sal)
#	h.update(password)
#	return h.hexdigest()
#}

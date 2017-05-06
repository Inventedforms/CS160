#!/usr/bin/python

#Global variable for generic credentials used to access postgres db
#I recommend renaming this to something less obvious.
credentials = "dbname='cs160' user='postgres' host='localhost' password = 'student'"

#Generic error message.
def printerror(msg):
	print ("Content-Type: text/html\r\n\r\n")    # HTML is following   
	print                        # blank line, end of headers
	print ("""<html>
			<head>
				<title>Error</title>
			</head>
	<p>
	%s
	</p>
	</html>
	""" % msg)
#Create a redirect button. Toggle standalone if the button needs to be its own html page.
def redirect(standalone):
	if not standalone:
		print ("Content-Type: text/html\r\n\r\n")    # HTML is following   
		print  ()                      # blank line, end of headers
		print ("<html>")
	print ("""<form id=return name=return method=post action=/cgi-bin/redirect.cgi>
	<input type='submit' name='submit' value='Click to return to your home page.' />""")
	if not standalone:
		print ("</html>")
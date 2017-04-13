#!/usr/bin/python

#Global variable for generic credentials used to access postgres db
#I recommend renaming this to something less obvious.
credentials = "dbname='cs160' user='postgres' host='localhost' password = 'student'"

def printerror(msg):
	print "Content-Type: text/html\r\n\r\n"    # HTML is following   
	print                        # blank line, end of headers
	print "<html>"
	print "<head>"
	print "<title>Error</title>"
	print "</head>"
	print "<p>Something went wrong.</p>"
	print "<p>"
	print msg
	print "</p>"
	print "</html>"	
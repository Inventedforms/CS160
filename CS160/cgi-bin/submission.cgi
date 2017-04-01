#!/usr/bin/python
import cgi, cgitb, os
fs = cgi.FieldStorage()
message = "wololo"
cgitb.enable()
## Test if the file was uploaded
print "Content-Type: text/html\r\n\r\n"    # HTML is following   
print                        # blank line, end of headers
print "<html>"
print "<head>"
print "<title>Submission!</title>"
print "</head>"
print "<p>Submitted</p>"
#if not "userfile" in fs:
#	message = 'No file in form detected'
#else:
fileitem = fs['file']
print fileitem.filename
if fileitem.file:
   #fn = os.path.basename(fileitem.filename)
   #open('/tmp/' + fn, 'wb').write(fileitem.file.read())
	message = 'The file ' + fileitem.filename +' was uploaded successfully'
else:
	message = 'No file was uploaded'
print message
print "</html>"
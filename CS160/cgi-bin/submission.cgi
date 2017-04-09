#!/usr/bin/python
import cgi, cgitb, os, sys
message = "wololo"
cgitb.enable()

def save_uploaded_file (form_field, upload_dir):
    """This saves a file uploaded by an HTML form.
       The form_field is the name of the file input field from the form.
       For example, the following form_field would be "file_1":
           <input name="file_1" type="file">
       The upload_dir is the directory where the file will be written.
       If no file was uploaded or if the field does not exist then
       this does nothing.
    """
    form = cgi.FieldStorage()
    if not form.has_key(form_field):
    	return "no such file found"
    fileitem = form[form_field]
    if not fileitem.file: 
    	return "invalid file"
    fout = file (os.path.join(upload_dir, fileitem.filename), 'wb')
    while 1:
        chunk = fileitem.file.read(100000)
        if not chunk: break
        fout.write (chunk)
    fout.close()
    return "file uploaded"
## Test if the file was uploaded
print "Content-Type: text/html\r\n\r\n"    # HTML is following   
print                        # blank line, end of headers
print "<html>"
print "<head>"
print "<title>Submission!</title>"
print "</head>"
print "<p>Submitted</p>"
try:
	print save_uploaded_file("file", "/home/alan/cs160")
except Exception, e:
	print str(e)
print "</html>"
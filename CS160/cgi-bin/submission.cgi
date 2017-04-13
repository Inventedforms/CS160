#!/usr/bin/python3
import cgi, cgitb, os, sys, subprocess, shlex, re
from subprocess import call
from subprocess import getstatusoutput
cgitb.enable()
def remove_file(filename):
	cmd = "rm " + filename
	return getstatusoutput([cmd])
def ffprobe_file(filename):
	p = "\n = EMPTY RETURN"
	cmnd = 'ffprobe -v error -show_format -show_entries stream=width,height,bit_rate,duration -of default=noprint_wrappers=1 '
	#p = getoutput([cmnd+filename])
	p = getstatusoutput([cmnd+filename])
	return parse(p)

def parse(str):
	acc = ""
	if str[0] == 1:
		return str[1]
	else:
		str = (str[1].split('\n'))
		for string in str:
			string = (string.split('=')[1])
			acc = acc + " " + string
	return acc
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
	if not form_field in form:
		return "no such file found"
	fileitem = form[form_field]
	if not fileitem.file: 
		return "invalid file"
	fn = os.path.basename(fileitem.filename)
	open(upload_dir + fn, 'wb').write(fileitem.file.read())
	return upload_dir + fn
## Test if the file was uploaded
print ("Content-Type: text/html\r\n\r\n")    # HTML is following   
print ()                       # blank line, end of headers
print ("<html>")
print ("<head>")
print ("<title>Submission!</title>")
print ("</head>")
try:
	#print (sys.path)
	res = save_uploaded_file("file", "/temp/")
	print(res)
	print(ffprobe_file(res))
except Exception as  e:
	print ("shit.")
	print (str(e))
print ("</html>")
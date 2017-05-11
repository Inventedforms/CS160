#!/usr/bin/python3
import cgi, cgitb, os, re
import globals
import psycopg2
import ffmpeg
import sys
from subprocess import getstatusoutput
from uuid import getnode as get_mac
cgitb.enable()


def getusername():
	#because I can't seem to easily pass variables. Also, this provides for an extra layer of security.
	conn = psycopg2.connect(globals.credentials)
	cur = conn.cursor()
	checksession = """
	SELECT * FROM user_login WHERE MAC_Address=(%s)
	"""
	mac = str(get_mac())
	cur.execute(checksession, [mac])
	info = cur.fetchone()
	if info:
		result = info[1]
	else:
		result = None
	conn.close()
	return result

#Nuke a video and the folder it created.
def remove_file(filename, filepath):
	cmd = "rm " + filename
	getstatusoutput([cmd])
	cmd = "rm -r " + filepath
	getstatusoutput([cmd])


def ffprobe_file(filename):
	p = "\n = EMPTY RETURN"
	cmnd = 'ffprobe -v error -show_format -show_entries stream=width,height,avg_frame_rate,duration -of default=noprint_wrappers=1 '
	#p = getoutput([cmnd+filename])
	p = getstatusoutput([cmnd+filename])
	result =  parse(p)
	if isinstance(result, list) and result[2] != '0/0':
		cmnd = 'ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 '
		p = getstatusoutput([cmnd+filename])
		result = [p[1]] + result
	else:
		result = False
	
	return result


def parse(str):
	acc = []
	if str[0] == 1:
		return str[1]
	else:
		str = (str[1].split('\n'))
		for string in str:
			string = (string.split('=')[1])
			acc.append(string)
	return acc


def verify(file, owner):
	info = ffprobe_file(file)
	#print(info)
	if info:
		conn = psycopg2.connect(globals.credentials)
		cur = conn.cursor()
		#framerate = [top, bottom, width, height]
		framerate = info[3].split('/')
		framerate = framerate + [info[1], info[2]]
		fr = list(map(lambda x: int(x), framerate))
		data = [fr[0]/fr[1], info[0], fr[2], fr[3] , info[7], info[10], owner]
		cur.execute("""
		INSERT INTO video_metadata (framerate, frame_num_total, resolution, video_name, encoding, owner)
		 VALUES (%s, %s,point(%s, %s), %s, %s,%s)
		""", data)
		info = [True] + info
		conn.commit()
		conn.close()
	return info

#Todo: Also, consider what happens with multiple videos of the same name.
#Returns [status, video location, video folder]
def save_uploaded_file (form_field, upload_dir, username):
	"""This saves a file uploaded by an HTML form.
	   The form_field is the name of the file input field from the form.
	   For example, the following form_field would be "file_1":
		   <input name="file_1" type="file">
	   The upload_dir is the directory where the file will be written.
	   If no file was uploaded or if the field does not exist then
	   this does nothing.
	"""
	form = cgi.FieldStorage()
	#print(form)
	if not form_field in form:
		return [False,"No file detected."]
	fileitem = form[form_field]
	if not fileitem.file: 
		return [False,"Invalid file"]
	filename = os.path.basename(fileitem.filename)
	filename = re.sub('[<>/]', '', filename)
	if filename == "":
		return [False, "No file detected."]
	if not os.path.isdir(upload_dir + username):
		os.mkdir(upload_dir + username)
	#Handle periods in video names
	fn = filename.split('.')
	if(len(fn) > 2):
		for x in fn[1:-1]:
			fn[0] = fn[0] + '.' + x
	path = upload_dir + username + '/' + fn[0]
	#Todo: Multiple files with the same name and user.
	#subscript = 1
	#while os.path.isdir(path):
#		path = path + '(' + subscript +  ')'
	if not os.path.isdir(path):
		os.mkdir(path)

	open(upload_dir + username + '/' + filename, 'wb').write(fileitem.file.read())
	return [True, upload_dir + username + '/' + filename, path]


def header():
	print ("Content-Type: text/html\r\n\r\n")    # HTML is following   
	print ()                       # blank line, end of headers
	print ("<html>")
	print ("<head>")
	print ("<title>Submission!</title>")
	print ("</head>")

#main
try:
	#print (sys.path)
	user = getusername()
	if not user:
		print("Location:userlogin.cgi")

	#form = cgi.FieldStorage()
	res = save_uploaded_file("file", "/var/www/html/temp/", user)
	#print(res)
	if not res[0]:
		globals.printerror(res[1], "Error")
		sys.exit()
	#print(res)
	verif = verify(res[1], user)
	#print(verif)
	if res[0] and verif:
		header()
		ffmpeg.split(res[1] ,res[2])
		#Call other shit
		p = ffmpeg.unsplit(res[2], res[2])
		#print(p)
		print("File successfully uploaded.", "Success")
		globals.redirect(True)
	else:
		globals.printerror("File is invalid, for some reason.", "Error")
		#globals.redirect(True)
		remove_file(res[1], res[2])
except Exception as  e:
	globals.printerror(str(e), "Error")
print ("</html>")

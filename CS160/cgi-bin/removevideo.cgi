#!/usr/bin/python3.5
import os, cgi, cgitb, psycopg2, globals
from subprocess import getstatusoutput
#Nuke a video and the folder it created.
#We'll have to add to this later to more thoroughly remove stuff.
def remove_file(filename, filepath):
	cmd = "rm "  + filename
	getstatusoutput([cmd])
	cmd = "rm " + filepath + "_NEW.mp4"
	getstatusoutput([cmd])
	cmd = "rm -r " + filepath
	getstatusoutput([cmd])

form = cgi.FieldStorage()
user = form.getvalue("username")
upload_dir = "/var/www/html/temp/"
vid = upload_dir + form.getvalue("videoname")
fp = upload_dir + os.path.split(form.getvalue("videoname"))[0]

remove_file(vid, fp)

conn = psycopg2.connect(globals.credentials)
cur = conn.cursor()
cur.execute("DELETE FROM video_metadata WHERE Owner = (%s) AND video_name = (%s)", [user, vid])
conn.commit()
conn.close()
print("Location:userpage.cgi\r\n")
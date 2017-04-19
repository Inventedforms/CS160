#!/usr/bin/python
import os, cgi, cgitb, psycopg2
def remove_video(video_name):

	cmd = "rm " + filename
	return getstatusoutput([cmd])
form = cgi.fieldStorage()
remove_video()
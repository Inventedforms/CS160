#!/usr/bin/python
import psycopg2, os, globals
from uuid import getnode as get_mac
msg = ""
try:
	ip = os.environ["REMOTE_ADDR"]
	mac = str(get_mac())
	conn = psycopg2.connect(globals.credentials)
	c = conn.cursor()
	checksession = """
	SELECT * FROM user_login WHERE MAC_Address=(%s) AND Login_ip=(%s)
	"""
	c.execute(checksession, [mac, ip])
	session = c.fetchone()
	if session:
		print ("Location:userpage.cgi\r\n")
	else:
		print ("Location:userlogin.cgi\r\n")
	c.close()
	conn.close()
except Exception, e:
	globals.printerror(str(e), "Error")

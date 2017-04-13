#!/usr/bin/python
import psycopg2, os
from uuid import getnode as get_mac
import globals
try:
	mac = get_mac()
	ip = os.environ["REMOTE_ADDR"]
	conn = psycopg2.connect(globals.credentials)
	c = conn.cursor()
	string = "SELECT * FROM user_login WHERE MAC_Address=(%s) AND Login_ip=(%s)"
	info = [str(mac), ip]
	c.execute(string, info)
	if c.fetchone() is not None:
		c.execute("DELETE FROM user_login WHERE MAC_Address=(%s) AND Login_ip=(%s)",info)
	conn.commit()
	c.close()
	conn.close()
	print("Location:http://localhost/home.html\r\n")
except Exception, e:
	globals.printerror(str(e))

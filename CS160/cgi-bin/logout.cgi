#!/usr/bin/python
import psycopg2, os
from uuid import getnode as get_mac
try:
	mac = get_mac()
	conn = psycopg2.connect("dbname='cs160' user='cs160' host='localhost' password='student'")
	c = conn.cursor()

	str = "SELECT * FROM user_login WHERE MAC_Address=(%s) AND Login_ip=9(%s)"
	info = [str(mac), str(os.environ["REMOTE_ADDR"])]
	c.execute(str, info)
	if c.fetchone() is not None:
		c.execute("DROP * FROM user_login WHERE MAC_Address=(%s) AND Login_ip=9(%s)",info)
except Exception, e:
#!/usr/bin/python
from furl import furl
url = furl(os.environ["REQUEST_URI"])
url.join('../userreg.html')
print "Location:" + url + "\r\n"
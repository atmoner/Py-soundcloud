import pycurl
import cStringIO
import urllib2
import re
import time
import urlparse 
from urlparse import urlparse
import sys

def getMp3( str ):
   ret = re.findall(r'("streamUrl":[^\s]+)',  urllib2.urlopen(str).read())[0][48:60]
   return "".join(['http://media.soundcloud.com/stream/', ret, '?stream_token=own3d'])

def soundcloud_dl(url, name, mode):
   # Curl part
   print "Connecting to %s" % url
   try:
      buf = cStringIO.StringIO()
      c = pycurl.Curl()
      c.setopt(c.URL, url)
      c.setopt(c.FOLLOWLOCATION, 1)
      c.setopt(c.WRITEFUNCTION, buf.write)
      c.perform()
   except:
      print "Error with : %s" % name
   else:
      print "Downloading %s" % name
      # Write part
      with open(name, mode) as file : file.write(buf.getvalue())
      buf.close()
 
print """---------------------
Py-soundcloud
By @atmon3r (contact.atmoner@gmail.com)
(f0rk by fr0g)
---------------------"""

# Basic script
if (len(sys.argv) < 2):
   print """Usage : ./py-soundcloud.py [URL_1] [URL_2] ..."""
   exit(1);

for i in range(1, len(sys.argv)):
   
   try:
      info= urlparse(sys.argv[i]).path.split("/")
      info[2]
   except:
      print "Error : Bad url"
      continue
   else:
      print """Artiste  : %s\nTrack   : %s""" % (info[1] , info[2])

   try:
      url = getMp3(sys.argv[i]);
      soundcloud_dl(url, info[2], "w+");

   except: print "Error : %s" % info[2]

   else:      print '%s is now saved!\n' % info[2] 



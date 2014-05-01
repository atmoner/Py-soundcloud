#!/usr/bin/python

import pycurl
import cStringIO
import urllib2
import re
import time
import urlparse 
from urlparse import urlparse


def getMp3( str ):
 
   resp = urllib2.urlopen(str)
   page = resp.read()
   resp.close()
   ret = re.findall(r'("streamUrl":[^\s]+)', page)
   ret = ret[0][48:60]
   lst = ['http://media.soundcloud.com/stream/', ret, '?stream_token=own3d']
   finalurl = "".join(lst)
 
   return finalurl;

def soundcloud_dl(url, name, mode):
   # Curl part
   buf = cStringIO.StringIO()
   c = pycurl.Curl()
   c.setopt(c.URL, url)
   c.setopt(c.FOLLOWLOCATION, 1)
   c.setopt(c.WRITEFUNCTION, buf.write)
   c.perform()
 

   # Write part
   file = open(name, mode)
   file.write(buf.getvalue())
   file.close()

   buf.close()
   return;
 
print('---------------------')
print('  Py-soundcloud  ')
print('  By @atmon3r (contact.atmoner@gmail.com) ')
print('---------------------')
  
# Basic script
soudcloudUrl = raw_input('Soundcloud url file: ')

if soudcloudUrl:

    print '....'
    time.sleep(1)
    print('....')
    time.sleep(1)
    
    parsed = urlparse(soudcloudUrl)
    info = parsed.path.split("/")
    print 'Artiste  :',info[1]
    print 'Track    :',info[2]
    time.sleep(1)
    
    print('Connection established to soundcloud')
    time.sleep(1)
    print('Download in progress')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('....')
    time.sleep(1)
    url = getMp3(soudcloudUrl);
    soundcloud_dl(url, info[2], "w+");
    print 'Your file is download!\n' 
else:
    print 'Add soundcloud url!' 

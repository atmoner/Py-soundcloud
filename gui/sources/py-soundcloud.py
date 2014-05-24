#-*-coding:utf8-*-
from Tkinter import *
import tkMessageBox
import pycurl
import cStringIO
import urllib2
import re
import time
import urlparse 
from urlparse import urlparse
from os.path import expanduser
 

root = Tk()
root.title("Py-soundcloud Gui")
pathImg = expanduser("~") +'/soundcloud-gui/'
 

img = PhotoImage(file=pathImg+'ico.gif')
root.tk.call('wm', 'iconphoto', root._w, img)
root.geometry("400x500")
saisie=StringVar()

p = PhotoImage(file=pathImg+"banner.gif")
l = Label(root, image=p)
l.pack_propagate(0)
l.pack()

photo = PhotoImage(file=pathImg+'download.gif')

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
      
def about():
   tkMessageBox.showinfo("About Py-soundcloud Gui", "Version: 2.0 \nCreated by @atmon3r")

def timeSleep():
    tex2.configure(text= 'Your download is complete')

def fonc(event):  
    affichage() 

def affichage():
    # tex2.configure(text= ent.get())
    parsed = urlparse(ent.get())
    info = parsed.path.split("/")
    print 'Artiste  :',info[1]
    print 'Track    :',info[2]
    tex2.configure(text= 'Track information\nArtist: ' + info[1] + '\nTrack: ' + info[2]) 

    url = getMp3(ent.get());
    soundcloud_dl(url, info[2], "w+");
    
    
    tex2.after(5000, timeSleep)
      

labelframe1 = LabelFrame(root, text="Soundcloud url")
labelframe1.pack(fill="both", expand="yes")

L1 = Label(labelframe1, text="Url")
L1.pack( side = LEFT)
ent = Entry(labelframe1, bd =2,textvariable=saisie,width=40)
ent.bind("<Return>",fonc) # A MODIFIER
ent.pack(side = LEFT)
saisie.set('https://soundcloud.com/atm0ner/shadow')


labelframe2 = LabelFrame(root, text="One click download",height="200")
labelframe2.pack(fill="both", expand="yes")

bou1 = Button(labelframe2, text='Donwload ',command = affichage, pady = '25', image=photo)
bou1.pack(side = TOP)

 
labelframe3 = LabelFrame(root, text="Result")
labelframe3.pack(fill="both", expand="yes")

tex2 = Label(labelframe3, text="", fg='black')
tex2.pack(side = LEFT)

labelframe4 = LabelFrame(root, text="About Py-soundcloud Gui")
labelframe4.pack(fill="both", expand="yes")

About = Button(labelframe4, text = "About this software", command = about)
About.pack()

root.mainloop()

#!/usr/bin/env python

# Import documents into CouchDB

# TODO: Create settings.py

from datetime import datetime

from couchdbkit import Server
from couchdbkit.schema import *

class ImageDoc(Document):
    date = DateTimeProperty(default=datetime.utcnow)

server = Server('http://192.168.1.124:5984')
db = server.get_or_create_db("pdfs")

ImageDoc._db = db


import urllib2
import sys

base_url = 'http://localhost:8000/pdf/'

nstart = int(sys.argv[1])
nend = int(sys.argv[2])

for i in range(nstart, nend):
    i = i + 1
    file = ('%s' + '.pdf') % (i,)
    url = (base_url + file)

    print "Importing url: " + url

    # create the doc
    imageDoc = ImageDoc()
    imageDoc._id = str(i)
    imageDoc.save()

    # read PDF from our document generator
    f = urllib2.urlopen(url)
    data = f.read() #read in because of seek(0) issue
    # save as attachment
    imageDoc.put_attachment(data, file, "application/x-pdf")



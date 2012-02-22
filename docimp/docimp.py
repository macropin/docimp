#!/usr/bin/env python

# Import a range of documents into CouchDB from a remote url / generator

from datetime import datetime

from couchdbkit import Server
from couchdbkit.schema import *

from settings import *

# CouchDB Document object
class ImageDoc(Document):
    date = DateTimeProperty(default=datetime.utcnow)

server = Server(COUCH_SERVER_URL)
db = server.get_or_create_db(COUCH_DATABASE_NAME)

ImageDoc._db = db

# Main function loop
import urllib2
import sys

base_url = DOCMK_URL

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



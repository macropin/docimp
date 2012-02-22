# Settings for docimp

COUCH_SERVER_URL='http://192.168.1.124:5984' # Set Me
COUCH_DATABASE_NAME='pdfs'

DOCMK_URL='http://localhost:8000/pdf/' # Base Url to our 'docmk' pdf generator 


try:
    from local_settings import *
except ImportError:
    pass

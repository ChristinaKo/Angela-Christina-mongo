import random
from pymongo import Connection

conn = Connection()

#db.conn.admin
#db.authenticate('user','password')

db = conn['ACdata']

print db.collection_names() #currently empty


###FOR REGISTERING:
#use input from the HTML for name and password
#format in mongo style (d = {'username':'inputhere','password':'moreinput'} )
#and place formatted information into a string
#then insert into our collection (people?)/database

##REGISTERING INFORMATION NEEDED:
#-->username
#-->password/confirm password
#-->birthday (via dropbox)
#-->Real Name
#-->color of page?


###FOR CHECKING (USERNAME AND PASSWORD):
#check if username is in database/collection
#if yes, then check if corresponding pwd matches
#if no, then return error message, angry face, redirect to login page

#use boolean to pass through jinja/html to see whether or not to display error message (when username is not available/DNE)


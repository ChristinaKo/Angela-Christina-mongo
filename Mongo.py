import random
from pymongo import MongoClient
#after looking at the API, it seems like using
#MongoClient is better than using Connection,
#which is depreciated

client = MongoClient()

db = client['data']#database called data
users = db['names']#collection of users
#print db.collection_names() #currently empty
user1 = { 'name': "lame", 'id':'12323'}
user2 = { 'name': "lame", 'id':'56567'}
users.insert(user1)
users.insert(user2)

for post in users.find({'name':'lame'}):
    print post
    
db.drop_collection('names') #drops collection each time --> this should not be necessary in the future but...



###FOR REGISTERING:
#use input from the HTML for name and password
#format in mongo style (d = {'username':'inputhere','password':'moreinput'} )
#and place formatted information into a string
#then insert into our collection (people?)/database

##REGISTERING INFORMATION NEEDED:
#-->username
#-->password/confirm password
#-->birthday (via dropdown)
#-->Real Name
#-->color of page?

###FOR CHECKING (USERNAME AND PASSWORD):
#check if username is in database/collection
#if yes, then check if corresponding pwd matches
#if no, then return error message, angry face, redirect to login page

##USER EXCLUSIVE PAGES
#user information page
#

##NON-USER AVAILABLE PAGES
#about page
#login page
#register page

#use boolean to pass through jinja/html to see whether or not to display error message (when username is not available/DNE)


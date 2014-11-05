import random
from pymongo import MongoClient
#after looking at the API, it seems like using
#MongoClient is better than using Connection,
#which is depreciated
client = MongoClient()


db = client['data']#database called data
users = db['names']#collection of users
#users should have uname, password, firstname, lastname

#checks if the user is already in our users collection
def check_user_in_db(usr):
    return users.find_one({'uname':usr})

#creating a new user
def new_user(dictinput):#MUST CHECK IF USER IN DB
    users.insert(dictinput)
    for user in users.find():
        print user

def drop_users():
    db.drop_collection('names') #drops collection each time --> this should not be necessary in the future but...


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


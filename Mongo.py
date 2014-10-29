import random
from pymongo import Connection

conn = Connection()

db = conn['AC']
# print db.collection_names()
names = []
passwords=[]

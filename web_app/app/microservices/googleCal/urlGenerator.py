import datetime
import os.path
import json

# generate google calendar link for user
def createURL():
    name = "Nishant Srivastava"
    school = "rpi.edu"
    api.create(name,school)
    return(link)

# when user deletes account, delete calendar
def deleteURL(link):
    api.delete(link)

# :~)

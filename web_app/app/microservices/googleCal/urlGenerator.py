from .Google import Create_Service
import datetime
import os
import json

CLIENT_SECRET_FILE = os.path.abspath("app/microservices/googleCal/credentials.json")
# CLIENT_SECRET_FILE = "./microservices/googleCal/credentials.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

# generate google calendar link for user
def createURL(name, email):
    name = name.strip()
    school = email.strip().split("@")[1].split(".")[0]

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    # Nishant Srivastava - rpi
    calendarName = name+" - "+school

    calendar = { 
        'summary': calendarName,
        'timeZone': 'America/New_York'
    }

    newCalendar = service.calendars().insert(body=calendar).execute()
    return(newCalendar['id'])

# when user deletes account, delete calendar
def deleteURL(id):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    service.calendars().delete(calendarID=id).execute()
    pass

# :~)

if __name__ == "__main__":
    # createURL("Nishant Srivastava", "srivan@rpi.edu")
    pass

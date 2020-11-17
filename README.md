# CourseCal
Automate the process of transferring your semester's calendar from your university's end to your personal calendar (google calendar/outlook calendar/etc)

# Virtual Environment
- python3 -m venv venv
- source venv/bin/activate
To deactivate, simply enter `deactivate`

# Dependencies
- python3 -m pip install -r requirements.txt
then lock the requirements
- pip freeze > requirements.txt

# Starting the server & stuff
- cd web_app
- python3 manage.py runserver

Since we're working with a MongoDB, we don't have to worry about migrations :smiley:

# Next?
- Work on the project
- Setup Docker shit for professionalism (lol) & for ease of deployment
- Work on RPI's automation
- Integrate a ReCaptcha solver (I bet some universities have implemented Google ReCaptcha or something similar)
-- maybe make our own ReCaptcha solver (that'd be an insane side project)
# CourseCal
Automate the process of transferring your semester's calendar from your university's end to your personal calendar (google calendar/outlook calendar/etc)

# Virtual Environment
- `python3 -m venv venv`
- `source venv/bin/activate`
To deactivate, simply enter `deactivate`

# Dependencies
- `python3 -m pip install -r requirements.txt` then lock the requirements *(you may need to run `wget https://bootstrap.pypa.io/get-pip.py` then `sudo python3.6 get-pip.py`)*
- `pip freeze > requirements.txt`

# Starting the server & stuff
- `cd web_app`
- `python3 manage.py runserver`

Since we're working with a MongoDB, we don't have to worry about migrations :smiley:

# Project Screenshots
Some of these screenshots weren't implemented in code because I either was lazy or didn't have the time for it (school gah)
- ![image](https://user-images.githubusercontent.com/20250366/116817437-f1291900-ab83-11eb-974b-b4d79561d8d2.png)
- ![image](https://user-images.githubusercontent.com/20250366/116817445-fbe3ae00-ab83-11eb-84f7-c5229cd4a94a.png)
- ![image](https://user-images.githubusercontent.com/20250366/116817403-cb9c0f80-ab83-11eb-9455-95ebb85ca030.png)
- ![image](https://user-images.githubusercontent.com/20250366/116817411-d5257780-ab83-11eb-8038-716fe62d9c19.png)
- ![image](https://user-images.githubusercontent.com/20250366/116817415-da82c200-ab83-11eb-958e-5bad2654b936.png)
- ![image](https://user-images.githubusercontent.com/20250366/116817422-e1a9d000-ab83-11eb-8a31-5bef208ae0cb.png)


# Next?
- Work on the project
- Setup Docker for professionalism (lol) & for ease of deployment
- Work on RPI's automation
- Integrate a ReCaptcha solver (I bet some universities have implemented Google ReCaptcha or something similar)
-- maybe make our own ReCaptcha solver (that'd be an insane side project)

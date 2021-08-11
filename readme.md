# Fullstackk Backend Assignment

#### Installation
- Clone the GitHub repo
- First open the terminal in the root of the github repo -> "fullstackk_assignment"
- Assuming System has python3 installed, create the virtual environment in the root folder itself using "python3 -m venv my-project-env" or "virtualenv my-project-env"
- Activate the environment using "source my-project-env/bin/activate"
- Install the requirement/dependncies using "pip install -r requirements.txt"

#### Run the project
- python manage.py makemigrations
- python manage.py migrate
- python manage.py populate_masters
- python manage.py createsuperuser
    - (username): xyz
    - (email): PRESS ENTER
    - (password): root
    - (password again): root
    - Bypass password validation and create user anyway? [y/N]: y
    - The above steps will create 8 TABLES. The above tables visualization can be done by accessing the admin panel with superuser's credentials whose username is 'xyz'
- Runserver using "python manage.py runserver 8869", assuming 8869 to be the port address

- Goto the development server address i.e. 'http://127.0.0.1:8869/' or 'localhost:8869/' to visit the home page to check the working of the server.


### ===== ###
Transaction Endpoints: https://github.com/Khairajani/fullstackk_assignment/tree/main/transaction
### ===== ###

Regards: Himanshu Khairajani
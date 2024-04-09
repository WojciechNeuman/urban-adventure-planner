<div align="center">
  <img src="static/images/logo_uap.png" alt="UAP Logo" width="100" height="100">
  <h2>Urban Adventure Planner</h2>
</div>


### Project goal

**UAP** will allow users to add their propositions for city tours by adding points on the map. Our application is going to calculate the fastest way that connects these points and display its length and predicted time for making the trip. Added tours will be grouped by cities and profiles.

This project is made as a part of Geospatial Data Processing course at Universitat Politècnica de València.


### Technologies used

[![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Railway.app](https://img.shields.io/badge/railway.app-%23000000.svg?style=for-the-badge&logo=railway&logoColor=white)](https://railway.app/)
[![Retool](https://img.shields.io/badge/retool-%2300C58E.svg?style=for-the-badge&logo=retool&logoColor=white)](https://retool.com/)



### How to run the project

#### Disclaimer
```
This repository doesn't contain websiteManager/settings.py file that holds credential database data. Without this file setting up the project won't work. 

You can make it work by adding the file setting up your own empty database and running 'python manage.py migrate' before step 4.
```

1. Clone repository & move into the directory

```shell
git clone https://github.com/WojciechNeuman/urban-adventure-planner.git

cd urban-adventure-planner
```

2. Set up the virtual environment (Mac & Linux)

```shell
pip install virtualenv

virtualenv env

source env/bin/activate
```

3. Install the requirements
```shell
pip install -r requirements.txt
```

4. Run the server
```shell
python manage.py runserver
```

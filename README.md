# introduction
The Teachers a lounge is a platform for professionals to share teaching materials. In this why this projects would like to improve access to teaching material from teachers all over the world. 

- [Link deployed API](https://drf5.herokuapp.com/)

This repository contains the API database. Wich is linked to a React front-end: 

- [Link deployed front-end](https://dashboard.heroku.com/apps/languageteach)
- [Front-end Github](https://github.com/Vanhouttestien/languageteachtool)


# Table of contents

- [introduction](#introduction)
- [Entity Relationship Diagram](#entity-relationship-diagram)
- [testing](#testing)
  - [validator testing](#validator-testing)
  - [manual testing](#manual-testing)
- [bugs](#bugs)
  - [fixed](#fixed)
  - [unfixed](#unfixed)
- [technologies used](#technologies-used)
- [Agile Development](#agile-development)
- [languages](#languages)
- [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Deployment](#deployment)
- [credits](#credits)
  - [code](#code)
  - [Others](#others)

# Entity Relationship Diagram
The database contains of 3 models, the user model (which was provided by Django allauth), the profile model and the post model. 

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1670848374/drf_erd_rkbxhw.jpg" alt="Entity Relationship Diagram" width="300px">
# testing
## validator testing
PEP8 errors where fixed only too long lines in setting.py remained

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1670847825/pep8_puax8q.jpg" alt="PEP8" width="300px">


## manual testing

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1670847205/CRUD_functionality_l9oiqg.jpg" alt="Table of crud functionality" width="300px">
<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1670848182/filtertest_zrzqws.jpg" alt="Table of filter functionality" width="300px">

# bugs 
## fixed
- My logout function didn't work as expected. It wouldn't logout. This was fixed by adding the logout path in de API urls. 
- I couldn't set my languages choices in the profile model to allow blank. So to solve this I added a none category and filtered these out in the frontend. 

## unfixed 
No known unfixed bugs
# technologies used

# Agile Development
To support the development of this project Agile development was used. The Automated Kanban from GitHub was used as a project management tool. User stories and found bugs were raised as issues. 

# languages
Python

# Frameworks, Libraries & Programs Used
- Git: Git was used to commit and push to GitHub 
- [GitPod](https://gitpod.io/): Gitpod was used as a development environment 
- [GitHub](https://github.com/): Github was used to deploy the site and store it  
- [Balsamiq](https://balsamiq.com/): used to create wireframes
- [DrawSQLl](https://drawsql.app/): used to create the database schema.
- [Google Fonts](fonts.google.com/): Google fonts was used for the font styles
- [Bootstrap](https://getbootstrap.com/): Bootstrap was used for frontend design
- [cloudinary](https://cloudinary.com/): was used to store images and static files.
- [Heroku](https://www.heroku.com/): Heroku was used for the deployment


- [asgiref](https://pypi.org/project/asgiref/1.1.1/)
- [gunicorn](https://gunicorn.org/):  HTTP server 
- [psycopg2](https://pypi.org/project/psycopg2/):PostgreSQL database adapter
- [dj-database-ur](https://pypi.org/project/dj-database-url/):12factor inspired database_url environment
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/): Authentication
- [Django](https://www.djangoproject.com/):  Python web framework
- [django-allauth] (https://django-allauth.readthedocs.io/):Authentication
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/): Media storage
- [django-cors-headers](https://pypi.org/project/django-cors-headers/):allows in-browser requests to your Django application from other origins
- [django-filter](https://django-filter.readthedocs.io/en/stable/): Used to let user filter the data
- [djangorestframework](https://www.django-rest-framework.org/): framework to build the API
- [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/): Web Token authentication
- [oauthlib](https://oauthlib.readthedocs.io/):Authentication
- [PyJWT](https://pyjwt.readthedocs.io/):Encode and decode JSON Web Tokens
- [python3-openid](https://pypi.org/project/python3-openid/):Support use of the OpenID decentralized identity system
- [pytz](https://pypi.org/project/pytz/):cross platform timezone calculations
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/):Authorasition
- [sqlparse](https://pypi.org/project/sqlparse/): parsing, splitting and formatting SQL statements

# Deployment


# credits 
## code
- The code was based on [the Django Rest Framework walkthrough of code institute](https://github.com/Code-Institute-Solutions/drf-api/blob/ed54af9450e64d71bc4ecf16af0c35d00829a106/drf_api/urls.py).
- [Stackoverflow](https://stackoverflow.com/)

## Others
- The code institute tutors: helping with debugging
- Martina Terlevic:  Code Institute Mentor


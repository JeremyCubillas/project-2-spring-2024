# Web Security Overview and Login and Registraion with User Profile

In this assignment, you will need to watch the video and review the code discussed. You will need to add the code to
make the Login, Registration, and User Profile model work.

## Screenshots of the code

## Overview Video

1. [Web Security Overview](https://youtu.be/xBSd-U-QB7g)
2. Repository and Video The Shows HOw to Deploy the App on Oracle Cloud using Docker  [Fixes Video Mistake in Video 1](https://github.com/kaw393939/docker-nginx-flask)
3. [Code OVerview for Login and Adding The Profile Model and Form](https://youtu.be/ScfbDhiUdG4)

## Screenshots of the code

### Login Code
1. [Login route]()

# local Install Commands

1. pip(3) install -r requirements.txt
2. flask db upgrade
3. flask --debug run or flask run (no debugging)
4. pytest

# Docker Install / Run Commands

1. docker compose up --build

## Fix Mac Permission Error after docker compose up --build  command - Run these on the terminal

* chmod +x ./development.sh
* chmod +x ./production.sh

# General Readings - You should at least look these over because you will need to refer to these in the future for your project.

* [Flask Routing](https://hackersandslackers.com/flask-routes)
* [Simple Faker tutorial](https://zetcode.com/python/faker/)
* [Faker in  Depth](https://towardsdatascience.com/faker-library-in-python-an-intriguing-expedient-for-data-scientists-7dd06f953050)
* [Jinja Templates  In Depth](https://realpython.com/primer-on-jinja-templating/)
* [Flask SQL ALchemy Tutorial](https://pythonbasics.org/flask-sqlalchemy/) <-this a general tutorial and some of our
  file names and directory structure is different.
* [Flask Blueprints](https://realpython.com/flask-blueprint/)
*

# Docker Commands

* docker compose up --build <- builds the image in development mode and shares the volume
* docker compose up <- runs the previously built image without redoing the build process
* docker build -t myapp . <- builds it to run with gunicorn in production mode
* docker run -itp 80:8080 myapp <- runs the website / flask in console output mode
* docker exec -it <containerid> bash <- logs into container (replace <containerid> with the container id)
* docker run -itp 80:8080 myapp pytest <-runs pytest in the container image

# Flask Migrate / Alembic Commands - Must delete the migrations and instance folder / database. These will reset it

* flask db init <-initializes migrations (don't need to do this the project has its first migration)
* flask db migrate -m "Initial migration." <-change the message to whatever describes the schema change
* flask db upgrade <- applies the migrations

# Libraries

* https://flask.palletsprojects.com/en/2.2.x/
* https://www.sqlalchemy.org/
* https://alembic.sqlalchemy.org/en/latest/
* https://github.com/miguelgrinberg/flask-migrate
* https://flask-wtf.readthedocs.io/en/1.0.x/  <-Very Useful
* https://bootstrap-flask.readthedocs.io/en/stable/
* https://getbootstrap.com
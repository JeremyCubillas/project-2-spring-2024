# Project 2

For this project, you need to fix 16 tests by running each test individually and fixing the error. Many of the errors
are just the wrong text is being displayed or it is not redirecting the user to the proper web page; however, some
errors are more challenging.

## In addition, you will need to implement the following functionality:

1. A user goes to the homepage
2. A user clicks on the link for "Calculate Sample"
3. If the user is not logged in they are prompted to login and after login they are redirected to a sample calculation
   form.
4. The sample calculation form should have a dropdown form control to select the z-score / confidence.
5. Once the user enters the values they should press the submit button and be redirected to a list of sample size
   calculations that they have previously entered.

## How to complete the project

### Fis each test in order by running pytest tests/<replace with name of test>.py

1. test_about_page.py
2. test_index_page.py
3. test_login_bad_password.py
4. test_login_dashboard.py
5. test_login_success.py
6. test_login_user_not_found.py
7. test_logout.py
8. test_profile_controller.py
9. test_profile_model.py
10. test_registration_duplicate_fail.py
11. test_registration_success.py
12. test_sample_authenticated_menu.py
13. test_sample_login_redirect.py
14. test_sample_model.py
15. test_sample_route.py
16. test_sample_unauthenticated_menu.py

## Unit Videos

1. [Project Overview and Instructions](https://youtu.be/KmB3ZhFnsZg)

#### Basically, you should learn is this workflow:

1. Add the model, create a migration, do the db upgrade
2. Write tests to test the model
3. Make a form class and html template to display the form
4. Make a controller for that page and add the logic to process the form as necessary
5. Write a test for the controller
6. Write tests as necessary to verify redirection to wherever the user can view the submitted data.

* Note: Don't forget that you should make tests assert the condition of the database, perform an action to insert a
  record, and then check the database to see that its added

## Screenshots of the code

All the following code goes in the route file [here](application/bp/authentication/__init__.py)

1. [Improved Registration with Hashing](readme_images/registration_route.png)
2. [Login Route](readme_images/registration_route.png)
3. [Logout Route](readme_images/login_route.png)
4. [User Profile Route](readme_images/profile_route.png) <- pay attention to how i use current_user to get the
   currently logged-in users information

## Code you also need to review / Understand

1. [Database Models](application/database/__init__.py) <- Look at how I set up relationships and add fields
2. [Form Example for User Profile](application/bp/authentication/forms/__init__.py) <- Look at how the class properties
   for the profile match the database profile model
3. [Example of a template to display a form - Same as any template but you need to change the title of the page](application/bp/authentication/templates/login.html)
4. [How I control visability of links in the main menu](application/templates/base.html) <- Look how i check for the
   user being authenticated with a jinja if statement

### Login Code

1. [Login route]()

# Optional Readings

1. [SQL Alchemy with Flask Relationships](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/)
2. [Flask Routing](https://hackersandslackers.com/flask-routes/)
3. [Flask WTF Forms](https://www.digitalocean.com/community/tutorials/how-to-use-and-validate-web-forms-with-flask-wtf)
4. [Flask Login Explained](https://www.freecodecamp.org/news/how-to-authenticate-users-in-flask/)

# local Installation Commands

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
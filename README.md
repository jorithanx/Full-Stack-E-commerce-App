[![Build Status](https://travis-ci.org/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce.svg?branch=master)](https://travis-ci.org/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce)

# Project 4 - Ecommerce (full stack web application)
This project is built for [Code Institute](https://codeinstitute.net/) as a part of _Full Stack Software Development Diploma course_. Project was build with using semantic HTML5, CSS3, JavaScript along with Python framework Django 2.2.

:grey_exclamation: The project had been built with the project requirements published before July 2019. :grey_exclamation:

Live version deployed on Heroku [here](https://django-ecommerce-milestone.herokuapp.com/).


## Table of Contents
* [UX](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#ux)
   * [User Stories](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#user-stories)
   * [Wireframes](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#wireframes)
* [Technologies Used](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#technologies-used)
* [Features](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#features)
   * [Register Account](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#register-account--)
   * [Change Password](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#change-password-)
   * [Searching scooters](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#searching-scooters)
   * [View a particular scooter detail](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#view-a-particular-scooter-detail)
* [Testing](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#testing)
   * [HTML](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#html)
   * [CSS](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#css)
   * [JavaScript](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#javascript)
   * [Python](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#python)
   * [Automated Testing](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#automated-testing)
* [Deployment](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#deployment)
   * [Local Deployment](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#local-deployment)
   * [Remote Deployment](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#remote-deployment)
* [Contriting](https://github.com/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce#contributing)


## UX
This is aiming at people who are looking for buying a kick scooter, eScooter or scooter for kids.

### User Stories

* As a user I want to sing up so that I have my own account
* As a user I want to login so that I can see my profile page
* As a user I want to logout 
* As a user I want to see my main page as the first so that I can easily select which scooter I want
* As a user I want to see shopping cart on every page
* As a user I want to see a summary of my cart so that I can easily see my purchases
* As a user I want to see a summary of my cart so that I can easily remove items
* As a user I want to see a summary of my cart so that I can easily amend the amount of items
* As a user I want to see a summary of my cart so that I can easily see how much it costs
* As a user I want to have intuitive access to the checkout page so that I can easily proceed with the payment
* As a user I want to have a search field so that I can look up items
* As a user I want to see if the scooter is in stock
* As a user I want to have mobile friendly website layout so that I can use my smart phone to purchase products

### Wireframes:  
The following wireframes were created in order to provide a starting point for the website skeleton:

* [mobile device](wireframes)
* [desktop device](wireframes)


## Technologies Used
I used following technologies for this particular project:
* HTML5
* CSS3
   * [Bootstrap](https://getbootstrap.com/)
   * [Font Awesome](https://fontawesome.com/)
* [Python](https://www.python.org/)
   * [Django 2.2](https://docs.djangoproject.com/en/2.2/releases/2.2/)
* Javascript ([jQuery](https://jquery.com/))
* [Stripe](https://stripe.com/)
* [AWS S3](https://aws.amazon.com/s3/)
* [SQLite](https://www.sqlite.org/index.html)
* [Postgresql](https://www.postgresql.org/)
* [Heroku](https://heroku.com/)
* [Adobe Xd](https://www.adobe.com/cz/products/xd.html)
* [VS Studio Code](https://visualstudio.microsoft.com/cs/?rr=https%3A%2F%2Fwww.google.ie%2F)
* [GIMP](https://www.gimp.org/)


## Features
Based on the project brief, I have successfully implemented the follow features:

### Register Account :heavy_plus_sign:
   * Anybody can register for free and create their own unique account. This is built using Django's authentication   and authorization to validate profile data. Passwords are hashed for security purposes!

### Change Password :closed_lock_with_key:
   * Users can update their passwords from their profile page. They will receive an email with instructions with the link, where the password can be changed.

### Searching scooters
   * Users can easily use search input to find what they are looking for.

### View a particular scooter detail
   * Users can click on a praticular scooter to see details about the choosen scooter.


## Testing 
A thorough mix of automated and manual testing have gone into building the project. In addition to tests, I have validated all files against online validation sites, and checked compatibilities across various modern browsers and devices.

### HTML
* [W3C HTML Validator](https://validator.w3.org/)
   * All 25 .html files have been checked
   * Other validation issues are related to Django Templating not being recognized by W3C:
      * **Warning:** Consider adding a `lang` attribute to the `html` start tag to declare the language of this document
      * **Error:** bad value `{% foo %}`
      * **Error:** Non-space characters found without seeing a doctype first. Expected `<!DOCTYPE html>`
      * **Error:** Element `head` is missing a required instance of child element `title`

### CSS
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
   * The W3C Jugsaw validator did not found any errors. Only 3 **warnings**
      * `-webkit-background-size` is an unknown vendor extension
      * `-moz-background-size` is an unknown vendor extension
      * `-o-background-size` is an unknown vendor extension

### JavaScript
* [JSHint](https://jshint.com/)
   * Not found any major **errors**

### Python
* [PEP8 online](http://pep8online.com/)
   * Not found any major **errors**

### Automated Testing

With `TestCase` and `SimpleTestCase`, I built **36** different tests to test most of my python views, forms and models.

In addition to the `TestCase` and coverage.py tests, I have used [Travis-CI](https://travis-ci.org/) to test Continuous Integration. At the beginning, I had the problem due to the fact that my project is in src dir instead of top-level dirm which is why there are many various commits, but in the end it was sordted with successful passing build badge.

[![Build Status](https://travis-ci.org/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce.svg?branch=master)](https://travis-ci.org/Tomas-Kaiser/Code-Institute-Milestone-4-Full-Stack-App-Ecommerce)

I also used Chrome Lighthouse:
The Lighthouse is an open-source automated tool that audits website for performance, accessibility, best practices & SEO. The website current score as follows:

```
> Performance at 96
> Accessibility at 91
> Best practices at 86
> SEO at 90

the highest score is 100
```

### Manual Testing

The manual testing was accomplished mainly by using following technologies/tools:

* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/) - Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser. DevTools can help you edit pages on-the-fly and diagnose problems quickly, which ultimately helps you build better websites, faster.

* Web browers such as:
   * Chrome
   * Opera
   * Mozilla
   * Microsoft Edge
   * Safari

* Devices:
   * Desktop
   * Mobile Phone (iPhone S5)


## Deployment
This project is deployed on heroku: https://django-ecommerce-milestone.herokuapp.com/

### Local Deployment
It's highly recommended to work in a virtual environment, but not absolutely required.

In order to run this project locally on your own system, you need following:
   * [Python3](https://www.python.org/downloads/) to run the application
   * [PIP](https://pip.pypa.io/en/stable/installing/) to install all requirements
   * [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control or you can just download the repo in zip format
   * IDE (for example [Microsoft Visual Studio Code](https://code.visualstudio.com/))

Next steps in order to proceed with local deployment:
   * Clone the repo with command `git clone https://github.com/TravelTimN/ci-milestone05-fsfw.git` or donwloand the zip file
   * Navigate to the correct file location after unpacking the files `cd <path to folder>`
   * Create `.env` with `pipenv shell`
   * Install all requirements with `pip3 -r requirements.txt`
   * launche the project `python manage.py runserver`
   * The Django server should be running locally now on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   * When running the Django server for the first time, it should create a new SQLite3 database file: db.sqlite3
   * next steps are: `python manage.py makemigrations` and `python manage.py migrate`
   * To have an access to Django Admin Panel, you must generate a superuser:
      * `python manage.py createsuperuser`
   
### Remote Deployment
This project is currently deployed on [Heroku](https://heroku.com) using the master branch on GitHub. You can proceed to deploy it remotely with the following steps:
   * Create a requirements.txt
      * `pip3 freeze --local > requirements.txt`
   * Create a Procfile to tell Heroku what type of application is being deployed using gunicorn, and how to run it:
      * `echo web: gunicorn main.wsgi:application > Procfile`
   * Sign up for a free Heroku account (max 5 projects are for free tier), then create your project app and click the Deploy tab. You can also Connect your GitHub as the Deployment Method.
   * In the Heroku Resources tab, navigate to the _Add-Ons_ section and search for **Heroku Postgres**. Make sure to select the free Hobby level. This will allow you to have a remote database instead of using the local sqlite3 database, and can be found in the Settings tab. You'll need to update your .env file with your new database-url details
   * In the Heroku Settings tab, click on the Reveal Config Vars button to configure environmental variables. You might need to copy/paste all of the .env key value pairs into the config variables
   * Update the settings.py file to connect the remote database using this Python package: `dj_database_url`
   * Re-build the migrations and create a superuser to your new remote database
   * Sign up for a free [Amazon AWS](https://aws.amazon.com/) account in order to host your staticfiles and media files. From the **S3 buckets** section, you'll need to create a new unique bucket. Find more here, how to set up [AWS S3 Bucket](https://docs.aws.amazon.com/quickstarts/latest/s3backup/step-1-create-bucket.html)
   * After creating your AWS S3 Bucket, you should now be able to push the static files to AWS if everything is configured properly using this command `python manage.py collectstatic`
   * Sign up for a free [Stripe](https://stripe.com/ie) account. Navigate to the Developers section, and click on API Keys. You should have two confidential keys which need to be added to your .env file, as well as your Heroku config vars.
      * `Publishable Key`: pk_test_key and `Secret Key`: sk_test_key
Now your project should be completely setup and ready for remote deployment! 


## Contributing :credit_card:
This repository is a part of project for Code Institute of a Full Stack Software Development course. Therefore, I will most likely not accept pull requests.
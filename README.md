# User_Account_API
A register django app that consist of all that you need to know in creating a custom user model and handling email login of users in python/django.

## Table of Contents

- [Prerequisites:](#prerequisites)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Setup](#setup)
- [Running the API](#running-the-api)


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python3 3.x installed.
- Pip package manager installed.
- A code editor (e.g., VSCode) for development.
- Postman or a similar tool for API testing.

## Technologies
* Python 3.8.10
* Django 4.2.10
* Django Rest Framework 3.14.0
* SQLite3

## Getting Started

### Installation

* Clone the repository:

   ```bash
   https://github.com/micky225/Django-UserAccount-API.git

### Setup
* To create a normal virtualenv (example .venv) and activate it (see Code below).

  ```
  virtualenv --python=python3.18.10 .venv
  
  source .venv/bin/activate

  (venv) $ pip install -r requirements.txt

  (venv) $ python manage.py makemigrations

  (venv) $ python manage.py migrate

  (venv) $ python manage.py createsuperuser 

  (venv) $ python manage.py runserver

### Running the API

*The API will be available at http://localhost:8000/.*


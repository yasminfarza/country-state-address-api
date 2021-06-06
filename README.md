# Country-State-Address-Api
> API’s create with Django Rest Framework and MySQL

## Table of Contents
* [General Info](#general-information)
* [Technologies](#technologies)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)


## General Information
- This project is simple api for country, state, address.
- Use [CircleCI](https://circleci.com/) for automate development process.
- All APIs are authenticated.
- Provide testCase for all APIs.


## Technologies
- Django
- Django Rest Framework
- MySQL


## Features
In the project, you can find the API's:
- List all countries, with the option to filter countries by name and code.
- List all states by countries, with the option to filter states by name.
- List addresses of states, with the option to filter addresses by house_number and road_number.
- An api to fetch a detailed address that will return the address along with it’s respective state and country.


## Setup

### Requirements
- Python - version 3.8
- Python Virtualenv
- Django - version 3.2.3
- Django Rest Framework - version 3.12.4
- MySQL - version 8.0.21

`Note: Django and Django Rest Framework will be installed using virtualenv`

### Installation
```
# Clone this repository
$ git clone https://github.com/yasminfarza/country-state-address-api

# Go into the repository
$ cd country-state-address-api

# Create virtualenv
$ python -m venv env

# Activate virtualenv
$ source env/Scripts/activate

# Install packages
$ pip install -r requirements.txt

# Create a database
# Copy the contents of country_state_address/.env.example to country_state_address/.env and
  modify country_state_address/.env as necessary

# Migrate the database
$ python manage.py migrate

# Create new user
$ python manage.py createsuperuser

# Load dummy data (Optional)
$ python manage.py loaddata seeds/*

# Run all test cases
$ python manage.py test

# Run the project
$ python manage.py runserver
```

## Usage
URL for checking the api in browser:

* [/api-auth/login/](http://localhost:8000/api-auth/login/) - Login url
* [/api/countries/](http://localhost:8000/api/countries/) - Countries api url
* [/api/countries/?name=bangladesh&code=bd](http://localhost:8000/api/countries/?name=bangladesh&code=bd) - Filter countries by name and code
* [/api/states/bangladesh/](http://localhost:8000/api/states/bangladesh/) - States by country api url
* [/api/states/bangladesh/?name=dhaka](http://localhost:8000/api/states/bangladesh/?name=dhaka) - Filter states by name
* [/api/addresses/states/dhaka/](http://localhost:8000/api/addresses/states/dhaka/) - Addresses of states api url
* [/api/addresses/states/dhaka/?house_number=03&road_number=5](http://localhost:8000/api/addresses/states/dhaka/?house_number=03&road_number=5) - Filter addresses by house_number and road_number
* [/api/addresses/](http://localhost:8000/api/addresses/) - Addresses api url
* [/api/addresses/19/](http://localhost:8000/api/addresses/19/) - Address details api url

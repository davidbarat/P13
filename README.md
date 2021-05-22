# P13

[![Build Status](https://travis-ci.com/davidbarat/P13.svg?branch=master)](https://travis-ci.com/davidbarat/P13)

The purpose of this project is to allow user to send sos message to a list of trusted persons.

![Screenshot](https://github.com/davidbarat/P13/blob/main/imagesite.png)

## Main steps of the app
1. The user has to fullfill the registration form,
2. Once connected, you can make a simple search, 
3. The site will return a list of product with a better nutriscore grade,
4. The user can have a detail view of the product and then if you mind, you can store your new fav product.
5. Finally the user can find all his new products in a myproducts link in the navbar at the top.

## Data
* All Data came from OpenFoodFacts Api, please follow the link below if you want more informtions:
https://fr-en.openfoodfacts.org/
	
## Technologies:
This site uses:

* Bootstrap
* Python 3.6
* Django 3.1
* Raspberry 

## requisite
* Postgresql database

## Installing

Fork the project on your local machine and launch the script via these commands:

    pip install -r requirements.txt
    ./manage.py runserver

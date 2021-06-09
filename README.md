# P13

[![Build Status](https://travis-ci.com/davidbarat/P13.svg?branch=master)](https://travis-ci.com/davidbarat/P13)

The purpose of this project is to allow user to send SOS message via SMS to a list of trusted persons.
These persons are, this is the group of person to call in case of emergency

![Screenshot](https://github.com/davidbarat/P13/blob/main/imagesite.png)

## Main steps of the app rapsberry side
1. You have to follow pdf document to install and configure the app on your Raspberry:
P13_05_note_installation_raspberry.pdf
2. You have to add to your profile, groupname vars:
For example:
export groupname = 'raspberry3'


## Main steps of the app web site side
1. The user has to fullfill the registration form,
2. Once connected, you can create a group of person or list all group already created

Once service is running on Raspberry side and users created in the web site. You can press button 1 on your IR controler, it will send an emergency SMS to all your group phone number.
	
## Technologies:
The Django site uses:

* Bootstrap,
* Python 3.6,
* Django 3.1,
* Postgresql,

The Raspberry uses:
* Buster Debian,
* IR controler and receiver,
* jumper and breadboard,
* LED and resistor,

## Installing

Fork the project on your local machine and launch the script via these commands:

    pip install -r requirements.txt
    ./manage.py runserver

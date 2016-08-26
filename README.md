# Project: Places "Microservice"
# CodeName: pyPlaces

## Description
    This project provides a series of endpoints that returns information 
    from several places in the world


## Running the project Localy
 * Prerequisities: python2.7 and python-pip in order to install libraries from python
    * Python libraries
        - python-flask
        - requests
        - httplib2
        - flask-httpauth
        
 * In order to create the schema you need to:
 	* 1- run this command in the terminal
 		$ python database_setup.py
 	* 2- once created the schema you need to run this command, in order to add some data into the database 
 		$ python lots_of_places.py
 * To run the webserver you need to run this command from the terminal:
    - $ python places.py
    - this will fire up the webserver, after this you should access this URL from a webbrowser
        http://localhost:5000/


## JSON APIS URLS

    ### GET ALL THE cOUNTRIES
        - http://localhost:5000/api/v1/countries
    ### GET ALL THE PLACES
        - http://localhost:5000/api/v1/places
    ### GET THE DETAILS INFORMATION OF A PLACE
        - http://localhost:5000/api/v1/places/[ITEM_ID]
    ### GET ALL THE TYPES OF PLACES
        - http://localhost:5000/api/v1/types
# shub

This is just a simple web service that pulls information from the Scrapinghub Github and orders their top 10 open source projects by number of stars

A new python virtual environment was set up to prevent issues from other packages and/or version issues with older packages.
A requirements text file has been included - most of which are dependencies from Flask.

## Installation
Once you have your new environment activated, go to the location of the requirements file in terminal and type 

``pip install -r requirements.txt``


After this you can clone this repository and then type the following into your terminal.

``export FLASK_APP=app.py``

``python -m flask run``


Following this, you can navigate to ``http://127.0.0.1:5000/`` in your browser and the web app should load.

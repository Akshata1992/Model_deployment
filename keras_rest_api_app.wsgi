"""
--*utf-8*--
Author: Akshata
Usage:keras_rest_api_app.wsgi , is a new component to our deep learning REST API compared to last week.

This WSGI configuration file adds our server directory to the system path and imports the web app to kick off all the action. We point to this file in our Apache server settings file, /etc/apache2/sites-available/000-default.conf
"""
# add our app to the system path
import sys
sys.path.insert(0, "E:/DevOps/Flask")
# import the application and away we go...
from run_web_server import app as application
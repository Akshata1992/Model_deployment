# Model_deployment
# Branch: Flask_API_Apache_Server
Image classification:
 - Model : ResNet50
 - Framework : Keras
 - Web API : Flask Application
 - Server: Apache

Important files in the project:

1. run_web_server.py contains all our Flask web server code — Apache will load this when starting our deep learning web app.
2. run_model_server.py will:
 - Load our Keras model from disk
 - Continually poll Redis for new images to classify
 - Classify images (batch processing them for efficiency)
 - Write the inference results back to Redis so they can be returned to the client via Flask
3. settings.py contains all Python-based settings for our deep learning productions service, such as Redis host/port information, image classification settings, image queue name, etc.
4. helpers.py contains utility functions that both run_web_server.py and run_model_server.py will use (namely base64 encoding).
5. keras_rest_api_app.wsgi contains our WSGI settings so we can serve the Flask app from our Apache server.
6. simple_request.py can be used to programmatically consume the results of our deep learning API service.
"dog.jpg" is a photo of my family’s beagle. We’ll be using her as an example image when calling the REST API to validate it is indeed working.
7. Finally, use stress_test.py to stress our server and measure image classification throughout.

# Branch: Heroku - PAAS deployment for salary predictions
I. Model: Linear Regression
 - Web API: Flask
 - Server: Heroku - PAAS
 - API Link: https://linear-salary-predictions.herokuapp.com/

Important files:

1. model.py: Linear model for salary prediction with customized dataset
2. model.pk: model pickle file
3. app.py : Flask application
4. request.py : request with post method
5. requirements.txt: all libraries required for model
6. templates folder: html templates for app.route
7. procfile: procfile for Heroku to indicate which app file to be executed first(flask app name)
8. Commands to check deployment logs:
 - Open command prompt and enter 'heroku login'
 - Once logged in, enter heroku logs --app
 
 II: NLP Model to detect Spam/Ham email
  - Model: Naive-Bayes
  - Web API: Flask
  - Server: Heroku - PAAS
  - API Link:
  

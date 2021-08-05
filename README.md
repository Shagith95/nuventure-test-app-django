# Nuventure Test-App using Django

 - Django app to fetch and parse data from nominatim and provide API response with data caching
 - Unit test to check caching

# Setup
Navigate to the project directory and run the following commands with a python environment with python3.6+

    pip install -r requirements.txt
    python manage.py createcachetable

# API

Start the Django development server locally by

    python manage.py runserver

Use the following URL to get the API response

> lat - Latitude coordinate

> lon - Longitude coordinate

    http://localhost:8000/myapp/get_address/<lat>/<lon>/

Use this [link](http://localhost:8000/myapp/get_address/-34.4391708/-58.7064573/) to access (-34.4391708, -58.7064573) once the development server is running

# Running Test

Run the Django test by

    python manage.py test

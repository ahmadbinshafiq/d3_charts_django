# d3 chart

Behold My Awesome Project!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)

License: Apache Software License 2.0


## Basic Commands

### Docker (Recommended)
This project is dockerized. To run the project, you need to have docker and docker-compose installed.

Run the following commands to start the project:

```bash
docker-compose up
```

### Local environment (linux)

To run the project locally, you need to have Python 3.12.3 installed.


NOTE: If you are running this project locally, you should have a PostgreSQL database running on your machine. 
You can use the docker-compose file to run a PostgreSQL database. 

To use postgresql with docker-compose, run the following command:

```bash
docker compose up postgres-db
```

If you want to use a different database, you can update the `POSTGRES_CONNECTION_STRING` in the `.env` file.


1. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install the dependencies:

```bash
pip install -r requirements/local.txt
```

3. Run the migrations:

```bash
python manage.py migrate
```

4. Run the server:

```bash
python manage.py runserver
```


### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest


<br />

### API Documentation

The server is running on `http://localhost:8000/`.

There are two endpoints available:

1. `/chart/chart` - This endpoint returns the d3 chart template.
2. `/chart/api/chart-data/` - This endpoint returns the data for the d3 chart.

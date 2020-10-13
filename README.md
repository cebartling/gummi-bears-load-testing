# gummi-bears-load-testing
Load tests for Gummi Bears!

## Setup

1. Install pipenv via brew: `brew update && brew install pipenv`
2. Create a virtualenv environment using a recent Python 3 runtime: `pipenv --python 3.8`
3. Verify your Python 3 runtine installed: `pipenv --py`
4. Install the dependencies in the Pipfile into your virtualenv environment: `pipenv install`
6. Activate the virtualenv environment: `pipenv shell`
7. Verify the locust installation: `locust -V`. You should see something like... `locust 1.2.3`.

## Setting up the .env file
A `.env` file should reside in the root directory of this repository. It is not version controlled due to sensitive account information.

```dotenv
GUMMI_BEARS_DB_USERNAME=
GUMMI_BEARS_DB_PASSWORD=
GUMMI_BEARS_DB_HOSTNAME=
GUMMI_BEARS_DB_PORT=
GUMMI_BEARS_DB_DATABASE=
```

## Running the load test suite


1. From the activated virtualenv environment: `locust --config=.locust.conf`


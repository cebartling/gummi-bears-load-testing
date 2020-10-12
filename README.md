# gummi-bears-load-testing
Load tests for Gummi Bears!

## Setup

1. Install pipenv via brew: `brew update && brew install pipenv`
2. Create a virtualenv environment using a recent Python 3 runtime: `pipenv --python 3.8`
3. Verify your Python 3 runtine installed: `pipenv --py`
4. Install locust into your virtualenv environment: `pipenv install locust`
5. Install locust-plugins into your virtualenv environment: `pipenv install locust-plugins`
6. Activate the virtualenv environment: `pipenv shell`
7. Verify the locust installation: `locust -V`. You should see something like... `locust 1.2.3`.
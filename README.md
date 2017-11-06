# Birdee

A centralized notification system for Hasadna projects

## Development

To utilize the tools included, remember to always use class based Views, define forms and use ModelAdmin classes.

The idea behind Django, and consequentially the tools included in this app, is to reduce the amount of time developers
puts into making their environment work the way they see it.

### Requirements

(Unless specified, the recommended version is the latest stable)

* Python >= 3.6.1 (system or via pyenv)
* pip (for python 3)
* [pipenv](https://docs.pipenv.org/)
* [Docker](https://www.docker.com/community-edition)
* [docker-compose](https://docs.docker.com/compose/install/)
* [bower](https://bower.io/#install-bower)

### Start

This bootstrap is opinionated, so many settings are already pre-defined, but some require setup by the specific developer.

* Run `bower install -F` to get all static assets (jQuery, Bootstrap etc.)
* Copy `local_settings-example.py` to `local_settings.py` and configure the information you need
  * `SECRET_KEY` can be any string, on production this should be a long complex random string
  * `ALLOWED_HOSTS` if `DEBUG` is `False` you will need to specify the domains used (so if you use 'http://localhost:8000' to access the app, then `ALLOWED_HOSTS` should have 'localhost' as an item)
  * `DATABASES` if you are using the docker postgres, just uncomment and leave it as is
* Run `docker-compose -f docker-compose-dev.yml up -d` to get a PostgrSQL instance running (or have one running locally, in that case configure
* Run `pipenv install`
* Run `pipenv run python manage.py migrate`
* Run `pipenv run python manage.py createsuperuser` to create your first admin user
* Run `pipenv run python manage.py runserver` to start the dev server

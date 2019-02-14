# nasa

NASA Facilities 

This application provides functionality to:

1. Download NASA Facilities data from https://data.nasa.gov/Management-Operations/NASA-Facilities/gvk9-iz74
   and store the data in a local Sqlite database

2. Serve the data through an API

3. Provides a means to update the data for an admin user which you create during installation

## Prerequisites

Ubuntu 16.04

libsqlite3-dev

## Installation

Download or clone the repository into a local directory and from the root run:

```
./setup.sh
```

This script will:

1. If ran as sudo, it will try to install libsqlite3-dev, as mentioned in the prerequisites. No other steps require sudo, so if not will complete fine.
2. Download and setup pyenv
3. Install Python 3.6 into pyenv
4. Download and install the pyenv-virtualenv plugin
5. Create a new virtualenv called venv and install the python dependencies from the requirements.txt into this virtualenv
6. Pull JSON data from https://data.nasa.gov/resource/9g7e-7hzz.json into a local Sqlite database
7. Prompt the user to create a superuser that can login and modify the data


## Getting Started

To start the application, activate the virtualenv using:

```
export PYENV_ROOT=$(pwd)/.pyenv
export PATH=$PYENV_ROOT/bin:$PATH
eval "$(pyenv init -)"
pyenv activate venv
```

Run the development server:

python nasa/manage.py runserver


## Usage


### Add facilities

To add new facilities to the application, use the Django manage.py to invoke the add_facilities custom management command:

```
python manage.py add_facilities
```

When using this command, if any of the fields in the database are different compared to the JSON document, a new record will be added.

## Edit facilities

The application includes the Django admin site, through which facilities can be edited but not added/removed. Login with the superuser 
created during installation to edit the records.


## API

To get started with the API, view the documentation at /docs



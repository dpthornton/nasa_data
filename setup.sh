printf "\nInstalling application dependencies and setting up\n"
printf "\nPlease respond when prompted...\n\n"

apt-get install libsqlite3-dev

printf "\nInstall pyenv and create an isolated Python 3.6 installation\n"

git clone https://github.com/pyenv/pyenv.git .pyenv
export PYENV_ROOT=$(pwd)/.pyenv
export PATH=$PYENV_ROOT/bin:$PATH
eval "$(pyenv init -)"
pyenv install 3.6.0

printf "\n Install the virtualenv plugin for pyenv and create a virtualenv for python pacakges\n"

git clone https://github.com/yyuu/pyenv-virtualenv.git .pyenv/plugins/pyenv-virtualenv
eval "$(pyenv virtualenv-init -)"
pyenv virtualenv 3.6.0 venv
eval "$(pyenv init -)"
pyenv activate venv

printf "\n Install application python package dependencies from the requirements.txt\n"

pip install --upgrade pip
pip install -r requirements.txt

printf "\nSetting up a basic sqlite database and admin user (choose a username and password when prompted)\n"

python nasa/manage.py makemigrations
python nasa/manage.py migrate
python nasa/manage.py createsuperuser

printf "\nImporting NASA facilities data from https://data.nasa.gov/resource/9g7e-7hzz.json\n"

python nasa/manage.py add_facilities

printf "\Ccollecting staticfiles into single location\n"

python nasa/manage.py collectstatic

echo ""
echo ""
echo "Setup complete"
echo ""
echo "In order to start the application, activate the virtualenv first with the following commands:"
echo ""
echo 'PYENV_ROOT=$(pwd)/.pyenv'
echo "PATH=$PYENV_ROOT/bin:$PATH"
echo 'eval "$(pyenv init -)" '
echo "pyenv activate venv"
echo ""
echo "Use the Django command to start the server on port 8000 and test the application:"
echo "i.e. python nasa/manage.py runserver"

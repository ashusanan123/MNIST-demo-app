# Initialize a new virtual environment and start it
virtualenv mnist-app-env
source mnist-app-env/bin/activate

echo "Virtual Environment done"

echo "Installing dependencies"
# Install python dependencies
pip install -r requirements.txt

echo "Starting the server"
# Start the server
python manage.py runserver


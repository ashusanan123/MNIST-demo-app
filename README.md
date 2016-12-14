## MNIST Character Recognition App

MNIST-app is a web-app to demonstrate **MNIST Character recognition** using Multi-layer Perceptron. The web framework is written using Django.
The repository includes MNIST test dataset for testing the application in the end. Path to dataset **`prediction_Module/mnist-data`**

The system takes an image as a POST request and returns json value including ***fileName, predicted label and the confidence***. This json value is displayed on the webpage along with the image itself.

## How To Run

Clone or dowload the repository. Go to the repository

`$ cd /path/to/repository`

Once in the repository simply follow the mentioned steps to get the results.

### 1. Install Virtualenv if not already installed

Virtualenv is a very effective tool to create isolated Python Environment. Under the assumption that the system has `pip` installed:

`$ pip install virtualenv`

### 2. Make a new virtual environment and enter it

Make a new virtual environment and start it in the following way:

	$ virtualenv mnist-app-env
	$ source mnist-app-env/bin/activate

This will start the environment.

### 3. Install all the python requirements.

The next step is to install all the python libraries required for the application.
All the requirements are mentioned in requirements.txt file.

`pip install -r requirements.txt`

### 4. Start the server and access the webpage

	$ python manage.py migrate
	$ python manage.py runserver

Now visit **127.0.0.1:8000**

## Test

Simply upload the image from MNIST data set and the webpage will display the predicted label and the confidence for that label. For saving the user time to download and extract MNIST dataset. It is included in the repository. Path to dataset **`prediction_Module/mnist-data`**
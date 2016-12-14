from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier
import pickle
from PIL import Image
import numpy as np

filename = 'prediction_Module/trained_models/nn_trained_digit_classifier.pkl'


def predict_nn(img):
	with open(filename, 'rb') as f:
		mlp = pickle.load(f)

	predictions = mlp.predict_proba(img)
	label = np.argmax(predictions)
	confidence = np.max(predictions)*100;

	return label, confidence


# # rescale the data, use the traditional train/test split
# X, y = mnist.data / 255., mnist.target
# X_test = X[60000:]
# y_test = y[60000:]
# count = 0

# for i in range(10000):
# 	img = np.reshape(X_test[i], (28,28))
# 	img = img*255
# 	im = Image.fromarray(img)

# 	im = im.convert('1')

# 	name = './mnist-data/img'+str(count)+'.png'
# 	im.save(name)
# 	count += 1

def preprocess(image_path):
	img = Image.open(image_path)
	img = np.asarray(img.getdata(), dtype = 'float32')
	img = img / 255.

	if img.shape[0] != 28 or img.shape[1] != 28:
		img = np.resize(img, (28,28))

	return img


# This function will be called from Django website with argument as the image path
def predict(image_path, clf='NN'):

	img = preprocess(image_path)

	if clf == 'NN':
		img = img.flatten()
		label, confidence = predict_nn(img)

	return label, confidence    # The output should be a json with "name of the file, label predicted and confidence value. "



# check = './mnist-data/img5132.png'

# label, confidence = predict(check)

# print label
# print confidence



print(__doc__)

import matplotlib.pyplot as plt
import numpy as np
import pickle
from sklearn import linear_model

# trains a model and saves it as finalized-model.sav. Also tells us the error on our model
def createTrainedModel(dataset):
    # split into input X) and output (Y) variables
    X = dataset[:, 0:7]
    Y = dataset[:,7]

    # features

    # Split the data into training/testing sets
    dataset_X_train = dataset[:-20]
    dataset_X_test = dataset[-20:]

    # Split the targets into training/testing sets
    dataset_y_train = dataset.target[:-20]
    dataset_y_test = dataset.target[-20:]

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(dataset_X_train, dataset_y_train)

    # The coefficients
    print('Coefficients: \n', regr.coef_)
    # The mean squared error
    print("Mean squared error: %.2f"
          % np.mean((regr.predict(dataset_X_test) - dataset_y_test) ** 2))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % regr.score(dataset_X_test, dataset_y_test))

    # Plot outputs
    plt.scatter(dataset_X_test, dataset_y_test,  color='black')
    plt.plot(dataset_X_test, regr.predict(dataset_X_test), color='blue',
             linewidth=3)

    plt.xticks(())
    plt.yticks(())

    plt.show()

    # save the model to disk
    filename = 'finalized_model.sav'
    pickle.dump(model, open(filename, 'wb'))

def predictMidpoint(dataset_current):

    loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
    result = loaded_model.predict(dataset_current)
    return result
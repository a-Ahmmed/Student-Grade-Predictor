import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

def linearRegression(inputData: list) -> str:
    # Read in data and trim
    data = pd.read_csv("data/student-mat.csv", sep=';')
    data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]] # G references grade period 1 = First period 2 = Second period 3 = Final

    # Prediction for later (Can be changed)
    predict = "G3"

    # Define training and test data
    x = np.array(data.drop([predict], axis=1))
    y = np.array(data[predict])
    trainingDataX, testDataX, trainingDataY, testDataY = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    # Establish Model
    linear = linear_model.LinearRegression()

    # Get line of best fit based on our training data
    linear.fit(trainingDataX, trainingDataY)
    accuracy = linear.score(testDataX, testDataY) # How accurate our line of best fit is

    def testModel():
        # Get predictions given our test data (testDataX)
        predictions = linear.predict(testDataX)

        # Compare our predictions to actual student results (testDataY)
        for index, predictionValue in enumerate(predictions):
            print(f'Input Data: {testDataX[index]}\nPredicted Result: {predictionValue:.2f}\nActual Result: {testDataY[index]}\n')

    # Reformat input array into numpy array
    inputData = np.array(inputData)

    return f'Predicted Grade: {linear.predict([inputData])[0]:.2f}'
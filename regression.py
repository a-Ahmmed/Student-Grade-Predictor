import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

def linearRegression():
    # Read in data and trim
    data = pd.read_csv("data/student_mat_2173a47420.csv", sep=';')
    data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

    # Prediction for later (Can be changed)
    predict = "G3"

    # Define training and test data
    x = np.array(data.drop([predict], 1))
    y = np.array(data[predict])
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
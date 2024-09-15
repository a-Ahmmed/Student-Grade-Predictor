import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.utils import shuffle

def linearRegression():
    data = pd.read_csv("data/student_mat_2173a47420.csv", sep=';')
    print(data.head())
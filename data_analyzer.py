import numpy
import os
import sklearn
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor


def import_numerical_data(filename):
    if os.path.exists(filename):
        f = open(filename, "r")
        data = map(lambda arr: map(lambda str: convert_to_float(str), arr.split()), f.readlines())
        return data
    else:
        print "file does not exist"

def import_1d_data(filename):
    if os.path.exists(filename):
        f = open(filename, "r")
        data = map(lambda str: convert_to_float(str), f.readlines())
        return data
    else:
        print "file does not exist"

def convert_to_float(str):
    try:
        num = float(str)
        return num
    except ValueError:
        print "unable to parse string %s as float" % str

def regress_from_data(independent, dependent, maxlines = False):
    if maxlines:
        independent = independent[:maxlines]
        dependent = dependent[:maxlines]

    clf = linear_model.LinearRegression()
    clf.fit(independent, dependent)
    # LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False))
    return clf

def regress_and_predict_from_files(independent, dependent, num_training = False):
    independent = import_numerical_data(independent)
    dependent = import_1d_data(dependent)
    if not num_training:
        num_training = len(independent)
    clf = CLF(independent, dependent)
    clf.fit(num_training)
    return clf.predict(num_training)

class CLF:
    def __init__(self, independent, dependent):
        self.clf = linear_model.LinearRegression()
        self.independent = independent
        self.dependent = dependent

    def fit(self, maxlines):
        independent = self.independent[:maxlines]
        dependent = self.dependent[:maxlines]
        self.clf.fit(independent, dependent)

    def predict(self, start):
        return self.clf.predict(self.independent[start:])


filename1 = './MachineLearningASCIIData/LARain1901_2010.txt'
filename2 = './MachineLearningASCIIData/TBOT_Alphas.txt'
print regress_and_predict_from_files(filename2, filename1, 60)

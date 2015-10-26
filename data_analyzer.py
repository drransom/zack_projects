import os
from scipy import stats
from sklearn import linear_model
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
        data = [ convert_to_float(line.rstrip('\n')) for line in f.readlines() ]
        return data
    else:
        print "file does not exist"

def convert_to_float(str):
    try:
        num = float(str)
        return num
    except ValueError:
        print "unable to parse string %s as float" % str

class DataAnalyzer:
    def __init__(self, independent, dependent):
        self.independent = import_numerical_data(independent)
        self.dependent = import_1d_data(dependent)
        self.clf = linear_model.LinearRegression()
        self.randomForest = RandomForestRegressor()

    def fit(self, maxlines = False):
        if not maxlines:
            maxlines = len(self.dependent)
        independent = self.independent[:maxlines]
        dependent = self.dependent[:maxlines]
        self.clf.fit(independent, dependent)

    def predict(self, start, end = False):
        if end:
            return self.clf.predict(self.independent[start:(end+1)])
        else:
            return self.clf.predict(self.independent[start:])

    def correllation(self, start = 0, end = False):
        if not end:
            end = len(self.dependent)
        self.fit(end)
        predicted = self.predict(start, end)
        return stats.pearsonr(predicted, self.dependent[start:end])

    def correllation_validate(self, num_training):
        self.fit(num_training)
        predicted = self.predict(num_training)
        return stats.pearsonr(predicted, self.dependent[num_training:])

    def random_forest_fit(self):
        return self.randomForest.fit(self.independent, self.dependent)

    def random_forest_predict(self):
        self.random_forest_fit()
        return self.randomForest.predict(self.independent)


if __name__ == "__main__":
    filename1 = './MachineLearningASCIIData/LARain1901_2010.txt'
    filename2 = './MachineLearningASCIIData/TBOT_Alphas.txt'
    analyzer = DataAnalyzer(filename2, filename1)
    # analyzer.fit()
    print analyzer.random_forest_predict()

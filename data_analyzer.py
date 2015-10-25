import numpy
import os

def import_numerical_data(filename):
    if os.path.exists(filename):
        f = open(filename, "r")
        data = map(lambda arr: map(lambda str: convert_to_float(str), arr.split()), f.readlines())
        return data
    else:
        print "file does not exist"

def convert_to_float(str):
    try:
        num = float(str)
        return num
    except ValueError:
        print "unable to parse string %s as float" % str


filename = './MachineLearningASCIIData/LARain1901_2010.txt'
filename2 = './MachineLearningASCIIData/TBOT_Alphas.txt'
import_numerical_data(filename2)

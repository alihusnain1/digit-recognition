import pandas as pd
import matplotlib.pyplot as plt  
from sklearn import svm
from sklearn import metrics
import joblib
import numpy as np
from sklearn.utils import shuffle


##Step 1: Get Data from CSV
dataframe = pd.read_csv('csv/dataset.csv')
dataframe = dataframe.sample(frac=1).reset_index(drop=true)
print dataframe

##Step 2: Seperate Labels and Features
 


##Step 3: Make sure you have the correct Feature / label combination in training



##Step 4: Build a Model and Save it

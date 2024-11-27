import pandas as pd
from sklearn import HistGradientBoostClassifier as hgbc
import pickle
import joblib

model = pickle.load('best_model.pkl')

def predict(phone_number):
    result = model.predict(phone_number)
    return result
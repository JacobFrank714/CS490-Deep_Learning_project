
import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import joblib
from keras.models import load_model

# load the scaler and encdoer and transform the prediction dataframe/csv
# modified in the website file

def ProcessLiveData(data):
    min_max_scaler = joblib.load('MinMaxScaler.gz')
    one_hot_encoder = joblib.load('OneHotEncoder.joblib')
    encoder_lobby = pd.DataFrame(one_hot_encoder.transform(data[["Rank","Top_Current_Champ", "Jg_Current_Champ", "Mid_Current_Champ", "Bot_Current_Champ", "Sup_Current_Champ","Top_Enemy_Champ", "Jg_Enemy_Champ", "Mid_Enemy_Champ", "Bot_Enemy_Champ", "Sup_Enemy_Champ"]]).toarray())
    data = data.join(encoder_lobby)
    data = data.drop(["Rank","Top_Current_Champ", "Jg_Current_Champ", "Mid_Current_Champ", "Bot_Current_Champ", "Sup_Current_Champ","Top_Enemy_Champ", "Jg_Enemy_Champ", "Mid_Enemy_Champ", "Bot_Enemy_Champ", "Sup_Enemy_Champ"],axis=1)
    data["Side"] = data["Side"].astype('category')
    data["Side"] = data["Side"].cat.codes
    data = min_max_scaler.transform(data)
    return data

    
# load the model call the process data function and then use that to output a prediction

def Predict():
    model = load_model('KerasModel.h5')
    lobby =  pd.read_csv("lobby.csv")
    NewPredict = ProcessLiveData(lobby)
    return model.predict(NewPredict)[0,0]
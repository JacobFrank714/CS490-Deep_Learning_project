
import pandas as pd
import joblib
from keras.models import load_model

def ProcessLiveData(data):
    # Recieves in a pandas dataframe, processes it using a min max scaler and a one hot encoder
    min_max_scaler = joblib.load('MinMaxScaler.gz')
    one_hot_encoder = joblib.load('OneHotEncoder.joblib')
    # using one hot encoder to change the string name of the rank and the champion into features
    encoder_lobby = pd.DataFrame(one_hot_encoder.transform(data[["Rank","Top_Current_Champ", "Jg_Current_Champ", "Mid_Current_Champ", "Bot_Current_Champ", "Sup_Current_Champ","Top_Enemy_Champ", "Jg_Enemy_Champ", "Mid_Enemy_Champ", "Bot_Enemy_Champ", "Sup_Enemy_Champ"]]).toarray())
    # adding the new one hot encoded data to the original data frame
    data = data.join(encoder_lobby)
    # dropping the string name for the rank and champions
    data = data.drop(["Rank","Top_Current_Champ", "Jg_Current_Champ", "Mid_Current_Champ", "Bot_Current_Champ", "Sup_Current_Champ","Top_Enemy_Champ", "Jg_Enemy_Champ", "Mid_Enemy_Champ", "Bot_Enemy_Champ", "Sup_Enemy_Champ"],axis=1)
    data["Side"] = data["Side"].astype('category')
    data["Side"] = data["Side"].cat.codes
    # Scaling all data to be between 1 and 0
    data = min_max_scaler.transform(data)
    return data

def Predict(data):
    # load in the deep learning model that has already been trained
    model = load_model('KerasModel.h5')
    # call above processing function to process the data received from the data collection file
    NewPredict = ProcessLiveData(data)
    # returns the model's prediciton based on the data recieved from the app
    return model.predict(NewPredict)[0,0]
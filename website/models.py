from keras.models import load_model

class Prediciton():
    
    def __init__(self,df) -> None:
        self.prediction_df = df
        model = load_model('/model/Model61.h5')
        predict = model.predict(self.prediction_df)
        return predict
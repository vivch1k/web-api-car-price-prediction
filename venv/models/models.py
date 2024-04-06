import pickle
import pandas as pd


with open('venv/models/prediction_model.pkl', 'rb') as f:
    load_ml_pipeline = pickle.load(f)


def prediction(values):
    df = pd.DataFrame(data=values, 
             columns=['Year', 'Vehicle type',
                      'Drivetrain', 'Transmission',
                      'Engine HP', 'highway l/100km',
                      'city l/100km'])
    

    pred = load_ml_pipeline.predict(df)
    return pred[0]
import joblib

model = joblib.load('./model/gboost_model.joblib')
result_target = ['Dropout', 'Graduate/Enrolled']

def predictions(data):
    result = model.predict(data)
    return result_target[result[0]]
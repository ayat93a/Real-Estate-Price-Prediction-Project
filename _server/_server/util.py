import pickle
import json
import joblib

_location = None
_data_columns = None
_model = None


def load_saved_files():
    global _location , _data_columns , _model
    print('i saved them')

    # with open('AI_model/columns.json' , 'r') as f :
    #    _data_columns = json.load(f)['data_columns']
    #    _location = _data_columns[3:]

    mj = joblib.load('AI_model/model_joblib')


    # with open('AI_model/func_pickle.pickle' , 'rb') as f:
    #     _model = pickle.load(f)

def get_location_names():
    return _location


if __name__ == '__main__':
    load_saved_files()
    print(get_location_names())
    
    
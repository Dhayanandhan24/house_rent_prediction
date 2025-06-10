# load ML model : pickle
# import pickle

# with open('modelPickle', 'rb') as modelku:
#     modelLoad = pickle.load(modelku)

import joblib
modelLoad = joblib.load('modelJoblib')

print(modelLoad.predict([[
    4.240700, 40, 5.694362, 1.032641, 1851, 2.746291,
    34.16, -117.99
]])[0])


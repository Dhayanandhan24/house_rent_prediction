import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing

# load sklearn dataset
dataCH = fetch_california_housing()
dfCH = pd.DataFrame(
    dataCH.data,
    columns = dataCH['feature_names']
)
dfCH['PRICE'] = dataCH.target

# split datasets: 90% training + 10% testing
x = dfCH[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 
    'Population', 'AveOccup', 'Latitude', 'Longitude' ]]
y = dfCH['PRICE']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .02)

# linear reg model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)

print(model.predict([[
    4.240700, 40, 5.694362, 1.032641, 1851, 2.746291,
    34.16, -117.99
]]))

# save model ML: pickle
# import pickle
# with open('modelPickle.pkl', 'wb') as modelku:
#     pickle.dump(model, modelku)

# save model : joblib
# pip install joblib
import joblib
joblib.dump(model, 'modelJoblib')

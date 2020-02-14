
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import sys

#get_ipython().run_line_magic('matplotlib', 'inline')

data = pd.read_csv(sys.argv[1])
X = data.drop(sys.argv[3], axis=1)
y = data[sys.argv[3]]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# One Hot Encoder: Encode categorical features as a one-hot numeric array
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse=False)

X_train_ohe = ohe.fit_transform(X_train)
X_test_ohe = ohe.transform(X_test)

from sklearn.linear_model import LinearRegression

lr = LinearRegression().fit(X_train_ohe, y_train)

print('Training Score:',lr.score(X_train_ohe, y_train))

print('Test Score:',lr.score(X_test_ohe, y_test))

from sklearn.metrics import mean_squared_error
y_pred = lr.predict(X_test_ohe)
print('Mean Squared Error:',mean_squared_error(y_test, y_pred))

# save the model to disk
filename = sys.argv[2]
pickle.dump(lr, open(filename, 'wb'))

# save the One Hot Encoder to disk
filename_2 = sys.argv[4]
pickle.dump(ohe, open(filename_2, 'wb'))



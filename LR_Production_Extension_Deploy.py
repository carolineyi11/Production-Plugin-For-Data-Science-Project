#!/usr/bin/env python
# coding: utf-8



# In[21]:


# load the model from disk
#filename = 'C:\Desktop\ODSC\\finalized_model.sav'



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import sys

loaded_model = pickle.load(open(sys.argv[2], 'rb'))

preprocessor = pickle.load(open(sys.argv[4], 'rb'))

data_new = pd.read_csv(sys.argv[1])
X_new = data_new.drop(sys.argv[3], axis=1)
y_new = data_new[sys.argv[3]]

X_ohe = preprocessor.fit_transform(X_new)

y_new_pred = loaded_model.predict(X_ohe)


X_new['Prediction']=y_new_pred

X_new.to_csv(sys.argv[5])

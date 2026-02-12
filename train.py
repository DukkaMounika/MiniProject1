import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
import os

# 1. Create dummy data (Bedrooms, Bathrooms, Sqft, Floors)
X = np.array([[1, 1, 500, 1], [2, 1, 1000, 1], [3, 2, 1500, 2], [4, 3, 2500, 2]])
y = np.array([100000, 200000, 300000, 500000])

# 2. Train the model
model = LinearRegression()
model.fit(X, y)

# 3. Create the folder if it doesn't exist
if not os.path.exists('model'):
    os.makedirs('model')

# 4. Save the model to the path your app expects
pickle.dump(model, open("model/linear_model.pkl", "wb"))
print("Model saved successfully!")
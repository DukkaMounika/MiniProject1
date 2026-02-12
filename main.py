from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model/linear_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

# API Endpoint
@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    bedrooms = float(data['bedrooms'])
    bathrooms = float(data['bathrooms'])
    sqft = float(data['sqft'])
    floors = float(data['floors'])

    features = np.array([[bedrooms, bathrooms, sqft, floors]])

    prediction = model.predict(features)[0]

    return jsonify({
        "predicted_price": round(prediction, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)

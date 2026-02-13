from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


# Load your manual model (if you saved it as a pickle)
# model = pickle.load(open('model/linear_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', prediction_text="Waiting...")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        sqft = float(request.form['sqft_living'])

        # USE YOUR MANUAL MATH HERE: y = m*x + c
        # Example calculation:
        m = 280.5  # Your calculated slope
        c = 15000  # Your calculated C-value
        price = (m * sqft) + c

        return render_template('index.html',
                               prediction_text=f"₹ {price:,.2f}")
    except Exception as e:
        return render_template('index.html', prediction_text="Error in Input")


if __name__ == "__main__":
    app.run(debug=True)
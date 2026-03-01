from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import os
app = Flask(__name__)

model = pickle.load(open("house_price_model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    input_data = pd.DataFrame(
        [
            {
                "location": data["location"],
                "total_sqft": float(data["sqft"]),
                "bath": float(data["bath"]),
                "BHK": int(data["bhk"]),
            }
        ]
    )

    prediction = model.predict(input_data)[0]

    return jsonify({"price": round(prediction, 2)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)

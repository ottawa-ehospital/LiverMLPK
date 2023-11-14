from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS extension
import pickle

app = Flask(__name__)
CORS(app) # enable CORS for the entire app

#load the pretrained model
model = pickle.load(open("liver_prediction_model_1.0.pkl", "rb"))
@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        values = [data["Age"], data["Total_Bilirubin"], data["Direct_Bilirubin"], data["Alkaline_Phosphotase"], data["Alamine_Aminotransferase"], data["Aspartate_Aminotransferase"], data["Total_Protiens"], data["Albumin"], data["Albumin_and_Globulin_Ratio"], data["Gender_Female"], data["Gender_Male"]]
        print(values)
        prediction = model.predict([values])
        print("prediction: ", prediction)
        #values = []
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(debug=True)
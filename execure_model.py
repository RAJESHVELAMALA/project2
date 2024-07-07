# %%
#!pip install flask
#!pip install flask_cors
# %%


# %%
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the trained Naive Bayes model
with open('naive_bayes_model_v2.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return "Naive Bayes Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    print(data)

    required_keys = ['Age', 'Gender', 'itching', 'skin_rash', 'nodal_skin_eruptions',
       'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
       'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
       'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue',
       'weight_gain', 'anxiety', 'cold_hands_and_feets']
    
   # if not all(key in data for key in required_keys):
        #return jsonify({'error': 'Missing data'}), 400
    
   # Convert data to numpy array for prediction
    target_names = [
        '(vertigo) Paroymsal Positional Vertigo', 'AIDS', 'Acne', 'Alcoholic hepatitis',
        'Allergy', 'Arthritis', 'Bronchial Asthma', 'Celiac', 'Cervical spondylosis',
        'Chicken pox', 'Chronic cholestasis', 'Common Cold', 'Dengue', 'Diabetes ',
        'Dimorphic hemmorhoids(piles)', 'Drug Reaction', 'Fungal infection', 'GERD',
        'Gastroenteritis', 'Heart attack', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D',
        'Hepatitis E', 'Hypertension ', 'Hyperthyroidism', 'Hypoglycemia', 'Hypothyroidism',
        'Impetigo', 'Jaundice', 'Malaria', 'Migraine', 'Monkey Pox', 'No disease identified',
        'Osteoarthristis', 'Paralysis (brain hemorrhage)', 'Peptic ulcer diseae',
        'Pneumonia', 'Psoriasis', 'Tuberculosis', 'Typhoid', 'Urinary tract infection',
        'Varicose veins', 'hepatitis A'
    ]

    # Convert target_names to a numpy array
    target_names_np = np.array(target_names)

    features = np.array([[data['Age'], data['Gender'], data['itching'], data['skin_rash'],
                          data['nodal_skin_eruptions'], data['continuous_sneezing'], data['shivering'], 
                          data['chills'], data['joint_pain'], data['stomach_pain'], data['acidity'], 
                          data['ulcers_on_tongue'], data['muscle_wasting'], data['vomiting'], 
                          data['burning_micturition'], data['spotting_urination'], data['fatigue'], 
                          data['weight_gain'], data['anxiety'], data['cold_hands_and_feets']]])


    prediction = model.predict(features)
    print(prediction)
    prediction_proba = model.predict_proba(features)
    predicted_class = target_names[prediction[0]]
        

    return jsonify({
        'prediction': predicted_class,
        'probabilities': {target_names[i]: prob for i, prob in enumerate(prediction_proba[0])}
    })

if __name__ == '__main__':
    app.run(debug=True)


# %%




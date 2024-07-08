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

  #  required_keys = ['Age', 'Gender', 'itching', 'skin_rash', 'nodal_skin_eruptions',
  #     'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
  #     'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
  #     'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue',
  #     'weight_gain', 'anxiety', 'cold_hands_and_feets']
    
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

    features = np.array([[data['Age'],data['Gender'],data['itching'],data['skin_rash'],data['nodal_skin_eruptions'],data['continuous_sneezing'],data['shivering'],data['chills'],data['joint_pain'],data['stomach_pain'],data['acidity'],data['ulcers_on_tongue'],data['muscle_wasting'],data['vomiting'],data['burning_micturition'],data['spotting_urination'],data['fatigue'],data['weight_gain'],data['anxiety'],data['cold_hands_and_feets'],data['mood_swings'],data['weight_loss'],data['restlessness'],data['lethargy'],data['patches_in_throat'],data['irregular_sugar_level'],data['cough'],data['high_fever'],data['sunken_eyes'],data['breathlessness'],data['sweating'],data['dehydration'],data['indigestion'],data['headache'],data['yellowish_skin'],data['dark_urine'],data['nausea'],data['loss_of_appetite'],data['pain_behind_the_eyes'],data['back_pain'],data['constipation'],data['mild_fever'],data['yellow_urine'],data['yellowing_of_eyes'],data['acute_liver_failure'],data['fluid_overload'],data['swelling_of_stomach'],data['swelled_lymph_nodes'],data['malaise'],data['blurred_and_distorted_vision'],data['phlegm'],data['throat_irritation'],data['redness_of_eyes'],data['sinus_pressure'],data['runny_nose'],data['congestion'],data['chest_pain'],data['weakness_in_limbs'],data['fast_heart_rate'],data['pain_during_bowel_movements'],data['pain_in_anal_region'],data['bloody_stool'],data['irritation_in_anus'],data['neck_pain'],data['dizziness'],data['cramps'],data['bruising'],data['obesity'],data['swollen_legs'],data['swollen_blood_vessels'],data['puffy_face_and_eyes'],data['enlarged_thyroid'],data['brittle_nails'],data['swollen_extremeties'],data['excessive_hunger'],data['extra_marital_contacts'],data['drying_and_tingling_lips'],data['slurred_speech'],data['knee_pain'],data['hip_joint_pain'],data['muscle_weakness'],data['stiff_neck'],data['swelling_joints'],data['movement_stiffness'],data['spinning_movements'],data['loss_of_balance'],data['unsteadiness'],data['weakness_of_one_body_side'],data['loss_of_smell'],data['bladder_discomfort'],data['foul_smell_of_urine'],data['continuous_feel_of_urine'],data['passage_of_gases'],data['internal_itching'],data['toxic_look_(typhos)'],data['depression'],data['irritability'],data['muscle_pain'],data['altered_sensorium'],data['red_spots_over_body'],data['belly_pain'],data['abnormal_menstruation'],data['dischromic_patches'],data['watering_from_eyes'],data['increased_appetite'],data['polyuria'],data['family_history'],data['mucoid_sputum'],data['rusty_sputum'],data['lack_of_concentration'],data['visual_disturbances'],data['receiving_blood_transfusion'],data['receiving_unsterile_injections'],data['coma'],data['stomach_bleeding'],data['distention_of_abdomen'],data['history_of_alcohol_consumption'],data['fluid_overload.1'],data['blood_in_sputum'],data['prominent_veins_on_calf'],data['palpitations'],data['painful_walking'],data['pus_filled_pimples'],data['blackheads'],data['scurrying'],data['skin_peeling'],data['silver_like_dusting'],data['small_dents_in_nails'],data['inflammatory_nails'],data['blister'],data['red_sore_around_nose'],data['yellow_crust_ooze'],data['Diabetes'],data['Diabetes Type'],data['Diarrhoea'],data['Abdominal'],data['Sticky_Stool'],data['Weight_loss'],data['Marsh'],data['Rectal Pain'],data['Sore Throat'],data['Penile Oedema'],data['Oral Lesions'],data['Solitary Lesion'],data['Swollen Tonsils'],data['HIV Infection'],data['Sexually Transmitted Infection'],data['Fever'],data['Swollen_Lymph_Nodes'],data['Muscle_Aches'],data['PSS'],data['Variant'],data['DSS']]])


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




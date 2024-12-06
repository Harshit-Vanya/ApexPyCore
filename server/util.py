from flask import Flask, render_template, request, jsonify
import json
import pickle
import numpy as np
import pandas as pd
import requests
from flask_cors import CORS

app = Flask(__name__)

__model = None
__symptoms = None

with open('symptoms.json') as f:
    data = json.load(f)
    __symptoms = data['symptoms']

@app.route('/')
def index():
    return render_template('index.html', symptoms=__symptoms)

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '').lower()
    filtered_symptoms = [symptom for symptom in __symptoms if symptom.lower().startswith(query)]
    return jsonify(filtered_symptoms)

def load_artifacts():
    global __model
    try:
        with open('artifacts/Disease_identifier', 'rb') as m:
            __model = pickle.load(m)
        if __model is None:
            raise Exception("Model loaded as None")
        print("Model loaded successfully")
    except Exception as e:
        print(f"Critical error loading model: {e}")
        raise

@app.before_request
def initialize_once():
    global __model
    if __model is None:
        try:
            load_artifacts()
        except Exception as e:
            return jsonify({'error': 'Model initialization failed'}), 500

def get_disease_id(selected_symptoms):
    x = pd.DataFrame(np.zeros((1, len(__symptoms))), columns=__symptoms)
    for symptom in selected_symptoms:
        if symptom in __symptoms:
            x[symptom] = 1
    prediction = __model.predict(x)
    return prediction[0]

@app.route('/submit_symptoms', methods=['POST'])
def submit_symptoms():
    data = request.get_json()
    selected_symptoms = data.get('symptoms', [])
    
    if not selected_symptoms:
        return jsonify({'error': 'No symptoms provided'}), 400
    
    try:
        disease_id = int(get_disease_id(selected_symptoms))
        df_check = pd.read_csv('artifacts/id_wise.csv')
        disease_row = df_check.loc[df_check['Disease_no'] == disease_id, 'diseases']
        
        if not disease_row.empty:
            disease = disease_row.values[0]
            return jsonify({
                'disease': disease,
                'message': 'Prediction successful'
            })
        else:
            return jsonify({'error': 'Disease not found'}), 404
            
    except Exception as e:
        print(f"Error in submit_symptoms: {str(e)}")
        return jsonify({'error': f'Error processing request: {str(e)}'}), 500

CORS(app)

NEWS_API_KEY = 'd8c07d61de1c4cec8b30bcd9175fd65c'

def get_fallback_news():
    return {
        'articles': [
            {
                'title': 'Regular Exercise Boosts Immune System',
                'description': 'New research shows that regular physical activity can significantly improve immune function and reduce the risk of various diseases.',
                'urlToImage': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?ixlib=rb-4.0.9',
            },
            {
                'title': 'Importance of Mental Health Awareness',
                'description': 'Healthcare professionals emphasize the growing need for mental health awareness and early intervention strategies.',
                'urlToImage': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?ixlib=rb-4.0.9',
            },
            {
                'title': 'Balanced Diet and Health Benefits',
                'description': 'Studies confirm that maintaining a balanced diet rich in nutrients can prevent various health conditions and improve overall wellbeing.',
                'urlToImage': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?ixlib=rb-4.0.9',
            }
        ]
    }

@app.route('/get-news', methods=['GET'])
def get_news():
    try:
        news_api_url = 'https://newsapi.org/v2/top-headlines'
        params = {
            'country': 'us',
            'category': 'health',
            'apiKey': NEWS_API_KEY
        }
        response = requests.get(news_api_url, params=params, timeout=5)
        
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            # Return fallback news if API fails
            return jsonify(get_fallback_news())
            
    except Exception as e:
        print(f"News API Error: {str(e)}")
        # Return fallback news on any error
        return jsonify(get_fallback_news())

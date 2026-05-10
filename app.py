from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the model
MODEL_PATH = 'system_health_model.pkl'

def predict_status(cpu, memory, disk, db_load):
    if not os.path.exists(MODEL_PATH):
        return "Model not found", "error"
    
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
        
    features = np.array([[cpu, memory, disk, db_load]])
    prediction = model.predict(features)[0]
    
    # 0: Healthy, 1: Warning, 2: Critical
    status_map = {
        0: ("Healthy System", "healthy"),
        1: ("Warning Condition", "warning"),
        2: ("Critical Condition", "critical")
    }
    
    return status_map.get(prediction, ("Unknown", "error"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/objectives')
def objectives():
    return render_template('objectives.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        cpu = float(request.form['cpu'])
        memory = float(request.form['memory'])
        disk = float(request.form['disk'])
        db_load = float(request.form['db_load'])
        
        status_text, status_class = predict_status(cpu, memory, disk, db_load)
        
        return render_template('result.html', 
                               status_text=status_text, 
                               status_class=status_class,
                               cpu=cpu, memory=memory, disk=disk, db_load=db_load)
    except Exception as e:
        return render_template('result.html', status_text=f"Error: {str(e)}", status_class="error")

if __name__ == '__main__':
    app.run(debug=True, port=8080)

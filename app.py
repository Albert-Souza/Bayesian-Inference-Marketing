from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()
    
    visits_A = int(data['visits_A'])
    conversions_A = int(data['conversions_A'])
    visits_B = int(data['visits_B'])
    conversions_B = int(data['conversions_B'])
    
    samples_A = np.random.beta(conversions_A + 1, visits_A - conversions_A + 1, 100000)
    samples_B = np.random.beta(conversions_B + 1, visits_B - conversions_B + 1, 100000)
    
    prob_B_best = np.mean(samples_B > samples_A) * 100
    
    return jsonify({'probabilidade': f"{prob_B_best:.2f}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Set your DeepInfra API key
API_KEY = '********'
BASE_URL = 'https://api.deepinfra.com/v1/openai/chat/completions'

# Function to get a response from the chatbot
def get_chatbot_response(user_input):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "model": "mistralai/Mistral-7B-Instruct-v0.3",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }
    
    response = requests.post(BASE_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_chatbot_response(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)

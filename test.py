import requests

# Set your DeepInfra API key
API_KEY = 'aanNnBnBwStL8i0CNQuS1SG6JRYUr4s8'
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
    
    if response.status_code == 20:
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Main function to interact with the chatbot
def main():
    print("Welcome to the DeepInfra Chatbot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = get_chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
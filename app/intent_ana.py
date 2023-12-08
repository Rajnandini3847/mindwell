import json
import pandas as pd
import joblib

def predict_intent(user_input):
    # Load the saved vectorizer
    vectorizer = joblib.load('/Users/pranaymishra/Desktop/backend_mindwell/backend/app/models/intent_vectorizer.joblib')

    # Vectorize the user input
    user_input_vec = vectorizer.transform([user_input])

    # Load the saved model
    model = joblib.load('/Users/pranaymishra/Desktop/backend_mindwell/backend/app/models/intent_classifier_model.joblib')

    # Predict the intent
    intent = model.predict(user_input_vec)[0]

    return intent

# Function to generate responses based on predicted intents
def generate_response(intent):
    # Implement your logic here to generate appropriate responses based on the predicted intents
    if intent == 'greeting':
        response = "Hello! How can I assist you today?"
    elif intent == 'farewell':
        response = "Goodbye! Take care."
    elif intent == 'question':
        response = "I'm sorry, I don't have the information you're looking for."
    else:
        response = "I'm here to help. Please let me know how I can assist you."

    return response

def main_function(user_input):
    intent = predict_intent(user_input)
    print(f"Intent for '{user_input}': {intent}")
    print(f"Response: {generate_response(intent)}")
    return intent

def main_response(user_input):
    intent = predict_intent(user_input)
    response = generate_response(intent)
    return response
# Example usage
# main_function("i am not feeling well")

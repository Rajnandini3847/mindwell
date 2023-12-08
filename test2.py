import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import joblib

# Load intents data
with open('/Users/pranaymishra/Desktop/backend_mindwell/backend/app/intents.json', 'r') as f:
    data = json.load(f)

# Preprocess data
dic = {"tag":[], "patterns":[], "responses":[]}
for i in range(len(data['intents'])):
    ptrns = data['intents'][i]['patterns']
    rspns = data['intents'][i]['resonses']
    tag = data['intents'][i]['tag']
    for j in range(len(ptrns)):
        dic['tag'].append(tag)
        dic['patterns'].append(ptrns[j])
        dic['responses'].append(rspns)

df = pd.DataFrame.from_dict(dic)

# Train-test split
X = df['patterns']
y = df['tag']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Train a Support Vector Machine (SVM) classifier
model = SVC()
model.fit(X_train_vec, y_train)

# Save the model and vectorizer
joblib.dump(model, 'intent_classifier_model.joblib')
joblib.dump(vectorizer, 'intent_vectorizer.joblib')

# Function to predict intent using the saved model
def predict_intent(user_input):
    # Load the saved vectorizer
    vectorizer = joblib.load('intent_vectorizer.joblib')

    # Vectorize the user input
    user_input_vec = vectorizer.transform([user_input])

    # Load the saved model
    model = joblib.load('intent_classifier_model.joblib')

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

# Function to call the main process
def main_function(user_input):
    intent = predict_intent(user_input)
    print(f"Intent for '{user_input}': {intent}")
    print(f"Response: {generate_response(intent)}")

# Example usage
main_function("i am not feeling well")

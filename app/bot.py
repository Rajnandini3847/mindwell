import json
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Embedding, LSTM, LayerNormalization, Dense, Dropout
import re
import random

def load_data(file_path='/Users/pranaymishra/Desktop/backend_mindwell/backend/app/intents.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data['intents'])

def preprocess_data(df):
    dic = {"tag": [], "patterns": [], "responses": []}
    for i in range(len(df)):
        ptrns = df[df.index == i]['patterns'].values[0]
        rspns = df[df.index == i]['resonses'].values[0]
        tag = df[df.index == i]['tag'].values[0]
        for j in range(len(ptrns)):
            dic['tag'].append(tag)
            dic['patterns'].append(ptrns[j])
            dic['responses'].append(rspns)

    processed_df = pd.DataFrame.from_dict(dic)
    return processed_df

def create_model(X, y, vocab_size):
    model = Sequential()
    model.add(Input(shape=(X.shape[1])))
    model.add(Embedding(input_dim=vocab_size + 1, output_dim=100, mask_zero=True))
    model.add(LSTM(32, return_sequences=True))
    model.add(LayerNormalization())
    model.add(LSTM(32, return_sequences=True))
    model.add(LayerNormalization())
    model.add(LSTM(32))
    model.add(LayerNormalization())
    model.add(Dense(128, activation="relu"))
    model.add(LayerNormalization())
    model.add(Dropout(0.2))
    model.add(Dense(128, activation="relu"))
    model.add(LayerNormalization())
    model.add(Dropout(0.2))
    model.add(Dense(len(np.unique(y)), activation="softmax"))
    model.compile(optimizer='adam', loss="sparse_categorical_crossentropy", metrics=['accuracy'])
    return model

def train_model(model, X, y, callbacks=None, epochs=6, batch_size=10):
    return model.fit(x=X,
                     y=y,
                     batch_size=batch_size,
                     callbacks=callbacks,
                     epochs=epochs)

def generate_answer(model, tokenizer, lbl_enc, df, pattern):
    text = []
    txt = re.sub('[^a-zA-Z\']', ' ', pattern)
    txt = txt.lower()
    txt = txt.split()
    txt = " ".join(txt)
    text.append(txt)

    x_test = tokenizer.texts_to_sequences(text)
    x_test = np.array(x_test).squeeze()
    x_test = pad_sequences([x_test], padding='post', maxlen=X.shape[1])
    y_pred = model.predict(x_test)
    y_pred = y_pred.argmax()
    tag = lbl_enc.inverse_transform([y_pred])[0]
    responses = df[df['tag'] == tag]['responses'].values[0]

    print("you: {}".format(pattern))
    print("model: {}".format(random.choice(responses)))
    
def generate_answer(model, tokenizer, lbl_enc, df, X, pattern):
    text = []
    txt = re.sub('[^a-zA-Z\']', ' ', pattern)
    txt = txt.lower()
    txt = txt.split()
    txt = " ".join(txt)
    text.append(txt)

    x_test = tokenizer.texts_to_sequences(text)
    x_test = np.array(x_test).squeeze()
    x_test = pad_sequences([x_test], padding='post', maxlen=X.shape[1])
    y_pred = model.predict(x_test)
    y_pred = y_pred.argmax()
    tag = lbl_enc.inverse_transform([y_pred])[0]
    responses = df[df['tag'] == tag]['responses'].values[0]

    print("you: {}".format(pattern))
    print("model: {}".format(random.choice(responses)))


# Example usage:
generate_answer(model, tokenizer, lbl_enc, processed_df, X, "Hi! How are you?")

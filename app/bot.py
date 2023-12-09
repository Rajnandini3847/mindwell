# import json
# import pandas as pd
# import numpy as np
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from sklearn.preprocessing import LabelEncoder
# from tensorflow import keras
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Input, Embedding, LSTM, LayerNormalization, Dense, Dropout
# import re
# import random

# def load_data(file_path='/Users/pranaymishra/Desktop/backend_mindwell/backend/app/intents.json'):
#     with open(file_path, 'r') as f:
#         data = json.load(f)
#     return pd.DataFrame(data['intents'])

# def preprocess_data(df):
#     dic = {"tag": [], "patterns": [], "responses": []}
#     for i in range(len(df)):
#         ptrns = df[df.index == i]['patterns'].values[0]
#         rspns = df[df.index == i]['resonses'].values[0]
#         tag = df[df.index == i]['tag'].values[0]
#         for j in range(len(ptrns)):
#             dic['tag'].append(tag)
#             dic['patterns'].append(ptrns[j])
#             dic['responses'].append(rspns)

#     processed_df = pd.DataFrame.from_dict(dic)
#     return processed_df

# def create_model(X, y, vocab_size):
#     model = Sequential()
#     model.add(Input(shape=(X.shape[1])))
#     model.add(Embedding(input_dim=vocab_size + 1, output_dim=100, mask_zero=True))
#     model.add(LSTM(32, return_sequences=True))
#     model.add(LayerNormalization())
#     model.add(LSTM(32, return_sequences=True))
#     model.add(LayerNormalization())
#     model.add(LSTM(32))
#     model.add(LayerNormalization())
#     model.add(Dense(128, activation="relu"))
#     model.add(LayerNormalization())
#     model.add(Dropout(0.2))
#     model.add(Dense(128, activation="relu"))
#     model.add(LayerNormalization())
#     model.add(Dropout(0.2))
#     model.add(Dense(len(np.unique(y)), activation="softmax"))
#     model.compile(optimizer='adam', loss="sparse_categorical_crossentropy", metrics=['accuracy'])
#     return model

# def train_model(model, X, y, callbacks=None, epochs=3, batch_size=5):
#     return model.fit(x=X,
#                      y=y,
#                      batch_size=batch_size,
#                      callbacks=callbacks,
#                      epochs=epochs)

# def generate_answer(model, tokenizer, lbl_enc, df, X, pattern):
#     text = []
#     txt = re.sub('[^a-zA-Z\']', ' ', pattern)
#     txt = txt.lower()
#     txt = txt.split()
#     txt = " ".join(txt)
#     text.append(txt)

#     x_test = tokenizer.texts_to_sequences(text)
#     x_test = np.array(x_test).squeeze()
#     x_test = pad_sequences([x_test], padding='post', maxlen=X.shape[1])
#     y_pred = model.predict(x_test)
#     y_pred = y_pred.argmax()
#     tag = lbl_enc.inverse_transform([y_pred])[0]
#     responses = df[df['tag'] == tag]['responses'].values[0]

#     you = "you: {}".format(pattern)
#     model = "model: {}".format(random.choice(responses))
#     return you, model

# # Example usage:
# def call_bot(input):
#     data_df = load_data()
#     processed_df = preprocess_data(data_df)
#     tokenizer = Tokenizer(lower=True, split=' ')
#     tokenizer.fit_on_texts(processed_df['patterns'])
#     vocab_size = len(tokenizer.word_index)
#     ptrn2seq = tokenizer.texts_to_sequences(processed_df['patterns'])
#     X = pad_sequences(ptrn2seq, padding='post')
#     lbl_enc = LabelEncoder()
#     y = lbl_enc.fit_transform(processed_df['tag'])
#     model = create_model(X, y, vocab_size)
#     train_model(model, X, y)
#     you , model = generate_answer(model, tokenizer, lbl_enc, processed_df, X, input)
#     print(you)
#     print(model)
#     return model
    
# # call_bot("i am sad, i just broke up with my girlfriend")
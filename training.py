import pandas as pd
import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Dense
from tensorflow.keras import Sequential
from sklearn.preprocessing import LabelEncoder
import os

def retraining():
    
    df = pd.read_csv('filos.csv')
    num_filos = df.shape[0]

    model = Sequential()
    model.add(Dense(23, activation='tanh'))
    model.add(Dense(num_filos, activation='softmax'))
    model.compile(loss=tf.keras.metrics.sparse_categorical_crossentropy,
                optimizer=tf.keras.optimizers.SGD(1.), metrics=['accuracy'])

    x_df = df.drop(['Phylum','descripcion'], axis=1)
    y_df = df.Phylum

    X = x_df.to_numpy()
    y = y_df.to_numpy()

    label_encoder = LabelEncoder()
    label_encoder.classes_ = np.array([i for i in y])
    y_encoded = label_encoder.transform(y) 

    _= model.fit(X,y_encoded, epochs=50)
    
    model.save("modelo.keras")
    #os.chmod("modelo.keras", 0o666)
    
    return model.evaluate(X,  y_encoded, verbose=2)
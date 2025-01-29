from tensorflow.keras.models import load_model
import numpy as np


def model_answer(input):
    question = np.array(input)
    question = question.reshape(1, -1)
    model = load_model('modelo.keras')

    pred = np.argmax(model.predict(question))
    return pred


def user_friendly_answer(array):
    
    ans = model_answer(array)

    filos = {
        0: 'chordata',
        1: 'echinodermata',
        2: 'arthropoda',
        3: 'annelida',
        4: 'molusca',
        5: 'rotifera',
        6: 'nematoda',
        7: 'nemertea',
        8: 'platyhelmithes',
        9: 'ctenophera',
        10: 'cnidaria',
        11: 'polifera',
        12: 'protozooarios'
    }

    return filos[ans]


if __name__ == '__main__':
    print(user_friendly_answer([1, 1, 1, 0, 1, 0, 1, 1, 0, 1,
          0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]))

from tensorflow.keras.models import load_model
import numpy as np
from data_acces import get_filos


def model_answer(input):
    question = np.array(input)
    question = question.reshape(1, -1)

    model = load_model('model/modelo.keras')
    pred = np.argmax(model.predict(question))

    return pred


def user_friendly_answer(array):
    ans = model_answer(array)
    filos = get_filos()

    return filos[ans]


def editar_filo():
    pass


def eliminar_filo():
    pass


def agregar_filo():
    pass


if __name__ == '__main__':
    chordata = [1, 1, 1, 0, 1, 0, 1, 1, 0, 1,
                0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]
    protozoa = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    print(user_friendly_answer(protozoa))
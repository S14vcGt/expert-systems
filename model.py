from tensorflow.keras.models import load_model
import numpy as np
import data_acces as da


def model_answer(input):
    question = np.array(input)
    question = question.reshape(1, -1)

    model = load_model('modelo.keras')
    pred = np.argmax(model.predict(question))

    return pred


def user_friendly_answer(array):
    ans = model_answer(array)
    filos = da.get_filos()
    descriptions = da.get_filos_description()

    return {"filo": filos[ans], "descripcion": descriptions[ans]}


def find_all():
    pass


def agregar_filo(raw_new_filo):

    new_filo = {}

    da.add_filo()


def editar_filo():
    pass


def eliminar_filo():
    pass


if __name__ == '__main__':
    chordata = [1, 1, 1, 0, 1, 0, 1, 1, 0, 1,
                0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]
    protozoa = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    print(user_friendly_answer(protozoa))

from tensorflow.keras.models import load_model
import numpy as np
import data_acces as da
from support_data import diccionario_de_referencia


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
    return da.find_all_filos()


def agregar_filo(raw_new_filo):

    carac: list = raw_new_filo['caracteristicas']
    name_filo = raw_new_filo['filo']
    desc_filo = raw_new_filo['descripcion']

    new_filo = diccionario_de_referencia.copy()
    new_filo['Phylum'] = name_filo
    new_filo['descripcion'] = desc_filo
    
    keys = list(new_filo.keys())
    keys = keys[2:]
    i = 0
    for attribute in keys:
        new_filo[attribute] = carac[i]
        i+=1


    da.add_filo(new_filo )

    return {'message':'filo agregado con exito'}


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

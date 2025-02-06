from tensorflow.keras.models import load_model
import numpy as np
import uuid
import data_acces as da
from support_data import diccionario_de_referencia
from training import retraining


def model_answer(input):
    question = np.array(input)
    question = question.reshape(1, -1)

    model = load_model('modelo.keras')
    pred = model.predict(question)
    filo = np.argmax(pred)
    pred2 = pred.tolist()

    return (filo, pred2[0][filo])


def user_friendly_answer(array):
    ans = model_answer(array)
    if ans[1] > .9:
        filos = da.get_filos()
        return filos[ans[0]]
    else:
        return {"Phylum": "desconocido",
                "descripcion": "El filo que se describio no esta dentro de la base de conocimiento de este sistema"}


def find_all():
    filos = da.get_filos()
    # Agregar la propiedad 'id' a cada registro
    for index_registro, registro in filos.items():
        registro['id'] = uuid.uuid4()  # Generamos un UUID

    return filos


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
        i += 1

    da.add_filo(new_filo)

    loss, accuracy = retraining()
    return {'message': f'filo agregado con exito, el modelo se reentreno con una precision de {accuracy}, y una perdida de {loss}'}


'''def editar_filo():
    pass
'''


def eliminar_filo(index):

    da.delete_filo(index)

    loss, accuracy = retraining()
    return {'message': f'filo eliminado con exito, el modelo se reentreno con una precision de {accuracy}, y una perdida de {loss}'}


if __name__ == '__main__':
    chordata = [1, 1, 1, 0, 1, 0, 1, 1, 0, 1,
                0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]
    protozoa = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    print(user_friendly_answer(protozoa))

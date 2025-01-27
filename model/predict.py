import numpy as np
from model import model
from preprocessing import X_test, label_encoder
import pandas as pd

# Nuevo organismo
nuevo_organismo = {
    "nivel_organizacion": "organos",
        "simetria": "bilateral",
        "capas_germinales": "triploblastico",
        "cavidad_corporal": "celomado",
        "segmentacion": "segmentado",
        "sistema_digestivo": "completo",
        "sistema_nervioso": "ganglionar",
        "sistema_corporal": "exoesqueleto",
        "reproduccion": "sexual",
        "habitat": "acuatico o terrestre",
}

# Crear DataFrame con la misma estructura que X_test
nuevo_organismo_df = pd.DataFrame([nuevo_organismo])
nuevo_organismo_encoded = pd.get_dummies(nuevo_organismo_df)

# Verificar de que tenga las mismas columnas que X_test
nuevo_organismo_encoded = nuevo_organismo_encoded.reindex(columns=X_test.columns, fill_value=0)

# Convierte a float32
nuevo_organismo_encoded = nuevo_organismo_encoded.astype(np.float32)

# Realiza la predicción
prediccion = model.predict(nuevo_organismo_encoded)

# Decodifica la predicción
phylum_predicho = label_encoder.inverse_transform([np.argmax(prediccion)])
print(f"El organismo pertenece al phylum: {phylum_predicho[0]}")

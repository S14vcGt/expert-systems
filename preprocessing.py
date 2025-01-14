from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from data import df, labels
import pandas as pd

# Codificación de etiquetas
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(labels)

# Codificación de características (OneHotEncoder para texto)
X_encoded = pd.get_dummies(df)

# División de datos
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.2, random_state=42)

# Exportar datos preprocesados
__all__ = ["X_train", "X_test", "y_train", "y_test", "label_encoder"]

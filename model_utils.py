import numpy as np


def predict_rul(model, input_data):
    # Assurez-vous que les données d'entrée sont sous forme de tableau numpy
    input_data = np.array(input_data)

    # Si le modèle attend 8 caractéristiques, mais qu'on a 3, ajoute des valeurs par défaut (par exemple, 0.0) pour les autres caractéristiques
    if len(input_data) < 8:
        input_data = np.pad(input_data, (0, 8 - len(input_data)), 'constant', constant_values=0.0)

    # Redimensionner les données pour correspondre à la forme attendue : (1, 1, 8)
    input_data = input_data.reshape((1, 1, 8))

    # Prédire avec le modèle
    prediction = model.predict(input_data)

    return prediction[0][0]  # Renvoie la prédiction

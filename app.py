import streamlit as st

st.title("Prédiction du Remaining Useful Life (RUL)")

# Entrée utilisateur
st.write("Veuillez entrer les valeurs pour effectuer une prédiction :")

# Valeurs initiales fixes ou vides
temp = st.number_input("Température (°C)", min_value=0.0, max_value=150.0, value=0.0)
vibrations = st.number_input("Vibrations", min_value=0.0, max_value=100.0, value=0.0)
force = st.number_input("Force", min_value=0.0, max_value=50.0, value=0.0)

# Afficher le résultat
if st.button("Prédire"):
    # Simuler un résultat (ou utiliser votre modèle de prédiction)
    rul = 150  # Exemple de valeur fixe simulée
    st.success(f"Le Remaining Useful Life prédit est : {rul} cycles.")

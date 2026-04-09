import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
import streamlit as st

# --- MODULE 1: DATA ACQUISITION (With Auto-Generation) ---
def load_and_clean_data():
    try:
        # Try to load your file
        data = pd.read_csv('heart_disease_data.csv')
    except FileNotFoundError:
        # Create synthetic data so the app actually runs!
        st.info("CSV not found. Generating synthetic clinical data for demonstration...")
        np.random.seed(42)
        rows = 300
        data = pd.DataFrame({
            'age': np.random.randint(30, 80, rows),
            'sex': np.random.randint(0, 2, rows),
            'cp': np.random.randint(0, 4, rows),
            'trestbps': np.random.randint(100, 180, rows),
            'chol': np.random.randint(150, 400, rows),
            'fbs': np.random.randint(0, 2, rows),
            'restecg': np.random.randint(0, 2, rows),
            'thalach': np.random.randint(100, 200, rows),
            'exang': np.random.randint(0, 2, rows),
            'oldpeak': np.random.uniform(0, 4, rows),
            'slope': np.random.randint(0, 3, rows),
            'ca': np.random.randint(0, 4, rows),
            'thal': np.random.randint(0, 4, rows),
            'target': np.random.randint(0, 2, rows)
        })
    
    X = data.drop('target', axis=1)
    y = data['target']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42), scaler

# --- MODULE 2: MODEL DEVELOPMENT ---
def train_models(X_train, y_train):
    lr_model = LogisticRegression().fit(X_train, y_train)
    nb_model = GaussianNB().fit(X_train, y_train)
    return lr_model, nb_model

# --- MODULE 3: UI ---
def main():
    st.set_page_config(page_title="HeartSense AI", page_icon="❤️")
    st.title("❤️ HeartSense AI: Early Detection System")
    
    # Sidebar inputs
    st.sidebar.header("Patient Vitals")
    age = st.sidebar.slider("Age", 20, 100, 45)
    trestbps = st.sidebar.slider("Resting BP", 80, 200, 120)
    chol = st.sidebar.slider("Cholesterol", 100, 500, 200)
    thalach = st.sidebar.slider("Max Heart Rate", 60, 220, 150)
    
    (X_train, X_test, y_train, y_test), scaler = load_and_clean_data()
    lr_model, nb_model = train_models(X_train, y_train)

    # Dummy values for remaining 9 features to match model input shape
    user_input = np.array([[age, 1, 2, trestbps, chol, 0, 1, thalach, 0, 1.0, 1, 0, 2]])
    user_input_scaled = scaler.transform(user_input)

    if st.button("Run Heart Analysis"):
        lr_prob = lr_model.predict_proba(user_input_scaled)[0][1]
        nb_prob = nb_model.predict_proba(user_input_scaled)[0][1]
        risk_score = (lr_prob + nb_prob) / 2

        st.divider()
        if risk_score > 0.7:
            st.error(f"High Risk Detected: {risk_score:.1%}")
        elif risk_score > 0.3:
            st.warning(f"Moderate Risk: {risk_score:.1%}")
        else:
            st.success(f"Low Risk: {risk_score:.1%}")

if __name__ == "__main__":
    main()

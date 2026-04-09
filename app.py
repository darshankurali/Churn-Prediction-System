import streamlit as st
import numpy as np
from src.model import train_model
st.title("Customer Churn Prediction App")
model,scaler,acc,cm,roc = train_model()
st.write(f"Model Accuracy: {acc:.2f}")
st.write(f"ROC AUC: {roc:.2f}")
st.write("Confusion Matrix:")
st.write(cm)
st.header("Predict New Customer")
tenure=st.slider("Tenure",1,72)
monthly=st.slider("Monthly Charges",20,120)
total=st.slider("Total Charges",20,8000)
input_data=scaler.transform([[tenure, monthly, total]])
if st.button("Predict"):
    result=model.predict(input_data)[0]
    st.success(f"Prediction: {'Churn' if result == 1 else 'Stay'}")
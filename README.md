# 🚀 Customer Churn Prediction System

## 📌 Overview
This project predicts customer churn using Machine Learning techniques.  
It helps businesses identify customers who are likely to leave, enabling proactive retention strategies.

---

## 🎯 Features
- Machine Learning model (Logistic Regression)  
- Feature Scaling using StandardScaler  
- Performance Metrics:
  - Accuracy Score  
  - Confusion Matrix  
  - ROC-AUC Score  
- Interactive Web App using Streamlit  
- Real-time customer prediction  

---

## 🧠 Tech Stack
- Python  
- Pandas  
- Scikit-learn  
- Streamlit  

---

## 📁 Project Structure

churn-prediction/  
│  
├── app.py  
├── requirements.txt  
├── README.md  
│  
├── data/  
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv  
│  
└── src/  
&nbsp;&nbsp;&nbsp;&nbsp;└── model.py  

---

## 📊 Dataset
This project uses the Telco Customer Churn dataset.  

🔗 https://www.kaggle.com/datasets/blastchar/telco-customer-churn  

After downloading, place the file inside the `data/` folder.

---

## ⚙️ Installation

pip install -r requirements.txt  

---

## ▶️ Run the Application

streamlit run app.py  

---

## 📈 Model Performance
- Accuracy: ~80–85%  
- ROC-AUC Score: ~0.80+  
- Evaluated using confusion matrix and probability scores  

---

## 🔍 How It Works
1. Data preprocessing and cleaning  
2. Feature selection (tenure, monthly charges, total charges)  
3. Feature scaling using StandardScaler  
4. Model training using Logistic Regression  
5. Performance evaluation using metrics  
6. Deployment via Streamlit UI  

---

## 🧪 Sample Prediction
The app allows users to input:  
- Tenure  
- Monthly Charges  
- Total Charges  

👉 Predicts: **Churn / Stay**

---

## 🚀 Future Improvements
- Use advanced models (Random Forest, XGBoost)  
- Add feature importance visualization  
- Deploy on cloud (AWS / Render / Streamlit Cloud)  
- Add customer segmentation  

---

## 💡 Use Case
- Telecom companies  
- Subscription-based platforms  
- Banking & financial services  

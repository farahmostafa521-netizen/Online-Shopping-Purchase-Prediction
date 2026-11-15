Online Shopping Purchase Prediction
Project Overview
This project uses Machine Learning to predict whether an online shopping visitor will make a purchase based on their browsing behavior.
Dataset
Online Shoppers Purchasing Intention Dataset from the UCI Machine Learning Repository.
• 12,205 records after data cleaning
• 17 input features
• Target variable: Revenue
Technologies Used
• Python
• Pandas
• Scikit-learn
• Matplotlib
• Seaborn
• Streamlit
• Joblib
Machine Learning Model
Random Forest Classifier was used to predict customer purchase behavior.
GridSearchCV was used for hyperparameter tuning.
Model Evaluation
• Accuracy: 87.79%
• Precision (Buyers): 58%
• Recall (Buyers): 79%
• F1-score (Buyers): 67%
Web Application
A Streamlit web application allows users to enter visitor information and receive a purchase prediction with a probability score.
Project Files
• app.py: Streamlit application
• purchase_prediction_model.pkl: Trained model
• Online_Shopping_Purchase_Prediction.ipynb: Data analysis and model training
• requirements.txt: Required Python libraries
How to Run
Install the required libraries:
pip install -r requirements.txt
Run the application:
streamlit run app.py


Author
Farah Mustafa

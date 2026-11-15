Online Shopping Purchase Prediction
1. Project Overview
This project uses Machine Learning to predict whether a visitor to an online shopping website is likely to make a purchase.
The project is based on the Online Shoppers Purchasing Intention Dataset from the UCI Machine Learning Repository.
A Random Forest classification model is used to analyze visitor browsing behavior and predict the purchase decision.
The project also includes a Streamlit web application that allows users to enter visitor information and receive a prediction with its purchase probability.
2. Project Objective
The main objective is to understand visitor behavior and predict whether a website session will result in a purchase.
This can help online businesses:
	•	Understand customer browsing behavior.
	•	Identify visitors who are more likely to purchase.
	•	Analyze factors related to purchasing decisions.
	•	Support data-driven marketing decisions.
3. Dataset Description
Dataset: Online Shoppers Purchasing Intention Dataset Source: UCI Machine Learning Repository Dataset ID: 468 Original Number of Records: 12,330 Number of Features: 17 Target Variable: Revenue
The dataset contains information about visitors’ activities during their sessions on an online shopping website.
Dataset Features
Feature	Description
Administrative	Number of administrative pages visited
Administrative_Duration	Time spent on administrative pages
Informational	Number of informational pages visited
Informational_Duration	Time spent on informational pages
ProductRelated	Number of product-related pages visited
ProductRelated_Duration	Time spent on product-related pages
BounceRates	Bounce rate of the session
ExitRates	Exit rate of the session
PageValues	Value of pages visited
SpecialDay	Closeness to a special day
Month	Month of the session
OperatingSystems	Operating system used
Browser	Browser used
Region	Visitor region
TrafficType	Traffic source type
VisitorType	Type of visitor
Weekend	Whether the session occurred on a weekend
Target Variable: Revenue
	•	True: The visitor completed a purchase.
	•	False: The visitor did not complete a purchase.
4. Project Workflow
The project follows these main steps:
	1.	Importing the required Python libraries.
	2.	Loading the dataset from the UCI repository.
	3.	Exploring and understanding the dataset.
	4.	Checking and removing duplicate records.
	5.	Performing Exploratory Data Analysis (EDA).
	6.	Preparing the features and target variable.
	7.	Encoding categorical features.
	8.	Splitting the dataset into training and testing sets.
	9.	Training a Random Forest classification model.
	10.	Evaluating the model.
	11.	Saving the trained model.
	12.	Building a Streamlit application.
	13.	Connecting the application to the saved model.
	14.	Testing the application with sample inputs.
5. Data Exploration and Preprocessing
The dataset is explored using Pandas to understand its structure, feature types, and statistical information.
Duplicate records are checked and removed as part of data cleaning.
Exploratory Data Analysis (EDA) is performed to understand the distribution of the target variable and explore visitor behavior using visualizations.
The project uses:
	•	NumPy for numerical operations.
	•	Matplotlib and Seaborn for data visualization.
Categorical Data Encoding
The categorical features Month and VisitorType are converted into numerical columns using One-Hot Encoding with pd.get_dummies().
The target variable Revenue is used for classification.
6. Model Training
The project uses Random Forest Classifier, a supervised Machine Learning algorithm based on multiple decision trees.
The dataset is divided into:
	•	80% Training Data
	•	20% Testing Data
The training data is used to train the model, while the testing data is used to evaluate its performance on unseen records.
7. Model Evaluation
The trained model is evaluated using classification metrics, including:
	•	Accuracy
	•	Precision
	•	Recall
	•	F1-Score
	•	Confusion Matrix
These metrics help evaluate how well the model identifies visitors who make purchases and visitors who do not.
8. Streamlit Web Application
A web application is built using Streamlit to make the trained model easy to use.
The application allows users to enter visitor session information, including:
	•	Browsing activity.
	•	Time spent on different pages.
	•	Bounce Rates and Exit Rates.
	•	Page Values.
	•	Month and Visitor Type.
	•	Operating System, Browser, Region, and Traffic Type.
	•	Weekend information.
After clicking the Predict Purchase button, the application:
	1.	Prepares the entered information in a DataFrame.
	2.	Applies One-Hot Encoding to categorical features.
	3.	Aligns the input columns with the model’s training columns.
	4.	Uses the trained model to make a prediction.
	5.	Displays the predicted purchase probability.
	6.	Shows whether the visitor is likely to make a purchase.
9. Technologies and Libraries
	•	Python
	•	Pandas
	•	NumPy
	•	Matplotlib
	•	Seaborn
	•	Scikit-learn
	•	Random Forest Classifier
	•	Streamlit
	•	Joblib
	•	UCI Machine Learning Repository
10. Project Structure
Online-Shopping-Purchase-Prediction/
│
├── app.py
├── purchase_prediction_model.pkl
├── Online_Shopping_Purchase_Prediction.ipynb
├── requirements.txt
├── .gitignore
└── README.md
11. Installation and Usage
Step 1: Clone the Repository
git clone https://github.com/farahmostafa521-netizen/Online-Shopping-Purchase-Prediction.git
Step 2: Open the Project Folder
cd Online-Shopping-Purchase-Prediction
Step 3: Install Required Libraries
pip install -r requirements.txt
Step 4: Run the Streamlit Application
streamlit run app.py
The application will open in your web browser.
12. Project Goal
This project demonstrates the use of Machine Learning classification techniques to analyze online shopping behavior and predict purchasing intention through an interactive web application.
Developed by: Farah mustafa


           Developed by: Farah Mustaf

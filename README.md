# Web-Application-Heart-Failure-Prediction-System

# Project Overview
In this situation, approximately 17 million people kill globally per year in the whole world because of cardiovascular disease, and they mainly exhibit myocardial-exhibit myocardial infarction and heart failure. Heart failure (HF) occurs when the heart cannot pump enough blood to meet the needs of the body.

In this heart prediction problem statement, we are trying to predict whether the patient's heart muscle pumps blood properly or not using Logistic Regression. In this project, a dataset is downloaded from the UCI repository and this dataset is real. this dataset is collected from one of the most famous hospitals is in the United Kingdom (UK) in 2015 and there are 299 patient records and 12 features(attribute) and one label. Based on that 12 features, we will predict whether the patient's heart working properly or not.

In this problem statement, we analyze a dataset of 299 patients with heart failure collected in 2015. We apply several machine learning & classifiers to both predict the patient’s survival, and rank the features corresponding to the most important risk factors. We also perform an alternative feature ranking analysis by employing traditional biostatistics tests and compare these results with those provided by the machine learning algorithms. Since both feature ranking approaches clearly identify serum creatinine and ejection fraction as the two most relevant features, we then build the machine learning survival prediction models on these two factors alone.

For model building we use various library packages like Pandas, Scikit learns (sklearn), matplotlib, Seaborn, Tensorflow, Keras, etc., then we will use data description, Data description involves carrying out initial analysis on the data to understand more about the data, its source, volume, attributes, and relationships. Once these details are documented, any shortcomings if noted should be informed to relevant personnel. after that, we use the data cleaning method for cleaning the dataset to check if there are any missing values or not and we split the dataset into training & testing purposes with 70%, 30% criteria. Then the next step is Model Building, The process of model building is also known as training the model using data and features from our dataset. A combination of data (features) and Machine Learning algorithms together give us a model that tries to generalize on the training data and give necessary results in the form of insights and/or predictions. Generally, various algorithms are used to try out multiple modeling approaches on the same data to solve the same problem to get the best model that performs and gives outputs that are the closest to the business success criteria. Key things to keep track of here are the models created, model parameters being used, and their results. And the last step is to analyze the result in this step we check our model score or accuracy by using Confusion Matrix and Model Score. For this model, we got 80% accuracy. In the future, we try to improve that accuracy. For model deployment, we use the python flask and based on that we build the web-based application.

# Dataset
Thirteen (13) clinical features:

- age: age of the patient (years)
- anaemia: decrease of red blood cells or hemoglobin (boolean)
- high blood pressure: if the patient has hypertension (boolean)
- creatinine phosphokinase (CPK): level of the CPK enzyme in the blood (mcg/L)
- diabetes: if the patient has diabetes (boolean)
- ejection fraction: percentage of blood leaving the heart at each contraction (percentage)
- platelets: platelets in the blood (kiloplatelets/mL)
- sex: woman or man (binary)
- serum creatinine: level of serum creatinine in the blood (mg/dL)
- serum sodium: level of serum sodium in the blood (mEq/L)
- smoking: if the patient smokes or not (boolean)
- time: follow-up period (days)
- [target] death event: if the patient deceased during the follow-up period (boolean)

# Installation
All libraries are available in Anaconda distribution of Python.

# File Description
heart_failure_clinical_records_dataset.csv: the dataset file.
heart.py: contains the code of data exploration, preparation and modeling.
heart.pkl: the classification model.
app.py: Flask API that bind between the classification model and the web page.
templates:
heart.html, main1.html, main2.html: a web page that contains a form for heart disease testing.

# Data Science Life Cycle Article
https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-020-1023-5
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0181001

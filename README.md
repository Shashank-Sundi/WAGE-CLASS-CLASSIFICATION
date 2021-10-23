# WAGE-CLASS-CLASSIFICATION

[![wakatime](https://wakatime.com/badge/user/8f2e3b3a-321e-4119-b4f0-3a33c3752953/project/d9e5d731-ebf4-4812-8dba-6d86b0c7536a.svg)](https://wakatime.com/badge/user/8f2e3b3a-321e-4119-b4f0-3a33c3752953/project/d9e5d731-ebf4-4812-8dba-6d86b0c7536a) &nbsp;
<img src="https://badge-size.herokuapp.com/Shashank-Sundi/WAGE-CLASS-CLASSIFICATION/main/app.py" alt="app_size" />&nbsp;
<img src="https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg">

ML Project to classify  the wage class of a person , based on user inputs .

<img src="static\images\sharon-mccutcheon-rItGZ4vquWk-unsplash.jpg" alt="FIFA" />
<hr>

## Deployment

The model has been deployed using REST API using flask, on Heroku : 
 https://wage-class-prediction-sundi.herokuapp.com/
 
  ##  Original Dataset and Python Notebook

Original Dataset : https://archive.ics.uci.edu/ml/machine-learning-databases/adult/

Python Notebook : https://github.com/Shashank-Sundi/NOTEBOOKS/blob/main/wage_class_pred.ipynb

<hr>


## Project Description

| PROBLEM | MODELS USED  |LIBRARIES USED   |IDE's USED|
| :-------- | :------- | :------------------------- | :-------|
| **Predicting the Wage-Class of a Person**| `XGBOOST,ADABOOST ,LOG-REG ,KNN ,RANDOM FOREST ,DECISION TREE ,SVC ,NAIVE BAYES, STACKING CLASSIFIER ` | `Sklearn , Seaborn ,Pandas ,Numpy ,Scipy ,Xgboost `|`PyCharm,` `VS Code,` `Jupyter Notebook`|

<hr>


## Project Execution

### (A) **Analysis in Jupyter Notebook**

| **Step**|**Execution of the project was carried out as given in the following steps :** |
| :--------|:-------- | 
|1|Extracted data from the UCI ML Repository: https://archive.ics.uci.edu/ml/machine-learning-databases/adult/|
|2| Validated data types of the features and analysed the statistical properties of the features
|3| Checked for null values in feature vectors.Captured the importance of missing values in some features and Implemented Random Sample Imputation 
|4| Encoded the categorical feature vectors using frequency encoding and one-hot encoding
|5| Performed EDA on data - checked the distribution of data using  KDE plots ; checked for outliers via boxplots ,etc
|6| Found outliers and imputing them with the mean value for the corresponding features
|7| Standardizing the data and Oversampling the minority class , using SMOTE
|8|Trained and tested various models on the data and chose the model which gave highest accuracy score 
|9|  Xgboost gave highest accuracy for all the data clusters 
|10|Hyperparameter tuneing of XGBoost model
|11| Exported the xgboost model via pickle


### (B) **Building the Application**

| **Step**|**Execution of the project was carried out as given in the following steps :** |
| :--------|:-------- | 
|1| Built REST API using Flask framework ; created routes for home page and pred
|2| Built html pages for data input and results prediction
|3| Created the requirements.txt , Procfile , etc. and all other requirements to be satisfied for deployment.
|4| Deployed the model on Heroku via Git Bash terminal


<hr>


## Screenshots

### **Enter the required inputs in home page and press predict button**

<img src="static\images\wage class 1.PNG" alt="FIFA" style="height: 300px; width:700px;"/>

### **The Prediction Page**

<img src="static\images\wage class  2.PNG" alt="FIFA" style="height: 300px; width:700px;"/>

  <hr>

  
## Contact :

<a href="https://www.linkedin.com/in/shashank-sundi-4b78561b1"> ![alt text](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)</a>&emsp;
<a href="https://www.instagram.com/shashank_sundi13/">![alt text](https://img.shields.io/badge/Shashank_Sundi-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)</a>&emsp;
<a href="mailto:sundi.sn@gmail.com">![alt text](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a>

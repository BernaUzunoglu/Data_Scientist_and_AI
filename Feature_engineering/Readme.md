# **Feature Engineering**

### **What is Feature Engineering in Data Science?**

In data science, **Feature Engineering** is the process of creating meaningful and model-enhancing attributes (features) from raw data. This process is one of the most critical steps in data science because well-designed features directly impact the success of a model. When combined with **Data Cleaning**, it ensures that raw data is optimized for analysis and modeling.

---

## Topics and Details

### **Outliers**  
Gained skills and knowledge on handling outliers in datasets.

- Identifying Outliers  
- Capturing Outliers  
- Functionalizing Outlier Detection  
- Accessing Outliers  
- Resolving Outlier Problems  
- Multivariate Outlier Analysis  

---

### **Missing Values**  
Developed skills and knowledge on handling missing observations in datasets.

- Identifying Missing Values  
- Capturing Missing Values  
- Solving Missing Value Problems  
- Imputation Based on Categorical Variables  
- Predictive Imputation  
- Examining the Structure of Missing Data  
- Analyzing Missing Values with Dependent Variables  

---

### **Encoding and Scaling**  
Learned about label encoding, one-hot encoding for representing data as numerical values, and scaling or transforming variables to improve model performance, especially for distance-based machine learning algorithms.

- Label Encoding  
- One-Hot Encoding  
- Rare Encoding  
- Rare Encoding Function  
- Feature Scaling  

---

### **Feature Extraction**  
Acquired techniques for transforming raw data into meaningful forms using methods like regular expressions.

- Feature Extraction  
- Binary Features  
- Text Features  
- Regex Features  
- Date Features  
- Feature Interactions  

---

### **Steps Taken and Lessons Learned in Data Cleaning and Feature Engineering**

#### **1. Cleaning Raw Data**
- **Steps Taken:**
  - Identified missing, erroneous, or incompatible data.
  - Filled missing values using methods like mean, median, or mode.
  - Removed missing or meaningless observations from the dataset when necessary.  

- **Lessons Learned:**
  - Approaches for analyzing data and identifying deficiencies.
  - Strategies for correcting missing or erroneous data.

---

#### **2. Creating New Features**
- **Steps Taken:**
  - Generated new features to add more meaning to the data (e.g., extracting year, month, day from date).
  - Created new features through mathematical operations between variables (e.g., addition, subtraction, ratios).
  - Extracted features like word length or word count from text data.  

- **Lessons Learned:**
  - Techniques for enriching data by creating new features.
  - Analyzing how new features impact model performance.

---

#### **3. Transforming Variables**
- **Steps Taken:**
  - Transformed variables unsuitable for models into different formats (e.g., label encoding or one-hot encoding for categorical variables).
  - Transformed numerical variables using logarithmic or square root methods.
  - Normalized or standardized variable distributions.  

- **Lessons Learned:**
  - Techniques for transforming variables to make them suitable for modeling.
  - Evaluating the impact of feature transformations on models.

---

#### **4. Feature Selection**
- **Steps Taken:**
  - Selected features contributing the most to model performance.
  - Removed irrelevant or insignificant variables from the model.
  - Identified and resolved issues like multicollinearity.  

- **Lessons Learned:**
  - Methods for selecting the most important features for a model (e.g., correlation analysis, importance scores).
  - How to remove unnecessary variables to prevent model overcomplexity.

---

### **Key Takeaways**
Through these processes:
- Raw data was analyzed and cleaned.
- Meaningful and performance-enhancing features were extracted from the dataset.
- Variables were made suitable for modeling.
- A dataset that improves model accuracy and generalization capacity was created.

These learnings provide a strong foundation for any machine learning project.

---

### **Project 1: Diabetes Feature Engineering**

---

### **Project Objective:**  
This project aims to develop a machine learning model that predicts whether individuals have diabetes based on data from a study of Pima Indian women living in Arizona, USA.

### **Problem Statement:**  
Early detection of diabetes using health data can contribute to determining effective treatment methods and improving individuals' quality of life. By utilizing feature engineering and data analysis processes, a model capable of predicting diabetes based on the target variable will be developed.

### **Dataset Description:**  
The dataset used in this project is part of a large pool of data maintained by the National Institute of Diabetes and Digestive and Kidney Diseases in the USA. It contains data from a study of Pima Indian women aged 21 and older living in Phoenix. The dataset comprises 768 observations and 8 independent variables.

### **Dataset Features:**  

| **Feature Name**            | **Description**                                                |
|-----------------------------|----------------------------------------------------------------|
| **Pregnancies**             | Number of pregnancies of the woman                            |
| **Glucose**                 | Blood glucose levels                                          |
| **BloodPressure**           | Diastolic blood pressure                                      |
| **SkinThickness**           | Skin thickness (mm)                                           |
| **Insulin**                 | Insulin level (mu U/ml)                                       |
| **BMI**                     | Body mass index (kg/m²)                                       |
| **DiabetesPedigreeFunction**| Diabetes pedigree function measuring family history of diabetes|
| **Age**                     | Age of the individual                                         |
| **Outcome**                 | Diabetes test result (1 = positive, 0 = negative)            |


### **Analysis and Modeling Process:**  

#### **1. Exploratory Data Analysis (EDA):**  
- **General Overview:** Identified variables in the dataset and extracted summary statistics.  
- **Analysis of Numerical and Categorical Variables:** Examined characteristics and distributions of variables.  
- **Target Variable Analysis:** Analyzed the relationship between the target variable (Outcome) and independent variables.  
- **Analysis of Missing and Outlier Values:** Treated zero values in variables like Glucose and Insulin as missing and checked for outliers.  

#### **2. Feature Engineering:**  
- Imputed missing values and capped outliers using threshold values.  
- Created new features:  
  - **Age Categories (NEW_AGE_CAT):** Groups like "Mature" and "Senior."  
  - **BMI Categories (NEW_BMI):** Groups like "Underweight," "Healthy," "Overweight," and "Obese."  
  - **Glucose Level Categories (NEW_GLUCOSE):** Groups like "Normal," "Prediabetes," and "Diabetes."  
  - Categories based on combinations of age and BMI.  
  - Categories based on insulin values.  

#### **3. Encoding:**  
Prepared categorical variables for modeling using label encoding and one-hot encoding methods.  

#### **4. Modeling:**  
Developed a prediction model using powerful algorithms like Random Forest, and evaluated its success using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.  

### **Outcomes and Benefits:**  
- A model that enables early diagnosis of diabetes.  
- Supports individualized treatment decisions in healthcare.  
- Extracted more meaningful insights from the dataset through new features.  


### **Project Files:**  

- **Dataset:** [diabetes.csv](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Feature_engineering/datasets/diabetes.csv)  
- **Code File:** [Diabetes Feature Engineering](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Feature_engineering/diabetes_feature_engineering.py)  

---

### **Project 2: Telco Customer Churn Feature Engineering**

---

### **Project Objective:**  
To understand customer behavior and develop a machine learning model that predicts which customers are likely to churn (discontinue the service) for a telecommunications company.  

### **Dataset Story:**  
This dataset contains customer information for a fictional telecommunications company operating in California during the third quarter. It includes 7,043 customer observations and 21 variables, covering demographics, services received, account information, and churn status. The goal is to analyze churn tendencies and take preventive actions to reduce customer loss.  

---

### **Variables:**  

| **Variable Name**     | **Description**                                                             | **Type**                |
|-----------------------|-----------------------------------------------------------------------------|------------------------|
| **CustomerId**        | Customer ID                                                               | Categorical            |
| **Gender**            | Gender                                                                    | Categorical            |
| **SeniorCitizen**     | Whether the customer is a senior citizen (1: Yes, 0: No)                  | Categorical            |
| **Partner**           | Whether the customer has a partner (Yes, No)                              | Categorical            |
| **Dependents**        | Whether the customer has dependents (Yes, No)                             | Categorical            |
| **tenure**            | Number of months the customer has stayed with the company                 | Numerical (Continuous) |
| **PhoneService**      | Whether the customer has phone service (Yes, No)                          | Categorical            |
| **MultipleLines**     | Whether the customer has multiple phone lines                             | Categorical            |
| **InternetService**   | Customer's internet service provider (DSL, Fiber optic, No)               | Categorical            |
| **OnlineSecurity**    | Whether the customer has online security (Yes, No, No internet service)   | Categorical            |
| **OnlineBackup**      | Whether the customer has online backup (Yes, No, No internet service)     | Categorical            |
| **DeviceProtection**  | Whether the customer has device protection (Yes, No, No internet service) | Categorical            |
| **TechSupport**       | Whether the customer has technical support (Yes, No, No internet service) | Categorical            |
| **StreamingTV**       | Whether the customer has streaming TV service                             | Categorical            |
| **StreamingMovies**   | Whether the customer has streaming movie service                          | Categorical            |
| **Contract**          | Customer's contract type (Month-to-month, One year, Two years)            | Categorical            |
| **PaperlessBilling**  | Whether the customer uses paperless billing (Yes, No)                     | Categorical            |
| **PaymentMethod**     | Customer's payment method                                                 | Categorical            |
| **MonthlyCharges**    | Monthly charges billed to the customer                                    | Numerical (Continuous) |
| **TotalCharges**      | Total charges billed to the customer                                      | Numerical (Continuous) |
| **Churn**             | Whether the customer churned (Yes, No)                                    | Categorical (Target)   |  

---

### **Data Categories:**  
1. **Service Data:**  
   - Phone, internet, security, backup, device protection, technical support, TV streaming, movie streaming.  
2. **Account Information:**  
   - Tenure, contract type, payment method, paperless billing, monthly and total charges.  
3. **Demographic Data:**  
   - Gender, senior citizen status, partner status, dependents.  

This project aims to analyze factors related to customer churn using the **Telco-Customer-Churn** dataset and develop predictive models. The methodologies and technologies used are explained as follows:

---

## **1. Technologies Used**
- **Python**: For data analysis and modeling.
- **Libraries**:
  - **Pandas**: Data manipulation and cleaning.
  - **NumPy**: Numerical computations.
  - **Matplotlib & Seaborn**: Data visualization.
  - **Scikit-learn**: Machine learning models and metrics.
  - **CatBoost, LightGBM, XGBoost**: Robust classification algorithms.

---

## **2. Steps Taken**

### **A. Data Loading and Preprocessing**
1. **Data Loading**: The Telco-Customer-Churn dataset was loaded.
2. **Adjusting Data Types**: 
   - `TotalCharges` was converted into a numerical variable.
   - `Churn` was recoded into a binary classification variable (1: Yes, 0: No).

---

### **B. Exploratory Data Analysis (EDA)**

#### 1. **General Overview**
- Obtained **shape, data types, missing values**, and **statistical summaries**.

#### 2. **Variable Categorization**
- Classified variables as categorical, numerical, or cardinal.
- **Categorical variables analysis**:
  - Example: Around 60% of customers prefer "paperless billing."
  - Fiber optic internet users have a higher churn rate.
- **Numerical variables analysis**:
  - Example: New customers (tenure = 1) tend to churn more.
  - Higher monthly charges increase the likelihood of churn.

#### 3. **Target Variable Analysis (Churn Relationships)**
- Relationships between categorical variables and churn:
  - **Short-term contracts** (month-to-month) increase churn rates.
  - Customers using **ElectronicCheck** have a higher churn rate.
- Relationships between numerical variables and churn:
  - **Tenure** negatively correlates with churn (longer tenure, lower churn).
  - **MonthlyCharges** positively correlates with churn.

#### 4. **Correlation Analysis**
- Correlation matrix:
  - **TotalCharges** and **MonthlyCharges** showed high correlation.
  - **Tenure** had a negative correlation with **Churn**.

---

## **Feature Engineering**

### 1. **Missing Value Analysis and Handling**
- **Detection**: The `missing_values_table` function effectively identified missing values and their percentages.
- **Filling**: Missing `TotalCharges` values were filled using `MonthlyCharges`. Alternatively, regression-based imputation could be explored.

---

### 2. **Outlier Analysis and Handling**
- **Threshold Calculation**: Functions like `outlier_thresholds` and `check_outlier` facilitated flexible outlier analysis.
- **Suppression**: Outliers were suppressed with the `replace_with_thresholds` function. Alternatively, transformations (e.g., logarithmic scaling) could be considered.

---

### 3. **Feature Creation**
- **Derived Variables**: Features like `NEW_TENURE_YEAR`, `NEW_Engaged`, `NEW_noProt`, and `NEW_TotalServices` provided significant insights into customer behavior.
- **Mathematical Features**: Features like `NEW_AVG_Charges` and `NEW_Increase` measured the financial impact of services on customers.

**Recommendation:**  
Check for linear relationships among the features using correlation analysis. If high correlations are found, feature selection should be revisited.

---

### 4. **Code Structure Evaluation**
- **Separation of Variables**: The use of `grab_col_names` ensured organized code.
- **Modularity**: Interactive functions (e.g., `one_hot_encoder`, `label_encoder`) provided flexibility.

---

### 5. **Model Performance**
The performance of various models was evaluated, and the results are as follows:

| Model       | Accuracy | AUC  | Recall | Precision | F1    |
|-------------|----------|------|--------|-----------|-------|
| **LR**      | 0.7999   | 0.840| 0.5003 | 0.6645    | 0.5699|
| **KNN**     | 0.7701   | 0.753| 0.4666 | 0.5851    | 0.5182|
| **CART**    | 0.7302   | 0.660| 0.5067 | 0.4922    | 0.4992|
| **RF**      | 0.7934   | 0.827| 0.5072 | 0.6404    | 0.5659|
| **XGB**     | 0.7907   | 0.826| 0.5153 | 0.6296    | 0.5664|
| **LightGBM**| 0.7940   | 0.836| 0.5222 | 0.6374    | 0.5738|
| **CatBoost**| 0.7970   | 0.840| 0.5051 | 0.6531    | 0.5691|

- **Strong Performance**: Logistic Regression and CatBoost showed strong AUC and accuracy.
- **Improvement Opportunity for Recall**: Recall rates are relatively low, indicating potential to better identify positive churn cases.

**Recommendations:**
- **Hyperparameter Tuning**: Optimize models using GridSearchCV or RandomizedSearchCV.
- **Feature Selection**: Simplify models using methods like Recursive Feature Elimination (RFE).

---

Insights from this project can guide actions to reduce customer churn, such as:
- Launching campaigns to **extend contract durations**.
- Promoting payment methods other than **ElectronicCheck** to decrease churn.

---

### Project Files  
- **Dataset**: [Telco-Customer-Churn.csv](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Feature_engineering/datasets/Telco-Customer-Churn.csv)  
- **Code File**: [Telco_Churn.py](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Feature_engineering/Telco_Churn.py
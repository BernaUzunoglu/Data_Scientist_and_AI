# CRM Analytics

CRM Analytics is one of the most widely used analysis methods in the business world. By using Python, I have learned to analyze customer data, enabling me to understand customers more closely, segment them, and make business decisions tailored to these segments. Additionally, I have gained the skills to develop churn models to retain customers. These projects helped me reinforce my programming and data analysis skills by applying them to real business problems.

## Topics and Details

### 1. Introduction to CRM Analytics:

- I developed the ability to interpret product performance using various time-based mathematical indicators and analyze fundamental digital marketing metrics.
- I learned to interpret the performance of products and services by analyzing Key Performance Indicators (KPIs).
- Through cohort analysis, I gained the ability to understand customer loyalty and trends by analyzing customer behavior over time.

**Covered Topics:**
- Introduction to CRM Analytics
- Key Performance Indicators (KPIs)
- Cohort Analysis

### 2. RFM Analysis:

- I successfully learned to perform rule-based segmentation based on customer purchasing behavior, including data preparation, calculating RFM metrics, and creating segments.
- I enhanced my efficiency by modularizing the RFM analysis process.

**Covered Topics:**
- Data Preparation
- Calculating RFM Metrics
- Calculating RFM Scores
- Creating RFM Segments
- Modularizing the Process

### 3. Customer Lifetime Value (CLTV):

- I developed the ability to calculate Customer Lifetime Value (CLTV) by analyzing purchasing and profitability patterns using mathematical and statistical models.
- I learned how to analyze customer value using metrics such as average order value, purchase frequency, repurchase, and churn rates.
- I learned to integrate these analyses into business decisions by creating segments based on customer lifetime value.

**Covered Topics:**
- Data Preparation
- Average Order Value
- Purchase Frequency
- Repurchase and Churn Rates
- Profit Margin
- Customer Value
- Customer Lifetime Value
- Creating Segments
- Modularizing the Entire Process

### 4. Predicting Customer Lifetime Value:

- I gained expertise in modeling customer churn and purchase behavior using BG/NBD and Gamma-Gamma models.
- I developed scalable analysis models by modularizing the entire CLTV prediction process.
- I used these methods to perform customer segmentation and develop strategies based on behavior patterns.

**Covered Topics:**
- Expected Transaction Count with BG/NBD
- Gamma-Gamma Submodel
- CLTV Prediction with BG/NBD and Gamma-Gamma
- Data Reading
- Preparing Lifetime Data Structure
- Building the BG/NBD Model
- Building the Gamma-Gamma Model
- Calculating CLTV with BG/NBD and Gamma-Gamma
- Creating Customer Segments
- Modularizing the Process

## PROJECT 1: Customer Segmentation with RFM

### Business Problem:
This project aims to analyze the shopping behavior of FLO customers and create segments based on their behaviors to develop marketing strategies. In the project, RFM analysis was used to segment customers, and specific strategies were developed for each segment.

**Project Goal:**
- Segment customers based on their behavior.
- Develop different marketing strategies for each segment.
- Strengthen customer relationships and contribute to revenue growth.

**Dataset Story:**
The dataset consists of the shopping history of OmniChannel (both online and offline shoppers) customers from 2020-2021.

**Dataset Variables:**

| **Variable Name**                       | **Description**                      |
|-----------------------------------------|--------------------------------------|
| `master_id`                             | Unique customer ID                   |
| `order_channel`                         | Platform used for shopping (Android, iOS, Desktop, Mobile, Offline) |
| `first_order_date`                      | Date of the customer’s first purchase |
| `last_order_date`                       | Date of the customer’s last purchase  |
| `last_order_date_online`                | Date of the customer’s last online purchase |
| `last_order_date_offline`               | Date of the customer’s last offline purchase |
| `order_num_total_ever_online`           | Total number of online purchases by the customer |
| `order_num_total_ever_offline`          | Total number of offline purchases by the customer |
| `customer_value_total_ever_online`      | Total amount spent by the customer on online purchases |
| `customer_value_total_ever_offline`     | Total amount spent by the customer on offline purchases |
| `interested_in_categories_12`           | List of categories the customer has shopped from in the last 12 months |

### RFM Analysis:
RFM analysis segments customers based on the following three criteria:
- **Recency (Last Purchase)**: The time since the customer's last purchase.
- **Frequency (Purchase Frequency)**: The total number of purchases made by the customer.
- **Monetary (Spending)**: The total amount spent by the customer.

**Project Steps:**
1. **Data Preparation**: Checked for missing values and transformed date columns into appropriate formats. Calculated total number of purchases and total spending.
2. **RFM Metric Calculation**: Calculated Recency, Frequency, and Monetary values.
3. **RFM Score Calculation**: Assigned scores from 1 to 5 based on RFM values.
4. **Segmentation**: Classified customers based on their RF scores into segments.

### Customer Segments:
| **Segment Name**        | **Description**                          |
|-------------------------|------------------------------------------|
| `hibernating`           | Customers with decreased engagement      |
| `at_Risk`               | Customers at high risk of churn          |
| `cant_loose`            | Customers that must not be lost          |
| `about_to_sleep`        | Customers who are about to stop engaging |
| `need_attention`        | Customers who need special attention     |
| `loyal_customers`       | Loyal customers                         |
| `promising`             | Customers with high potential            |
| `new_customers`         | Newly acquired customers                 |
| `potential_loyalists`   | Customers with potential to become loyal |
| `champions`             | Most valuable and highly engaged customers |

[Explore the Dataset Here](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/CRMAnalysis/datasets/flo_data_20k.csv).

[FLO Customer Segmentation and Marketing Strategies Work](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/CRMAnalysis/FLO_RFM.py)

## PROJECT 2: FLO Customer Lifetime Value (CLTV) Prediction and Segmentation

**Dataset:** [flo_data_20k.csv](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/CRMAnalysis/datasets/flo_data_20k.csv)

**Project Objective:**
Analyze customer data to predict Customer Lifetime Value (CLTV) and segment customers accordingly. This enables more targeted and efficient marketing and customer management strategies.

### Modeling:
- **BG/NBD Model:** Used to predict future customer purchase behaviors.
- **Gamma-Gamma Model:** Used to predict the future spending amounts for each customer segment.

[FLO Customer Lifetime Value (CLTV) Prediction and Segmentation](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/CRMAnalysis/FLO_CLTV_Prediction.py)

---

**Berna Uzunoğlu | Python Developer | Data Scientist**

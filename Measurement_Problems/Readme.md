# A/B Testing for Comparing Bidding Methods' Conversion (Facebook)

This project involves an **A/B test** to compare the purchase performance (**Purchase**) of two Facebook ad bidding strategies: **Maximum Bidding** and **Average Bidding**.

## Business Problem  
Facebook introduced a new bidding method, **Average Bidding**, as an alternative to the existing **Maximum Bidding**.  
Our client, **bombabomba.com**, decided to test this new feature to determine whether Average Bidding generates more conversions than Maximum Bidding. The effectiveness of ad strategies will be evaluated based on the test results.  

---

## Dataset Description  

The dataset includes control and test groups. Each group contains information about the number of ad impressions, clicks, purchases, and revenue.  

- **Control Group:** Maximum Bidding method was applied.  
- **Test Group:** Average Bidding method was applied.  

The following variables are included for both groups:  

- **Impression:** Number of ad impressions.  
- **Click:** Number of clicks on ads.  
- **Purchase:** Number of purchases made after clicking on ads.  
- **Earning:** Revenue generated from purchases.  

---

## A/B Testing Process  

### 1. Hypothesis Formulation  
- **Null Hypothesis (H0):** The Average Bidding method does not generate more conversions than the Maximum Bidding method.  
  \(H_0: \mu_{control} = \mu_{test}\)  
- **Alternative Hypothesis (H1):** The Average Bidding method generates more conversions than the Maximum Bidding method.  
  \(H_1: \mu_{control} \neq \mu_{test}\)  

---

### 2. Assumption Checks  
Two fundamental assumptions were tested for the validity of the A/B test:  

#### a. Normality Assumption  
- The normality assumption was tested using the **Shapiro-Wilk Test**.  
  - **Control Group:** \(p = 0.5891\) → The normality assumption is satisfied.  
  - **Test Group:** \(p = 0.1541\) → The normality assumption is satisfied.  

#### b. Homogeneity of Variance Assumption  
- Homogeneity of variance was tested using the **Levene Test**.  
  - **Result:** \(p = 0.1083\) → Homogeneity of variance is satisfied.  

---

### 3. Hypothesis Testing  
- After the assumption tests, an **Independent Samples T-Test (ttest_ind)** was performed.  
- **Result:**  
  - \(p = 0.3493\): The null hypothesis (H0) cannot be rejected.  
  - No statistically significant difference was found in the purchase means between the two groups.  

---

## Analysis and Recommendations  

### 1. Interpretation of Results  
- According to the A/B test results, there is no statistically significant difference in purchases (Purchase) between the **Average Bidding** and **Maximum Bidding** methods.  

### 2. Recommendations to the Client  
- The tested new bidding strategy currently does not provide a significant advantage.  
- A longer testing period or a larger sample size may be considered for a new A/B test.  
- Alternative metrics (e.g., revenue per user, ad click-through rate) can be analyzed.  
- Strategy improvements or customized offers for different user segments could be explored.  

---

## Technical Methods and Applications  

The following methods and tools were used throughout the project:  

1. **Data Preparation and Exploratory Data Analysis (EDA):**  
   - Control and test group data were merged and analyzed.  

2. **Statistical Tests:**  
   - **Normality Assumption:** Shapiro-Wilk Test  
   - **Homogeneity of Variance:** Levene Test  
   - **Hypothesis Test:** Independent Samples T-Test  

---

## Project Files  

- **Dataset:** [ab_testing.xlsx](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Measurement_Problems/datasets/ab_testing.xlsx)  
- **Code File:** [AB_Testing_Study.py](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Measurement_Problems/AB_Testing_Study.py)  

---

**Berna Uzunoğlu | Python Developer | Data Scientist**

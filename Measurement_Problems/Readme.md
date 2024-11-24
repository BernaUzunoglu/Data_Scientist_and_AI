# Measurement Problems

I have gained skills in approaches used to rate products and the methods for ranking reviews and ratings, which are key factors influencing purchasing decisions.

## Topics and Details

### 1. Rating Products
I gained detailed knowledge about the approaches used in product rating. I learned how unbiased rating methods can be created using statistical techniques. The approaches examined include:
- Average Rating Calculation
- Time-based Weighted Average Rating
- User-based Weighted Average Rating
- Weighted Rating

### 2. Sorting Products
I investigated the effects of product reviews and ratings on purchasing decisions. I learned about the methods used to sort the reviews and ratings provided by users. The approaches discussed include:
- Sorting by Rating
- Sorting by Review and Purchase Count
- Sorting by Rating, Purchase, and Review
- Bayesian Average Rating
- Hybrid Sorting
- IMDB Movie Rating and Sorting Methods

### 3. Sorting Reviews
I learned about the methods for sorting reviews, which have a significant impact on purchasing decisions. The methods include:
- Up-Down Difference Score
- Average Rating Calculation
- Wilson Lower Bound Rating

### 4. A/B Testing
I worked on A/B testing methods and statistical analyses to understand differences between two groups. The topics I covered include:
- Sampling and Descriptive Statistics
- Confidence Intervals and Hypothesis Testing
- Independent Two-Sample T-Test
- Two-Group Proportion Comparison Test
- ANOVA (Analysis of Variance) for Comparing More Than Two Group Means

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


# Project 2: Rating Product & Sorting Reviews in Amazon

## Project Objective
One of the fundamental problems in e-commerce is the correct calculation of product ratings and reviews. This project aims to calculate a product's average rating by weighting it according to recent reviews and sort the reviews displayed on the product detail page. This will result in more accurate product ratings and trustworthy reviews, providing a more efficient shopping experience for users and sellers.

## Business Problem
One of the most important issues in e-commerce is the accurate calculation of product ratings given after sales. Solving this problem means more customer satisfaction for the e-commerce site, better visibility of the product for sellers, and a seamless shopping experience for buyers. Another problem is the correct sorting of product reviews. Misleading reviews can directly impact sales, leading to financial loss and customer attrition. By solving these two core problems, the e-commerce site and sellers will increase sales, while customers will complete their purchase journey seamlessly.

## Dataset Story
This dataset, containing Amazon product reviews, includes reviews and user ratings for products in the electronics category. Each review includes metadata such as the product rating (overall), review text (reviewText), the number of helpful votes (helpful_yes), and the total number of votes (total_vote).

### Variables:
| Variable       | Description                                                               |
|----------------|---------------------------------------------------------------------------|
| **reviewerID** | User ID                                                                   |
| **asin**       | Product ID                                                                |
| **reviewerName**| User Name                                                                |
| **helpful**    | Helpful rating                                                           |
| **reviewText** | Review text                                                              |
| **overall**    | Product rating                                                            |
| **summary**    | Review summary                                                           |
| **unixReviewTime**| Review time - Unix timestamp representing the number of seconds since January 1, 1970. |
| **reviewTime** | Raw review time                                                           |
| **day_diff**   | Number of days since the review                                          |
| **helpful_yes**| Number of helpful votes for the review                                     |
| **total_vote** | Total number of votes for the review                                      |

## Project Process

1. **Exploration of the Dataset**:
   - The dataset was loaded, and basic product information was examined.
   - Missing values in the dataset were checked.

2. **Task 1: Calculating and Comparing the Average Rating**:
   - The average product ratings were calculated from the existing "overall" column.
   - Additionally, weighted averages based on review dates were calculated to highlight more recent evaluations.

3. **Task 2: Selecting the Most Helpful Reviews**:
   - A "helpful_no" variable was created to calculate the difference between positive and negative reviews.
   - Metrics such as "score_pos_neg_diff", "score_average_rating", and "wilson_lower_bound" were used to assign reliability scores to each review.

4. **Evaluation of Results**:
   - The top 20 most helpful reviews, sorted by Wilson's lower bound, were selected, and the most trustworthy reviews were highlighted.

## Techniques and Applications
- **Rating Weighting**: Reviews were weighted based on time, with older reviews receiving lower scores than newer ones.
- **Data Cleaning and Preparation**: Missing data was cleaned, and necessary transformations were applied.
- **Review Sorting**: Metrics such as "helpful_no", "score_pos_neg_diff", "score_average_rating", and "wilson_lower_bound" were used to rank trustworthy reviews.

## Results
- It was observed that weighting recent reviews had a significant impact on the average rating calculation.
- The "Wilson Lower Bound" method was successful in filtering out misleading reviews and highlighting the most reliable ones.
- With this project, more accurate and reliable product reviews were provided for users and sellers, improving the overall shopping experience.

## Project Files

- **Dataset:** [amazon_review.csv](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Measurement_Problems/datasets/amazon_review.csv)  
- **Code File:** [Rating Product & Sorting Reviews in Amazon.py](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Measurement_Problems/Rating%20Product%20%26%20Sorting%20Reviews%20in%20Amazon.py)

---

**Berna Uzunoğlu | Python Developer | Data Scientist**

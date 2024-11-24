# Recommendation Systems  

Recommendation Systems are machine learning-based systems that automatically suggest products, services, or content likely to interest users. They are widely used in areas such as e-commerce, music platforms, video streaming services, and social media. These systems enhance user experience while boosting companies' sales and customer satisfaction.  

### **Core Functionality of Recommendation Systems**  

Recommendation systems analyze users' past behaviors, preferences, and their relationships with other users to generate recommendations. Their functionality can be categorized into three main approaches:  

---  
## Topics and Details  

### 1. **Association Rule Learning**  

Association rule learning is a technique primarily used in the retail sector. Its goal is to uncover relationships between products often purchased together by customers.  

- **Example Application**: In market basket analysis, insights like "If a customer buys bread, they often buy milk too" are obtained.  
- **Advantages**:  
  - Quick implementation.  
  - Works with simple data structures.  
- **Disadvantages**:  
  - Relies solely on past data, making it challenging to work with new users or products.  

- **Subtopics**:  
  - Apriori Algorithm  
  - How Apriori Works  
  - Association Rule-Based Recommendation System  
  - Association Rule Learning  
  - Data Preprocessing  
  - Preparing ARL Data Structures  
  - Analyzing Association Rules  
  - Writing the Script  
  - Product Recommendation Application  

---  
### 2. **Content-Based Filtering**  

This method generates recommendations based on the features of a product. By analyzing the features of products users like, it suggests similar products.  

- **Example Application**: On Netflix, if a user enjoys action movies, other action movies with similar content features are recommended.  
- **Techniques Used**:  
  - **TF-IDF**: A technique commonly used in text-based data to measure the importance of keywords and analyze similarity.  
  - **Cosine Similarity**: Used to measure similarity between content features.  
- **Advantages**:  
  - Does not require user history.  
  - Utilizes content similarities between products.  
- **Disadvantages**:  
  - Limited in introducing new products to the user (only suggests similar content).  

- **Subtopics**:  
  - Count Vector  
  - Text Vectorization  
  - Content-Based Recommendation Systems  
  - Creating the TF-IDF Matrix  
  - Calculating Cosine Similarity  
  - Making Recommendations Based on Similarities  
  - Writing the Script  

---  
### 3. **Collaborative Filtering**  

This method creates recommendations based on users' past behaviors and their similarities to other users.  

- **Techniques**:  
  - **User-Based Collaborative Filtering**: Analyzes preferences of similar users to provide recommendations.  
  - **Item-Based Collaborative Filtering**: Uses relationships between similar items to make suggestions.  
- **Example Application**: Spotify suggests songs based on playlists created by users with similar music preferences.  
- **Advantages**:  
  - Learns from user behaviors.  
  - Does not require content features.  
- **Disadvantages**:  
  - **Cold-Start Problem**: Struggles to work with new users or products.  
  - High computational cost in large datasets.  

- **Subtopics**:  
  - Item-Based Recommendation System  
  - Item-Based Collaborative Filtering  
  - Creating the User-Movie DataFrame  
  - Making Item-Based Movie Recommendations  
  - Writing the Script  
  - User-Based Collaborative Filtering  
  - Preparing the Dataset  
  - Retrieving Watched Movies  
  - Identifying Users Watching Similar Movies  
  - Determining Similarities  
  - Calculating Scores  
  - Functionalizing the Work  

---  
### 4. **Model-Based Methods**  

Model-based methods employ more sophisticated algorithms and mathematical models. One such technique is **Matrix Factorization**, which extracts feature vectors for users and products and generates recommendations based on the relationships between these vectors.  

- **Example Application**: Predicting the rating a user would give to a product they have not yet rated on Amazon.  
- **Advantages**:  
  - Works well with sparse datasets.  
  - Can model complex relationships.  
- **Disadvantages**:  
  - Requires more computational power and time.  

- **Subtopics**:  
  - Gradient Descent  
  - Data Preparation  
  - Modeling  
  - Building the Model  
  - Final Model and Predictions  

---  
### **Applications of Recommendation Systems**  

- **E-commerce**: Product recommendations (Amazon, eBay).  
- **Music and Video Platforms**: Song and movie recommendations (Spotify, Netflix).  
- **Social Media**: Follower suggestions, content recommendations (Instagram, Twitter).  
- **Education**: Online course recommendations (Coursera, Udemy).  

Recommendation systems offer personalized experiences by better understanding users, enhancing user satisfaction, and increasing business revenues.

### **Project 1: Service Recommendation System Based on Association Rules for Armut Platform**  

---

### **Project Goal**  
The goal is to develop a content-based product recommendation system for Armut, one of Turkey's largest online service platforms, by identifying relationships between the services purchased by customers using **Association Rule Learning** methods.  

This system aims to suggest services similar to those purchased by users, thereby enhancing user experience.  

---

### **Business Problem**  
On the Armut platform, there is no predefined concept of a "basket" for users' purchased services. Monthly purchased services are defined as a basket, and association rules are derived from these baskets. The objective is to make the most likely service recommendations to customers based on their past purchases.  

---

### **Dataset Description**  

The dataset is suitable for analyzing how users utilize services across different categories and how these services change over time.  

### Variables  

| **Variable**   | **Description**                                                         |
|----------------|-------------------------------------------------------------------------|
| **UserId**     | A unique identifier for each customer.                                 |
| **ServiceId**  | An anonymized identifier for the services under each category.         |
| **CategoryId** | An anonymized ID representing the category of the services.            |
| **CreateDate** | The date when the service was purchased.                               |

---

### **Technologies and Methods Used**  

#### **1. Data Preprocessing**  
- The dataset was loaded and analyzed using pandas.  
- **ServiceId** and **CategoryId** were merged to create a unique **Service** column.  
- To define monthly baskets, users' service purchase dates were reformatted to a year-month format.  
- A combined **BasketID** column was created using user and date information.  

#### **2. Creating a Pivot Table**  
- Services purchased by users were converted into a pivot table.  
- The pivot table was transformed into a binary format suitable for analysis.  

#### **3. Association Rules**  
- Frequent service associations were extracted using the **Apriori Algorithm**.  
- Association rules were ranked based on **lift**, **confidence**, and **support** metrics.  
- These rules formed the foundation of the recommendation system.  

#### **4. Service Recommendation Function**  
- A function named **arl_recommender** was developed to take a given service ID and provide likely service recommendations for users.  

---

### **Insights and Results**  

- **Most Popular Service Associations:**  
  - For example, it was observed that users who purchased the `2_0` service often also purchased the `3_1` service.  

- **Personalized Recommendations for Users:**  
  - Using association rules, the system can provide the most relevant service recommendations to customers.  

- **Lift Value Analysis:**  
  - A high lift value indicates that the probability of two services being purchased together is greater than their independent probabilities.  

- **Potential for Improvement:**  
  - The system can be used to analyze user behavior and develop potential cross-selling strategies.  

---

### **Technologies Used**  
- **Python**: Pandas, mlxtend (for Apriori and Association Rules).  
- **Data Visualization**: Not directly used in this project, but tools like `seaborn` or `matplotlib` could be used in the future.  
- **Algorithm**: Apriori Algorithm and Association Rules.  

---

### **Conclusion**  
This project marks a critical step in understanding customer behavior on the Armut platform. Personalized recommendations were made to enhance user experience, which has the potential to increase customer satisfaction. The study provides a strong foundation, especially for developing cross-selling campaigns and boosting customer loyalty.  

---

### **Project Files**  

**Code File:** [armut_arl_project.py](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Recommendation_Systems/armut_arl_project.py) 

### **Project 2: Hybrid Recommender System**  

---

### **Objective and Problem Statement:**  
The aim of this project is to build a hybrid recommendation system for users. Based on their past interactions and ratings, users are provided with recommendations using both user-based collaborative filtering and item-based collaborative filtering. The main goal is to leverage existing user data to generate accurate movie recommendations and enhance the user experience.

---

### **Dataset Overview:**  
The dataset is provided by MovieLens, a movie recommendation service. It contains ratings for 27,278 movies, given by users over 2,000,263 interactions. The dataset spans from January 9, 1995, to March 31, 2015, and includes 138,493 users, all of whom have rated at least 20 movies.  

Two main datasets were utilized:  

- **Movie Dataset:** Contains information about movie titles and genres.  
- **Rating Dataset:** Contains user ratings and timestamps for movies.  

---

### **movie.csv**
| **Variable** | **Description**            |
|--------------|-----------------------------|
| movieId      | Unique movie identifier.    |
| title        | Movie name.                 |
| genres       | Genre.                      |

- **Total Observations:** 27,278  
- **File Size:** 1.5 MB  

---

### **rating.csv**
| **Variable** | **Description**                             |
|--------------|---------------------------------------------|
| userId       | Unique user identifier (UniqueID).          |
| movieId      | Unique movie identifier (UniqueID).         |
| rating       | Rating given by the user for the movie.     |
| timestamp    | Date of the rating.                        |

- **Total Observations:** 2,000,263  
- **File Size:** 690.4 MB  

These datasets offer rich insights into user preferences and behaviors for movie recommendation and prediction tasks.

---

### **Technologies and Methods Used:**  
The project employed the following technologies and methodologies:  

#### **Technologies Used:**  
- **Python:** Used for data manipulation and analysis.  
- **Pandas:** Core tool for data processing and frameworking.  

#### **Steps and Algorithms Applied:**  
1. **User-Based Collaborative Filtering:**  
   - Recommendations based on similarities between users.  
   - Correlation threshold (e.g., 0.65) was set to select similar users.  

2. **Item-Based Collaborative Filtering:**  
   - Recommendations based on similarities between movies.  
   - Movie correlations were calculated to determine recommendations.  

3. **Hybrid Recommendation:**  
   - Combined user-based and item-based approaches to deliver more diverse recommendations.  

#### **Data Processing Steps:**  
- **Filtering:** Movies with fewer than 1,000 ratings were removed.  
- **Pivot Table:** A user-movie interaction matrix was created for modeling relationships.  

---

### **Project Outcomes:**  
- Generated **10 diverse movie recommendations**:  
  - 5 movies using user-based methods.  
  - 5 movies using item-based methods.  
- Movies most likely to interest the user were determined based on their correlations.  

This system takes a significant step towards enhancing user experience by providing personalized recommendations based on their past preferences. The hybrid structure ensures the recommendations are both diverse and accurate.

---

### **Project Files:**  
- **Code File:** [hybrid_reccommender_project.py](https://github.com/BernaUzunoglu/Data_Scientist_and_AI/blob/main/Recommendation_Systems/hybrid_reccommender_project.py)  

---  
**Berna Uzunoğlu | Python Developer | Data Scientist**  
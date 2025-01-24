# Data Science Grind 100

## Theory

### High Frequency

#### Python & Data Wrangling 
1. When would you use a `groupBy` operation in Pandas? Provide and example #easyDS100 
> [!Success]
> We `groupBy` when we need to summarize/aggregate calculations based on categories or groups.
> For example say we wanted to find the total sales revenue month on month, we'd do
> ```
> df.groubBy('month')[sales].sum()
> ```
2. What is the difference between `iloc` and `loc` in Pandas? #easyDS100  
>[!Success]
> - `iloc` uses **integer** position/location based indexing (like arrays).
> - `loc` uses **label**-based indexing (like row/columns labels).
> For example consider the following series of characters with a non-monotonic(not consistent) integer index
> ```
> >>> s = pd.Series(list("abcdef"), index=[49, 48, 47, 0, 1, 2])
> 49    a
> 48    b
> 47   c
> 0     d
> 1     e
> 2     f
> >>> s.loc[0] # value at index label 0
> 'd'
> >>> s.iloc[0] # value at index location 0
> 'a'
> >>> s.loc[0:1] # rows at index labels between 0 and 1 (inclusive)
> 0   d 
> 1   e 
>> >>> s.iloc[0] # rows at index location between 0 and 1 (exclusive)
> 1   e 
>> >>> s.iloc[0] # rows at index location between 0 and 1 (exclusive)
> ```


#### SQL
1. Explain the difference between `INNER JOIN` , `LEFT JOIN`, `RIGHT JOIN` and `FULL JOIN`. #easyDS100  
> [!Success]
> **INNER JOIN**: Returns matching rows in both tables 
> **LEFT JOIN**:  Return all rows from the left table + matched from right.
> **RIGHT JOIN**: Returns all rows from the right table + matched from left
> **FULL JOIN**: Returns rows from both tables(matched + unmatched)

#### Probability & Statistics
1. What's the difference between Type I and Type II errors? #easyDS100 
2. Explain p-values in layman's terms #easyDS100 
3. What is the Central Limit Theorem and why it is important? #easyDS100 
4. How do you interpret confidence intervals? #easyDS100 

#### Advance Statistics & Experimentation
1. Explain A/B testing and how you determine sample size. #mediumDS100 
2. How do you define a null hypothesis and alternative hypothesis in an experiment? #easyDS100 
3. How do you measure the success of an A/B test, and what metrics are most important? #mediumDS100 
#### Machine Learning Fundamentals
1. Explain the bias-variance trade-off #easyDS100 
2. What is cross-validation and why is it useful? #easyDS100 
3. Define overfitting and underfitting with examples #easyDS100 
4. How do you evaluate a classification model (precision, recall, F1, ROC, AUC)? #mediumDS100 
5. Explain how Logistic Regression works and how to interpret its coefficients. #mediumDS100 
6. How do you handle imbalanced datasets? #mediumDS100 

#### Ensemble & Advanced ML
1. Describe how a Random Forest works #mediumDS100 
2. What is Gradient Boosting, and how is it different from Bagging? #mediumDS100 
3. What are hyperparameters, and how do you typically tune them? #mediumDS100 

#### Deep Learning
1. Explain the concept of backpropagation? #mediumDS100 
2. How do you approach transfer learning in deep learning? #mediumDS100 

#### Business & Product Sense
1. Explain a project where you had to balance technical accuracy with business requirements. #easyDS100 
2. How do you choose the right evaluation metric for a business problem? #mediumDS100 
3. Walk me through how you'd design a recommendation system for an e-commerce site #mediumDS100 

#### Behavioral & Team Fit
1. Tell me about a challenging data science problem you faced and how you solved it. #easyDS100 

## Practical

### High Frequency

#### Python & Data Wrangling

1. How do you handle missing value in a Pandas `DataFrame`? Give at least 2 approaches? #easyDS100
2. Describe how you would merge/join two data sets in Pandas? #easyDS100 

#### SQL
1. Write a query to find all employees with a salary above the average salary of their department #mediumDS100
2. How would you find the second highest (or Nth highest) value in a table? #mediumDS100 



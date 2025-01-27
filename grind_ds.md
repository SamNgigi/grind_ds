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
> [!Info]
>
> - **INNER JOIN**: Returns matching rows in both tables 
> - **LEFT JOIN**:  Return all rows from the left table + matched from right.
> - **RIGHT JOIN**: Returns all rows from the right table + matched from left
> - **FULL JOIN**: Returns rows from both tables(matched + unmatched)

#### Probability & Statistics
1. What's the difference between Type I and Type II errors? #easyDS100 
> [!Succes]
>
> - **Type I (False Positive)**: Rejecting the null hypothesis when it's actually true
>> If we use pregnancy tests as an example we can say Type I error would be a result indicating the test is pregnant when they actually aren't.
>>
>> Another example may be pursing a business idea based on incomplete validation assuming it will succeed when it is likely it will fail on further analysis
>
> - **Type II (False Negative)**: Failing to Reject the null hypothesis when it's actually false 
>> A Type II error would be a result indicating that a tester isn't pregnant when they actually are
>>
>> In context of a business it may mean giving up on a business idea to early yet is would have likely succeeded given time
>

2. Explain p-values in layman's terms #easyDS100 
> [!Success]
>
> The p-value is the probability of observing a result at least as extreme as the one observed/gotten, assuming the null hypothesis is true.
> 
> A low p-value suggests your observed data is unlikely under the null hypothesis, leading you to seriously consider rejecting it

3. What is the Central Limit Theorem and why it is important? #easyDS100 
>[!Success]
>
> The **Central Limit Theorem** states that the distribution of sample means approach a normal distribution as the sample size grows, regardless of the population's distribution
>
> This is important because it justifies using normal approximation for inference. This is to mean that even if the world is messy, _averages of large samples behave predictably_
> like a bell curve. This is why polls, medical studies, and quality control in factories rely on normal distribution tool.
>

4. How do you interpret confidence intervals? #easyDS100 
> [!Success]
>
> A confidence inteval is interpreted as a range of values within which we are a certain level of "confident" that the true population parameter (like the mean) lies, based on the data from the sample;
> essentially, if we were to repeate the sampling process many times the calculated confidence intervals would capture the true population parameter a specified % of the time
> 
>
> It means 95% confidence interval means that if we repeat the experiment many times, ~95% of the computed intervals would contain the true parameter
>
> We are 95% confident that 95% of the time the true population parameter value would lie within a specific interval

#### Advance Statistics & Experimentation
1. Explain A/B testing and how you determine sample size. #mediumDS100 
> A/B testing is about comparing 2 versions of the same experiment (A, B) on a key metric (e.g conversion)
> 
> The sample size is determined by **desired power**, **significance level** and **minimum detectable effect**.
>> - **power** - ability to find real effects
>> - **significance level** - false positive risk
>> - **minimum desired effect (MDE)** - smalles effect worth detecting
>
> A common approach is to use a standard formula or tool such as power analysis to determine an appropriate sample size
>


2. How do you define a null hypothesis and alternative hypothesis in an experiment? #easyDS100 
> Null Hypothesis **H0** Assumes no dfference in status quo
>
> Alternative Hypothesis **H1** Assumes there is a desired difference or effect

3. How do you measure the success of an A/B test, and what metrics are most important? #mediumDS100 
> Measure/KPI that is aligned with the business outcome typically conversion rate, click-through rate, revenue per user
>
> Important to look at statistical significance and practical significance


#### Machine Learning Fundamentals
1. Explain the bias-variance trade-off #easyDS100 
> - **Bias** - Difference between the predicted values and correct values. High Bias gives a large error in both
> training and test data. High bias leads to **Underfitting** i.e. the inability of a model to capture the underlying complexity/pattern of the data. It is recommended an algorithm have low bias.
> - **Variance** - In machine learning is the amount by which the performance of a predictive model changes when it is trained on different subsets of the training data, indicating how sensitive it is to another subset of the training set.
>
> Low variance means a model is less sensitive to changes in the training data and can produce consistent estimates. This may indicate undefitting
>
> High variance means that the model is very sensitive to changes in the training data meaning that may have also capture the noise in the traning data making perform poorly in new unseen test data.
>
>Ideally we want a model that has low bias and low variance which is not possible because optimizing for one causes the opposite change in the other.
>

2. What is cross-validation and why is it useful? #easyDS100 
> e.g **k-fold** splits data into multiple folds. In each iteration we use one fold for validation the other for training.
>
> Helps reduce overfitting and improve generalization estimates
>

3. Define overfitting and underfitting with examples #easyDS100 
> - **Overfitting:** Model captures noise and performs poorly on new data (e.g. a polynomial of very high degree that fits
> training data points exactly)
> - **Underfittig:** The model is too simple to capture the trend (e.g. using a linear model for a highly non-linear data)

4. How do you evaluate a classification model (precision, recall, F1, ROC, AUC)? #mediumDS100 
> - **Confusion Matrix:** Table of TP, FP, TN, FN to derive metrics like precision, recall and F1 for a granular view of the model.
> - **Precision:** Of all predicted positives how many are truly positive i.e. TP/(TP + FP). When minimizing False Positive is critical (spam detection, legal risk prediction)
> - **Recall:** Of all actual positives how many did we predict correctly i.e. TP/(TP + FN). When minimizing False Negatives is vital (medical diagnoses, fraud detection)
> - **F1 Score:** Harmonic mean of precision and recall. Used for balancing precision and recal in imbalanced datasets. Avoid if one metric is more critical
> - **ROC-AUC:** Area under the Receiver Operating Characterstic Curve (TPR vs FPR). Used for comparing overall model performance especially with balanced classes. Less reliable
> for severe imbalance
> - **PR-AUC:** Area under the Precision-Recall Curve. Usesd in imbalanced datasets or when focus is on positive class (e.ge rare disease screening)

5. Explain how Logistic Regression works and how to interpret its coefficients. #mediumDS100 
> Logistic regression works by using the logit function(sigmoid function) to model probability of a binary outcome.
> 
> The sign of the coefficient indicates direction of influence on the log-odds; exponentiated coefficients indicates the odds ratio for 1-unit increase in that feature.
>
>> - **Positive Coefficients:** Increase the log-odds (and hence the probability) of a positive class
>> - **Negative Coefficients:** Decrease the log-odds (and hence the probability) of a positive class
>> - **Magnitude:** Larger coefficients indicate stronger effects of the corresponding feature

6. How do you handle imbalanced datasets? #mediumDS100 
> - **Over Sampling (Synthetic Minority Over-Sampling Technique)** - 
> - **Undersampling Majority Class**
> - **Class Weighting** - Assign a weight to each class _e.g Majority class = 1, Minority class = #Majority class sample/#Minority class sample_
> - Using the approprate metric such as the _F1 Score_ and _PR-AUC_ which focus on minority class performance 



#### Ensemble & Advanced ML
1. Describe how a Random Forest works* #mediumDS100 
> A random Forest trains and aggregates multiple decision trees on different bootstrapped samples of the data (and with random subsets of features).
>
> Predictions are then averaged (for regression) or majority voted (for classification)

2. What is Gradient Boosting, and how is it different from Bagging? #mediumDS100 
> - **Bagging:** Trains models in parallel on bootstrapped samples: aggregates predictions
> - **Gradient Boosting:** Trains model in an additive, sequential manner, each new model correcting the errors of the previous enseble

3. What are hyperparameters, and how do you typically tune them? #mediumDS100 
> Hyperparameters are setting external to the model parameters (e.g. learning rate, max-depth)
>
> Tuning can be done via **GridSearchCV**, **RandomizedSearchCV**, **Bayesian Optimization**

#### Deep Learning
1. Explain the concept of backpropagation? #mediumDS100 
> **Backpropagation** is the process of computing gradients of the loss function with respect to (w.r.t) the networks's weights by applying the
> chain rule in a reverse pass, allowing weight updates that minimize the loss.

2. How do you approach transfer learning in deep learning? #mediumDS100 
> Typically **fine tune** a model (e.g. a pretrained CNN on ImageNet) on a custom specific dataset. Freeze early layers (to retain generic features)
> and retrain later layers on new data.

3. What is the Transformer Architecture, and why did it become popular for NLP tasks? #hardDS100
> **Self-Attention Mechanism** that allows the a model to capture global dependencies without recurrence or convolution
> 
> Scales well to large datasets due to ability to parallize and has achieved state of the art results in many NLP tasks

#### Retrieval-Augemented Generation (RAG)
1. What is Retrieval-Augmented Generation, and why might it be preferable to the standard LLM approach? #easyDS100
> RAG involves retrieving knowledge that is external to a model i.e not part of the model corpus (e.g. custom document, context) and feeding it
into an LLM to generate answers that are grounded in up-to-date or domain/context-specific information/data
>
> It reduces hallucinations, ensures answers are based on actual up-to-date data rather than purely on model "memory" and allows us to update its knowledge
> without fully retraining a large model

2. How do you typically store and retrieve documents in a RAG pipeline? #mediumDS100
> - **Storage:** Documents can be stored in a vector db such as Chroma, Milvus, Faiss, Pinecone Qdrant or an indexed system
> - **Retrieval:** Steps involve _creating embeddings_ (transforming text into vectors) and then querying the vector store with a user query (also transformed
> into a vector). The database returns the _top-k_ semantically relevant chunks, which are then provided as context to the LLM

3. How do you mitigate hallucinations in a Retrieval-Augmented Generation system? #mediumDS100
> - Using a reliable retrieval layer with high-quality embeddings and properly chunked documents.
> - Employ **prompt templates** that explicitly instruct the model to use only provided context.
> - Implement **verification step** such as cross checking the LLM's asnwer against the source document, or using chain of thought approach that references retrieved
> text

#### Business & Product Sense
1. Explain a project where you had to balance technical accuracy with business requirements. #easyDS100 
> Understanding the business impact of difference accuracy levels. In some cases, a simpler model with faster inference might be better
> if it meets the business's performance threshold
>
>> Alteranive
>
> Building model that could accurately predict students who were at risk of dropping out academically or giving low nps
> vs Identifying what was the primary cause of students dropping out. It wasn't academic nor because of student experience
>
> Reason was due to cost of the course and time demand. Main metric being optimized was for maximum revenue capture. Alternate automations helped track this.
> Dashboard of academic vs non-academic drop offs

2. How do you choose the right evaluation metric for a business problem? #mediumDS100 
> Focus on use-case and business value. If false positives are costly, optimize precision, if false negatives are risky, optimize recall for example.
> 
> For ranking problems me can use _NDCG_ or _MAP_.
>> - **Normalized Discounted Cumulative Gain (NDCG):** - A ranking quality metric used in information retreival to measure effectiveness of search engines, recommomendation
>> systems and other ranking algorithms. It evaluates ranking quality by taking into account both a relevant item's position and its importance/position
>>
>> - **Mean Average Position (MAP):** It considers the number of relevant recommendations and their position in the list
>
> Alway tying back to ROI or user satisfaction.

>> Alternative
>
> For profit making organizations its main metrics are around driving/increasing profits/revenue, reducing expenses
>
> For NGOs it maybe quantity of impact i.e. how many people have we served, or quality of impact. How different is it for people (Increase in standard of living)  


3. Walk me through how you'd design a recommendation system for an e-commerce site #mediumDS100 
> - Outline data source ( user behaviour, item metadata)
> - Consider collaborative filtering + content-based filtering
> - Decide on offline vs real-time serving. Evaluate via user engagement metrics or CTR (click through rate)

#### Behavioral & Team Fit
1. Tell me about a challenging data science problem you faced and how you solved it. #easyDS100 
> Influencing a study on Graduate Salary progression that involved multiple teams internally and externally
>
> - Current data has a lot of missing data. Whichever way the study was to be done needed to appropriately backdate existing data
> - Define appropriate null and alternative hypothesis
> - Validate findings
> - Communication of findings
> - Effective stakeholder management

## Practical

### High Frequency

#### Python & Data Wrangling

1. How do you handle missing value in a Pandas `DataFrame`? Give at least 2 approaches? #easyDS100
2. Describe how you would merge/join two data sets in Pandas? #easyDS100 

#### SQL
1. Write a query to find all employees with a salary above the average salary of their department #mediumDS100
2. How would you find the second highest (or Nth highest) value in a table? #mediumDS100 



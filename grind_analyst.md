### 1. Walk me through the steps of a typical data analysis process

1. **Define the question, goal/objective and the metric of success.** (e.g. We want to increase customer satisfaction by x%)
2. **Collect the data** (from DBs, APIs or spreadsheets)
3. **Clean and Pre-process** (handle missing values, outliers, datatypes).
4. **Explore and Visualize-EDA** (perform descriptive statistics, generate plots).
5. **Model and/or Analyze** (could be statistical tests/modeling, machine learning models or dashboards)
6. **Intepret Results** (provide insights, answer the original question)
7. **Communicate Findings** (create clear presentations or dashboard)

### 2. Difference between data analysis and data science

- **Data Analysis** - Focuses on understanding historical data to gather straight forward insights from patterns discovered in the data. (e.g business reporting, BI dashboard)
- **Data Science** - Overlaps with Data Analysis, however focuses more building predictive models, experimenting with complex algorithms. Data science extends to machine learning
and more advanced statistics and engineering components. Building out or using algorithms that try to uncover patterns and insights within the data by them selves

### 3. How do you handle missing or corrupted data in a dataset

- Indentify the pattern of missingness (random vs non-random)
- Decide wether to retain or drop the row/columns with missing data depending on amount of missing data or value to the analysis.
- Imputation statergies or techniques i.e using mean, mode or predictive methods for more sophisticated approaches
- Document decisions to ensure transparency

### 4. Explain the concept of outliers and how best to detect them and deal with them

- **Definition**: Data points that deviate significantly from majority of the data
- **Detection**: Box plots(Interquartile Range IQR rules), z-scores, or domain-specific thresholds.
- **Interventios**: Confirm if outliers are real or data error then trim, cap or transform them

### 5. How would you optimize a slow-running SQL query?

- Check indexing (ensure the right columns are indexed).
- Re-writing queries (avoid `SELECT *` for data with a lot of rows and columns, or reducing subqueries if possible)
- Analyze execution plans (look for table scans (without WHERE) vs index scans ( with >) vs index seek (with = ) ) and implement appropriate filters
- Use appropriate joins (confirm we are not using unnecessary cross joins)
- Partition large tables if relevant

### 6. What are some ways to handle dupliate records in SQL?

- Use GROUP BY or DISTINCT for identification
- Use *window functions* such as ROW_NUMBER, RANK/DENSE_RANK to tag duplicates
- Decide wether to remove or merge them based on domain logic

### 7. How do you ensure data integrity in a relation database?

- Proper contraints (unique primary keys, foreign keys, not null, specifying correct types for columns)
- Use transaction contorls (ACID - Atomicity, Consistency, Isolation, Durability)

### 8. How would you explain a complex technical concept to a non-technical stakeholder

- Simplify jargon, use analogies or visuals
- Emphasis on relevant business impact rather than raw metrics
- Ask for feedback to ensure comprehension

### 9. Describe the process of A/B testing (split testing). What metrics do you usually track?

- **Hypothesis**: Define what change might improve a metric. (Automated messaging for order-tracking to higher customer satisfaction)
- **Randomly split**: into control (A) and treatment (B) groups.
- **Run experiment** and collect relevant metric (i.e. retention rate and customer satisfaction)
- **Statistical analysis**: Check significance (confidence intervals, p-values, effect size)
- **Action**: Deploy winning variant

### 10. What is the Central Limit Theorem (CLT) and why is it important?

- **Definition**: As a sample size grows, the distribution of the sample means approximates a normal distribution, regardless of the population distribution
- **Importance**: Underpings many statistical methods, allowing confidence intervals and hypothesis tests to be valid for large samples

### 11. When would you use a _t-test_ vs an _ANOVA_ test?

- **t-test**: Compare the means of two groups (independent or paired)
- **ANOVA**: Compare the means of three or more groups simultaneously

### 12. What are the best charts to use for different data types or comparisons

- **Line Charts**: Trends over time
- **Bar Charts**: Categorical comparisons
- **Scatter plots**: Relationship between 2 variables
- **Box plots**: Distributions and outlier detection
- **Pie/Donut Charts**: Proporties (used sparingly)


#!/usr/bin/env python
# coding: utf-8

# # question 01
Q1. Explain the assumptions required to use ANOVA and provide examples of violations that could impact
the validity of the results.
ANOVA (Analysis of Variance) is a statistical method used to compare the means of three or more groups or populations. The following are the assumptions that are required to use ANOVA:

Independence: The observations in each group should be independent of each other. This means that the value of one observation should not be related to the value of another observation in the same group.

Normality: The data in each group should be normally distributed. This means that the distribution of data in each group should be bell-shaped.

Homogeneity of variance: The variance of the data in each group should be equal. This means that the spread of the data in each group should be the same.

Violations of these assumptions can impact the validity of the results. For example:

Independence: Violations of independence can occur when the observations in one group are related to the observations in another group. For example, if the same group of individuals is included in two different treatments, their responses may be correlated, violating the independence assumption.

Normality: Violations of normality can occur when the data in each group is not normally distributed. For example, if the data is skewed or has outliers, the assumption of normality may not hold.

Homogeneity of variance: Violations of homogeneity of variance can occur when the variance of the data in each group is not equal. For example, if the data in one group has a much larger variance than the data in another group, this assumption may not hold.

These violations can lead to incorrect conclusions and may invalidate the results of the ANOVA. It is important to check for these assumptions and, if necessary, take appropriate corrective action before conducting the ANOVA.
# # question 02
Q2. What are the three types of ANOVA, and in what situations would each be used?
The three types of ANOVA are:

One-way ANOVA: This is used when comparing the means of three or more groups that are independent of each other. It is called one-way because there is only one independent variable or factor being studied. For example, a one-way ANOVA could be used to compare the mean scores of students from different schools.

Two-way ANOVA: This is used when comparing the means of three or more groups that are classified based on two different independent variables or factors. It is called two-way because there are two independent variables being studied. For example, a two-way ANOVA could be used to compare the mean scores of students from different schools based on their gender and the type of teaching method used.

Repeated measures ANOVA: This is used when comparing the means of three or more groups that are dependent on each other, such as measuring the same group of individuals over time or under different conditions. For example, a repeated measures ANOVA could be used to compare the mean scores of students before and after a teaching intervention.

The choice of ANOVA depends on the research question and the design of the study. One-way ANOVA is appropriate when there is only one independent variable being studied, while two-way ANOVA is appropriate when there are two independent variables being studied. Repeated measures ANOVA is appropriate when measuring the same group of individuals over time or under different conditions.
# # question 03
What is the partitioning of variance in ANOVA, and why is it important to understand this concept?
Partitioning of variance is the process of dividing the total variability in the data into different sources of variation in ANOVA. The variance is partitioned into two components: the variation between groups and the variation within groups.

Understanding the partitioning of variance is important in ANOVA because it allows us to determine the proportion of variability in the data that is due to differences between groups and the proportion that is due to random error or variation within groups. This helps us to evaluate the significance of the group differences and make inferences about the population means.

Moreover, the partitioning of variance also helps us to calculate the F statistic, which is the ratio of the between-group variance to the within-group variance. The F statistic is used to test the null hypothesis that there is no significant difference between the means of the groups, and a larger F value indicates a stronger evidence against the null hypothesis.

Overall, understanding the partitioning of variance is crucial in ANOVA for accurately interpreting the results and making informed decisions.




# # question 04
Q4. How would you calculate the total sum of squares (SST), explained sum of squares (SSE), and residual
sum of squares (SSR) in a one-way ANOVA using Python?
# In[1]:


import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load data
data = pd.read_csv('data.csv')

# Fit one-way ANOVA model
model = ols('outcome ~ group', data=data).fit()

# Calculate total sum of squares (SST)
SST = sum((data['outcome'] - data['outcome'].mean())**2)

# Calculate explained sum of squares (SSE)
SSE = sum((model.fittedvalues - data['outcome'].mean())**2)

# Calculate residual sum of squares (SSR)
SSR = SST - SSE


# # question 05
Q5. In a two-way ANOVA, how would you calculate the main effects and interaction effects using Python?
In a two-way ANOVA, the main effects and interaction effects can be calculated using Python by fitting a linear regression model and analyzing the results.

To calculate the main effects, separate linear regression models can be fitted for each factor (or independent variable) separately. For example, if we have two factors A and B, we can fit two separate models, one with only A and one with only B, and calculate the sum of squared errors (SSE) for each model. The main effect of A is then calculated as the difference between the SSE of the model with only A and the SSE of the full model with both A and B. Similarly, the main effect of B is calculated as the difference between the SSE of the model with only B and the SSE of the full model.

To calculate the interaction effect, the full model with both factors A and B is fitted, and the SSE is calculated. The interaction effect is then calculated as the difference between the SSE of the full model and the sum of the SSEs of the two separate models with only A and only B.

Python libraries such as statsmodels and scikit-learn provide functions for fitting linear regression models and calculating the main effects and interaction effects in a two-way ANOVA.
# # question 06
Suppose you conducted a one-way ANOVA and obtained an F-statistic of 5.23 and a p-value of 0.02.
What can you conclude about the differences between the groups, and how would you interpret these
results?
A one-way ANOVA with a p-value of 0.02 and an F-statistic of 5.23 suggests that there is a statistically significant difference between the means of at least two groups. In other words, there is evidence to suggest that not all of the groups have the same mean. However, the F-test does not tell us which specific groups are different from one another.

The p-value of 0.02 indicates that there is a 2% chance of observing such a large F-statistic if the null hypothesis were true (i.e., if all the group means were equal). Since the p-value is less than the significance level of 0.05, we can reject the null hypothesis and conclude that there is a statistically significant difference between the means of at least two groups.

In summary, based on the results of the one-way ANOVA, we can conclude that there is strong evidence to suggest that there are differences between the means of the groups being compared.
# # question 07
In a repeated measures ANOVA, how would you handle missing data, and what are the potential
consequences of using different methods to handle missing data?
Handling missing data in repeated measures ANOVA can be a challenging issue, and there are several ways to approach it. Here are some common methods:

Pairwise deletion: This method involves removing any observation with missing data from the analysis. While this approach is easy to implement, it can result in biased estimates of the means and standard errors, especially if the missing data are not missing completely at random.

Listwise deletion: This method involves removing any participant with missing data from the analysis. While this approach results in unbiased estimates, it can lead to a loss of statistical power, especially if there are many missing values.

Mean imputation: This method involves replacing missing values with the mean of the available observations for that variable. While this approach is easy to implement, it can lead to biased estimates of the means and standard errors.

Maximum likelihood estimation: This method involves estimating the missing data values based on the observed data and a model of the data generating process. This approach can provide unbiased estimates if the missing data are missing at random or missing completely at random.

The potential consequences of using different methods to handle missing data in repeated measures ANOVA include biased estimates of means, standard errors, and statistical significance, as well as a loss of statistical power. It is important to carefully consider the nature and pattern of the missing data and choose a method that is appropriate for the research question and the data at hand.
# # question 08
What are some common post-hoc tests used after ANOVA, and when would you use each one? Provide
an example of a situation where a post-hoc test might be necessary.
Post-hoc tests are used after conducting an ANOVA to identify which specific groups differ significantly from each other. There are several post-hoc tests available, and the choice of which one to use depends on the specific research question and the design of the study. Some common post-hoc tests include:

Tukey's HSD (Honestly Significant Difference) Test: This test is used when there are equal sample sizes in each group. It is considered one of the most conservative tests and controls the overall Type I error rate.

Bonferroni Test: This test is used when there are unequal sample sizes in each group. It is also conservative, but it can be more powerful than Tukey's HSD test when the number of groups is small.

Scheffe's Test: This test is used when there are multiple comparisons and no assumptions are made about the variances of the groups. It is more powerful than the Bonferroni test but can be less powerful than Tukey's HSD test.

Games-Howell Test: This test is used when there are unequal variances between the groups. It is less conservative than Tukey's HSD test but more powerful than the Bonferroni test.

Post-hoc tests are necessary when the overall F-test in the ANOVA is significant, indicating that at least one group differs from the others. For example, suppose a researcher conducted a study to compare the effects of three different treatments on a specific outcome. After conducting an ANOVA, the researcher found a significant overall effect. They would then need to conduct post-hoc tests to determine which specific treatment(s) differed significantly from the others.
# # question 09
A researcher wants to compare the mean weight loss of three diets: A, B, and C. They collect data from
50 participants who were randomly assigned to one of the diets. Conduct a one-way ANOVA using Python
to determine if there are any significant differences between the mean weight loss of the three diets.
Report the F-statistic and p-value, and interpret the results.
# In[2]:


import scipy.stats as stats

# Sample data for each diet group
diet_a = [5, 6, 8, 4, 7, 6, 5, 8, 7, 6, 4, 9, 5, 6, 8, 4, 7, 6, 5, 8, 7, 6, 4, 9, 5, 6, 8, 4, 7, 6]
diet_b = [6, 7, 9, 5, 8, 7, 6, 9, 8, 7, 5, 10, 6, 7, 9, 5, 8, 7, 6, 9, 8, 7, 5, 10, 6, 7, 9, 5, 8, 7]
diet_c = [7, 8, 10, 6, 9, 8, 7, 10, 9, 8, 6, 11, 7, 8, 10, 6, 9, 8, 7, 10, 9, 8, 6, 11, 7, 8, 10, 6, 9, 8]

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(diet_a, diet_b, diet_c)

# Print results
print("F-statistic: ", f_statistic)
print("p-value: ", p_value)


# # question 10
Q10. A company wants to know if there are any significant differences in the average time it takes to
complete a task using three different software programs: Program A, Program B, and Program C. They
randomly assign 30 employees to one of the programs and record the time it takes each employee to
complete the task. Conduct a two-way ANOVA using Python to determine if there are any main effects or
interaction effects between the software programs and employee experience level (novice vs.
experienced). Report the F-statistics and p-values, and interpret the results.
# In[3]:


import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load data
data = pd.read_csv("task_times.csv")

# Conduct two-way ANOVA
model = ols('Completion_Time ~ C(Software_Program) + C(Experience_Level) + C(Software_Program):C(Experience_Level)', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Print ANOVA table
print(anova_table)


# # question 11
Q11. An educational researcher is interested in whether a new teaching method improves student test
scores. They randomly assign 100 students to either the control group (traditional teaching method) or the
experimental group (new teaching method) and administer a test at the end of the semester. Conduct a
two-sample t-test using Python to determine if there are any significant differences in test scores
between the two groups. If the results are significant, follow up with a post-hoc test to determine which
group(s) differ significantly from each other.
# In[5]:


import pandas as pd
from scipy.stats import ttest_ind

# Load data
data = pd.read_csv("test_scores.csv")

# Split data into control and experimental groups
control = data[data["Group"] == "control"]["Test_Score"]
experimental = data[data["Group"] == "experimental"]["Test_Score"]

# Conduct two-sample t-test
t_stat, p_val = ttest_ind(control, experimental)

# Print results
print("t-statistic:", t_stat)
print("p-value:", p_val)


# In[6]:


from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Conduct Tukey HSD test
tukey_results = pairwise_tukeyhsd(data["Test_Score"], data["Group"], alpha=0.05)

# Print results
print(tukey_results)


# # question 12
Q12. A researcher wants to know if there are any significant differences in the average daily sales of three
retail stores: Store A, Store B, and Store C. They randomly select 30 days and record the sales for each store
on those days. Conduct a repeated measures ANOVA using Python to determine if there are any

significant differences in sales between the three stores. If the results are significant, follow up with a post-
hoc test to determine which store(s) differ significantly from each other.
# In[7]:


import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
data = {'Store': ['A']*30 + ['B']*30 + ['C']*30,
        'Day': list(range(1,31))*3,
        'Sales': [10, 12, 14, 13, 11, 15, 17, 18, 19, 16, 20, 22, 25, 24, 26, 28, 30, 29, 27, 23, 21, 20, 18, 16, 14, 12, 10, 9, 8, 7]*3}
df = pd.DataFrame(data)
model = ols('Sales ~ C(Store) + C(Day) + C(Store):C(Day)', data=df).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
print(aov_table)


# In[ ]:





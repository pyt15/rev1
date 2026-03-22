# ============================================================
# TWO MARKS – ANSWERS
# ============================================================

# ============================================================
# Unit I – Data Types and Operators
# ============================================================

# Q1. What are arithmetic operators in Python? Give two examples.
# Arithmetic operators perform mathematical operations on numeric values.
# Examples: + (addition) e.g. 3+2=5, ** (exponentiation) e.g. 2**3=8.

# Q2. What is a string in Python?
# A string is a sequence of characters enclosed in single or double quotes.
# Example: name = "Python" — strings are immutable in Python.

# Q3. What are integer data types in Python? Give an example.
# Integers are whole numbers without a decimal point, positive or negative.
# Example: x = 42 or y = -7 — stored using the built-in int type.

# Q4. What are comparison (relational) operators? Give two examples.
# Comparison operators compare two values and return a Boolean (True/False).
# Examples: == (equal to) e.g. 5==5 → True, > (greater than) e.g. 7>3 → True.

# Q5. What is the purpose of logical operators in Python?
# Logical operators combine multiple conditions and return True or False.
# The three logical operators are: and, or, and not.

# Q6. What are assignment operators in Python?
# Assignment operators assign or update the value of a variable.
# Examples: = (assign), += (add and assign), -= (subtract and assign).

# Q7. What is the difference between identity operators and membership operators?
# Identity operators (is, is not) check if two variables point to the same object.
# Membership operators (in, not in) check if a value exists within a sequence.

# Q8. What is a Boolean data type?
# Boolean is a data type with only two values: True or False.
# It is used in conditions and logical expressions, e.g. result = (5 > 3) → True.

# Q9. What is a Python expression?
# An expression is a combination of values, variables, and operators that evaluates to a result.
# Example: 2 + 3 * 4 is an expression that evaluates to 14.

# Q10. What are list operations?
# List operations include append, remove, sort, reverse, insert, pop, and extend.
# Example: lst = [1,2,3]; lst.append(4) adds 4 to the end of the list.

# Q11. What is list slicing? Give an example.
# List slicing extracts a portion of a list using the syntax list[start:stop:step].
# Example: lst = [10,20,30,40,50]; lst[1:4] → [20, 30, 40].

# Q12. Differentiate between a list and a tuple.
# A list is mutable (can be changed after creation) and uses square brackets [ ].
# A tuple is immutable (cannot be changed after creation) and uses parentheses ( ).

# Q13. What is a tuple in Python?
# A tuple is an ordered, immutable collection of elements enclosed in parentheses.
# Example: t = (1, 2, 3) — elements cannot be added, removed, or changed.

# Q14. What is a set in Python?
# A set is an unordered collection of unique elements enclosed in curly braces { }.
# Example: s = {1, 2, 3, 2} → {1, 2, 3} — duplicates are automatically removed.

# Q15. What is a dictionary in Python?
# A dictionary stores data as key-value pairs enclosed in curly braces { }.
# Example: d = {"name": "Alice", "age": 20} — values are accessed via keys.

# Q16. What are bitwise operators?
# Bitwise operators perform operations on the binary representations of integers.
# Examples: & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift).

# Q17. How do membership operators work in Python?
# The 'in' operator returns True if a value is found in a sequence, False otherwise.
# The 'not in' operator returns True if the value is NOT present in the sequence.

# Q18. What are the common methods used with lists?
# Common list methods: append(), insert(), remove(), pop(), sort(), reverse(), index().
# Example: lst.sort() sorts the list in ascending order in place.

# Q19. What is the difference between mutable and immutable data types in Python?
# Mutable types (list, dict, set) can be changed after creation.
# Immutable types (int, str, tuple) cannot be changed once created.

# Q20. How are elements accessed in a dictionary?
# Dictionary elements are accessed using their key inside square brackets: dict[key].
# Example: d = {"age": 21}; print(d["age"]) → 21. Use get() to avoid KeyError.


# ============================================================
# Unit II – Conditional Statements, Looping and Functions
# ============================================================

# Q1. Write the syntax of the if statement in Python.
# Syntax: if condition:
#             statement(s)
# The block executes only when the condition evaluates to True.

# Q2. What is the purpose of the else block in conditional statements?
# The else block executes when the if condition is False.
# It provides an alternative action when none of the preceding conditions are met.

# Q3. What is an elif statement used for?
# elif (else-if) checks another condition when the previous if/elif was False.
# It allows multiple mutually exclusive conditions to be checked in sequence.

# Q4. Differentiate between for loop and while loop.
# A for loop iterates over a sequence for a known number of times.
# A while loop repeats as long as a given condition remains True.

# Q5. What is a loop in Python?
# A loop is a control structure that repeats a block of code multiple times.
# Python provides two loop types: for (definite) and while (indefinite).

# Q6. Name the looping statements used in Python.
# Python has two looping statements: for loop and while loop.
# Loop control is managed with break, continue, and pass statements.

# Q7. What is the use of the break statement?
# break immediately terminates the nearest enclosing loop.
# Execution continues with the first statement after the loop.

# Q8. What does the continue statement do in a loop?
# continue skips the remaining statements in the current iteration.
# The loop then moves on to the next iteration without terminating.

# Q9. What is the purpose of the pass statement?
# pass is a null statement used as a placeholder where syntax requires a statement.
# It does nothing and allows the program to continue without error.

# Q10. What is the use of else with loops?
# The else block after a loop executes when the loop completes normally (no break).
# If the loop is terminated by break, the else block is skipped.

# Q11. What is meant by loop control statements?
# Loop control statements change the normal execution flow of a loop.
# Python provides three: break (exit), continue (skip iteration), pass (do nothing).

# Q12. What is a function in Python?
# A function is a reusable, named block of code that performs a specific task.
# It is defined using the def keyword and called by its name with parentheses.

# Q13. Write the syntax for defining a function in Python.
# Syntax: def function_name(parameters):
#             statement(s)
# Use return to send a value back to the caller.

# Q14. What is meant by calling a function?
# Calling a function means invoking it to execute its block of code.
# Example: result = my_function(5) calls my_function with argument 5.

# Q15. What is the difference between global and local variables?
# A local variable is defined inside a function and accessible only within it.
# A global variable is defined outside all functions and accessible throughout the program.

# Q16. What is the scope of a local variable?
# A local variable's scope is limited to the function in which it is defined.
# It is created when the function is called and destroyed when the function returns.

# Q17. What is PIP in Python?
# PIP (Pip Installs Packages) is the standard package manager for Python.
# It allows users to install, upgrade, and remove third-party packages easily.

# Q18. Why is PIP used in Python programming?
# PIP simplifies the installation of external libraries not included in the standard library.
# Example: pip install numpy downloads and installs the NumPy package automatically.

# Q19. How are packages installed using PIP?
# Run: pip install package_name in the terminal or command prompt.
# Example: pip install pandas installs the Pandas library for data analysis.

# Q20. What are the advantages of using functions in Python?
# Functions promote code reusability, modularity, and readability.
# They reduce code duplication and make debugging and maintenance easier.


# ============================================================
# Unit III – NumPy, Pandas and Matplotlib
# ============================================================

# Q1. What is NumPy and why is it used in Python?
# NumPy is a library for numerical computing that provides support for arrays and matrices.
# It is used for fast mathematical operations on large datasets efficiently.

# Q2. Mention any two features of NumPy.
# NumPy provides N-dimensional array objects (ndarray) for efficient storage.
# It offers built-in mathematical functions like mean, std, dot product, and FFT.

# Q3. What is an array in NumPy?
# A NumPy array is a grid of values of the same data type stored in contiguous memory.
# Created using np.array([1,2,3]) — it supports vectorized operations without loops.

# Q4. What is Pandas used for in data analysis?
# Pandas is used for data manipulation, cleaning, and analysis using tabular structures.
# It provides Series and DataFrame objects to work with structured/labelled data.

# Q5. Define a DataFrame in Pandas.
# A DataFrame is a 2-dimensional labelled data structure with rows and columns.
# It resembles a spreadsheet or SQL table and is the primary Pandas data structure.

# Q6. What is the purpose of the describe() function in Pandas?
# describe() generates descriptive statistics (count, mean, std, min, max, quartiles).
# It provides a quick summary of the numerical columns in a DataFrame.

# Q7. What is the difference between loc and iloc in Pandas?
# loc selects data by label (row/column names), e.g. df.loc["row1", "col1"].
# iloc selects data by integer position (index), e.g. df.iloc[0, 1].

# Q8. What is the use of iloc in Pandas?
# iloc is used for integer-location based indexing to select rows and columns by position.
# Example: df.iloc[0:3, 1:4] selects the first 3 rows and columns at positions 1–3.

# Q9. What is the purpose of Matplotlib?
# Matplotlib is a Python plotting library used to create static, animated, and interactive graphs.
# It enables visualization of data through charts like line, bar, scatter, and histogram.

# Q10. What is the purpose of plt.show() in Matplotlib?
# plt.show() renders and displays all currently open figures to the screen.
# Without it, the plot may not be visible, especially in script (non-notebook) environments.

# Q11. Write the syntax to create a line plot using Matplotlib.
# import matplotlib.pyplot as plt
# plt.plot(x, y); plt.show()

# Q12. Write the syntax to create a scatter plot using Matplotlib.
# import matplotlib.pyplot as plt
# plt.scatter(x, y); plt.show()

# Q13. When is a bar plot used?
# A bar plot is used to compare discrete categories or groups using rectangular bars.
# The height of each bar represents the value or frequency of that category.

# Q14. What is a boxplot used for in data visualization?
# A boxplot displays the distribution of data through its quartiles and outliers.
# It shows the median, IQR (Q1–Q3), and any extreme values visually.

# Q15. What information does a histogram display?
# A histogram displays the frequency distribution of a continuous variable using bins.
# It shows how data is spread across intervals or ranges.

# Q16. What is a scatter plot used for?
# A scatter plot shows the relationship or correlation between two continuous variables.
# Each point represents one observation's values on the x and y axes.

# Q17. What is a line plot commonly used to represent?
# A line plot is commonly used to show trends or changes in data over time.
# It connects data points with a line to highlight direction and continuity.

# Q18. What is meant by formatting charts in Matplotlib?
# Formatting charts means adding titles, axis labels, legends, colors, and grid lines.
# Functions like plt.title(), plt.xlabel(), plt.legend() are used for formatting.

# Q19. What types of plots can be created using Matplotlib? Name any two.
# Matplotlib can create many plot types including line plots and bar charts.
# Other types include histograms, scatter plots, pie charts, and boxplots.

# Q20. How does Pandas help in handling structured datasets?
# Pandas provides DataFrame and Series to load, filter, group, and summarise tabular data.
# It supports reading from CSV, Excel, SQL, and JSON files with a single function call.


# ============================================================
# Unit IV – Descriptive Statistics
# ============================================================

# Q1. What are the different types of data in statistics?
# Data is classified as qualitative (categorical) and quantitative (numerical).
# Quantitative data is further divided into discrete and continuous types.

# Q2. What is nominal data?
# Nominal data represents categories with no natural order or ranking.
# Examples: gender (Male/Female), eye colour, and country names.

# Q3. What is ordinal data?
# Ordinal data has categories with a meaningful order but unequal intervals.
# Examples: satisfaction ratings (Poor/Good/Excellent) and education levels.

# Q4. What is the difference between ratio scale and interval scale?
# Interval scale has equal intervals but no true zero (e.g. temperature in °C).
# Ratio scale has equal intervals AND a true zero (e.g. height, weight, income).

# Q5. Define mean in statistics.
# Mean is the arithmetic average, calculated by dividing the sum by the count.
# Formula: Mean = Σx / n — sensitive to extreme values (outliers).

# Q6. What is median?
# Median is the middle value when data is arranged in ascending or descending order.
# For even-sized data, it is the average of the two middle values.

# Q7. What is mode?
# Mode is the value that appears most frequently in a dataset.
# A dataset can be unimodal, bimodal, or multimodal depending on frequency peaks.

# Q8. Define mean, median, and mode collectively.
# Mean, median, and mode are collectively called measures of central tendency.
# They describe the centre or typical value of a dataset.

# Q9. What is the purpose of a bar chart?
# A bar chart visually compares different categories using rectangular bars.
# The length of each bar is proportional to the value it represents.

# Q10. When is a pie chart used?
# A pie chart is used to show the proportional distribution of a whole into parts.
# It is most effective when there are a small number of categories (≤ 5–6).

# Q11. What is a box plot used to represent?
# A box plot represents the five-number summary: min, Q1, median, Q3, and max.
# It also displays outliers and helps compare distributions across groups.

# Q12. What is range in statistics?
# Range is the difference between the maximum and minimum values in a dataset.
# Formula: Range = Maximum – Minimum — it is the simplest measure of spread.

# Q13. What is interquartile range (IQR)?
# IQR is the range of the middle 50% of data, from Q1 (25th) to Q3 (75th percentile).
# Formula: IQR = Q3 – Q1 — it is resistant to outliers unlike the full range.

# Q14. What is standard deviation?
# Standard deviation measures how much values deviate from the mean on average.
# A low SD means data is clustered near the mean; a high SD means it is spread out.

# Q15. What is skewness?
# Skewness measures the asymmetry of a distribution around its mean.
# Positive skew: tail on right; Negative skew: tail on left; Zero: symmetric.

# Q16. What is kurtosis?
# Kurtosis measures the sharpness of the peak and heaviness of the tails of a distribution.
# Leptokurtic (>3): sharp peak; Platykurtic (<3): flat peak; Mesokurtic (=3): normal.

# Q17. What does a histogram represent?
# A histogram represents the frequency distribution of continuous numerical data.
# The x-axis shows data intervals (bins) and the y-axis shows frequency counts.

# Q18. What is meant by measures of variability?
# Measures of variability describe how spread out or dispersed data values are.
# Common measures: range, variance, standard deviation, and IQR.

# Q19. Why are measures of central tendency important?
# They summarise an entire dataset with a single representative value.
# They help in comparing datasets and understanding overall data behaviour.

# Q20. What does skewness indicate about a dataset?
# Skewness indicates the direction and degree of asymmetry in a distribution.
# It helps identify whether data has a longer tail on the left or right side.


# ============================================================
# Unit V – Statistical Inference and Hypothesis Testing
# ============================================================

# Q1. What is a population in statistics?
# A population is the complete set of all individuals or items of interest in a study.
# Example: all students in a university, or all products in a factory.

# Q2. What is a sample in statistics?
# A sample is a subset of the population selected for analysis and study.
# It should be representative of the population to yield valid conclusions.

# Q3. Differentiate between population and sample.
# A population includes all members of a defined group; it is large and often impractical.
# A sample is a smaller, manageable subset drawn from the population for study.

# Q4. What is hypothesis testing?
# Hypothesis testing is a statistical method to decide whether a claim about a population is valid.
# It uses sample data to accept or reject the null hypothesis based on a significance level.

# Q5. What is a null hypothesis (H₀)?
# The null hypothesis (H₀) states that there is no significant effect or difference.
# It is the default assumption that is tested and either rejected or not rejected.

# Q6. What is an alternative hypothesis (H₁)?
# The alternative hypothesis (H₁) states that there is a significant effect or difference.
# It is accepted when the null hypothesis is rejected based on evidence from sample data.

# Q7. What is the level of significance in hypothesis testing?
# The level of significance (α) is the probability threshold for rejecting the null hypothesis.
# Commonly set at 0.05 (5%), meaning a 5% risk of incorrectly rejecting H₀.

# Q8. What is a Type I error?
# A Type I error (false positive) occurs when H₀ is rejected even though it is true.
# Its probability is equal to the significance level α (e.g. 0.05).

# Q9. What is a Type II error?
# A Type II error (false negative) occurs when H₀ is not rejected even though it is false.
# Its probability is denoted by β; minimising it increases the power of the test.

# Q10. What decision is made if p-value < level of significance?
# If p-value < α, we reject the null hypothesis (H₀).
# This indicates the result is statistically significant.

# Q11. What decision is made if p-value > level of significance?
# If p-value > α, we fail to reject (accept) the null hypothesis (H₀).
# This indicates there is insufficient evidence to support the alternative hypothesis.

# Q12. What is a one-sample t-test used for?
# A one-sample t-test compares the mean of a single sample to a known population mean.
# Example: testing whether the average alcohol content differs from 10%.

# Q13. When is a paired sample t-test used?
# A paired t-test is used when the same subjects are measured twice (before and after).
# It tests whether the mean difference between paired observations is significantly zero.

# Q14. What is an independent samples t-test?
# An independent samples t-test compares the means of two unrelated groups.
# Example: comparing alcohol content between high-quality and low-quality wines.

# Q15. What is the purpose of one-way ANOVA?
# One-way ANOVA tests whether the means of three or more independent groups are equal.
# It compares variance between groups versus variance within groups using the F-statistic.

# Q16. What is the Chi-Square test used for?
# The Chi-Square test checks for association between two categorical variables.
# It compares observed frequencies with expected frequencies in a contingency table.

# Q17. What is a p-value in hypothesis testing?
# A p-value is the probability of obtaining results as extreme as observed, assuming H₀ is true.
# A small p-value (< α) indicates strong evidence against the null hypothesis.

# Q18. What is statistical inference?
# Statistical inference is the process of drawing conclusions about a population from sample data.
# It includes estimation (confidence intervals) and hypothesis testing.

# Q19. What is the importance of sampling in statistics?
# Sampling allows analysis of a large population without studying every member.
# A good sample saves time, cost, and resources while still providing accurate estimates.

# Q20. Why are hypothesis tests used in data analysis?
# Hypothesis tests help determine whether observed patterns in data are statistically significant.
# They prevent incorrect conclusions by providing a probability-based decision framework.

# ============================================================
# Unit 1
# ============================================================

# 1) Greet user by name
name = input("Enter your name")
print("Hello", name + "!")

# 2) Print the sum of two numbers
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
print("Sum=", a + b)

# 3) Area of rectangle
Length = float(input("Enter the length:"))
Breadth = float(input("Enter the breadth:"))
print("Area=", Length * Breadth)

# 4) Check age >= or < 18
age = int(input("Enter the age:"))
print(age >= 18)

# 5) Arithmetic operators
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# 6) Logical (comparison) operators
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print("a == b:", a == b)
print("a != b:", a != b)

# 7) Assignment operators
x = 10  # initialise x before using compound operators
x += 5
print("After += :", x)
x -= 3
print("After -= :", x)
x *= 2
print("After *= :", x)
x /= 4
print("After /= :", x)

# 8) Input age and nationality; check age >= 18 AND nationality "Indian"
age = int(input("Enter age: "))
nationality = input("Enter nationality: ")
print(age >= 18 and nationality == "Indian")

x = 5
y = 3
print("x & y:", x & y)
print("x | y:", x | y)
print("x ^ y:", x ^ y)
print("x << 1:", x << 1)
print("y >> 1:", y >> 1)

# 9) Bitwise AND and OR of two integers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("a & b:", a & b)
print("a | b:", a | b)

# 10) Check whether "python" exists in a list
lst = ["java", "python", "c"]
print("python" in lst)

# 11) Compare two lists using 'is' and '=='
A = [1, 2, 3]
B = [1, 2, 3]
print("A is B:", A is B)
print("A == B:", A == B)

# 12) Simple Interest
P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))
SI = P * R * T / 100
print("Simple Interest:", SI)

# 13) List of 5 countries – print first and last
countries = ["India", "France", "USA", "Uk", "Japan"]
print(countries[0])
print(countries[-1])

numbers = [10, 20, 30, 40, 50, 60, 70]
print("Sum =", sum(numbers))

# 14) Ask user for 8 numbers; print first 3 and last 3 using slicing
nums = []
for i in range(1, 9):
    nums.append(int(input(f"Enter number {i}: ")))
print("First 3:", nums[:3])
print("Last 3:", nums[-3:])

# 15) Append 3 student names to an empty list
students = []
students.append(input("Enter student 1: "))
students.append(input("Enter student 2: "))
students.append(input("Enter student 3: "))
print(students)

# 16) Append squares of 4, 5, 6 to [1,2,3]
lst = [1, 2, 3]
lst.append(4 ** 2)
lst.append(5 ** 2)
lst.append(6 ** 2)
print(lst)

# 17) Take 5 numbers; insert 100 in the middle (3rd position)
nums = []
for i in range(1, 6):
    nums.append(int(input(f"Enter number {i}: ")))
nums.insert(2, 100)
print(nums)

# 18) Take 6 numbers and sort in descending order
nums = []
for i in range(1, 7):
    nums.append(int(input(f"Enter number {i}: ")))
nums.sort(reverse=True)
print(nums)

# 19) Reverse the list of weekdays
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
days.reverse()
print(days)

# 20) Convert list to tuple
lst = [5, 10, 15, 20]
tpl = tuple(lst)
print(tpl)

# 21) Print last three elements of a tuple
tpl = (10, 20, 30, 40, 50)
print(tpl[-3:])

# 22) Set operations: union, intersection, difference, symmetric difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# 23) Take 5 student names and marks; store in a dictionary
students = {}
for i in range(1, 6):
    name = input(f"Enter student name {i}: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
print(students)

# 24) Update dictionary – change age to 22, add grade "A"
student = {"name": "Arjun", "age": 21, "course": "BSc"}
student["age"] = 22
student["grade"] = "A"
print(student)


# ============================================================
# Unit 2 – Control Flow
# ============================================================

# Q1. Positive, negative, or zero
num = float(input("Enter a number: "))
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

# Q2. Grade calculator
marks = float(input("Enter student marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")

# Q3. Largest of three numbers (without built-ins)
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("The largest number is:", largest)

# Q4. Leap year check
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

# Q5. Vowel or consonant
char = input("Enter a character: ").lower()
if char in 'aeiou':
    print(char, "is a Vowel")
elif char.isalpha():
    print(char, "is a Consonant")
else:
    print(char, "is not a letter")

# Q6. Multiplication table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Q7. Even numbers from 1 to 100
for i in range(2, 101, 2):
    print(i, end=" ")
print()

# Q8. Sum of all digits in a number
num = input("Enter a number: ")
total = 0
for digit in num:
    if digit.isdigit():
        total += int(digit)
print("Sum of digits:", total)

# Q9. Count uppercase letters
text = input("Enter a string: ")
count = 0
for char in text:
    if char.isupper():
        count += 1
print("Number of uppercase letters:", count)

# Q10. Star pattern
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)

# Q11. Print 1 to n using while loop
n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i, end=" ")
    i += 1
print()

# Q12. Reverse a number using while loop
num = int(input("Enter a number: "))
reverse = 0
while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number:", reverse)

# Q13. Keep asking until user enters 'stop'
while True:
    user_input = input("Enter something (type 'stop' to quit): ")
    if user_input.lower() == 'stop':
        print("You entered 'stop'. Exiting.")
        break
    print("You entered:", user_input)

# Q14. Fibonacci series up to n terms
n = int(input("Enter number of terms: "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()

# Q15. Sum all positive numbers until a negative is entered
total = 0
while True:
    num = float(input("Enter a number (negative to stop): "))
    if num < 0:
        break
    total += num
print("Sum of positive numbers:", total)

# Q16. break when number 13 is reached (1–50)
for i in range(1, 51):
    if i == 13:
        print("Stopping at 13!")
        break
    print(i, end=" ")
print()

# Q17. continue to skip multiples of 5 (1–50)
for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i, end=" ")
print()

# Q18. pass for odd numbers; print even numbers
for i in range(1, 11):
    if i % 2 != 0:
        pass  # Do nothing for odd numbers
    else:
        print("Even number:", i)

# Q19. Prime check using for-else
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "IS a prime number")
else:
    print(num, "is not a prime number")

# Q20. First number in 1–100 divisible by both 4 and 6
for i in range(1, 101):
    if i % 4 == 0 and i % 6 == 0:
        print("First number divisible by both 4 and 6:", i)
        break

# Q21. Square pattern of size n
n = int(input("Enter size of square: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# Q22. FizzBuzz (1–50)
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Q23. Classify numbers 1–20 as Even, Odd, or Prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(1, 21):
    if is_prime(i):
        print(i, "- Prime")
    elif i % 2 == 0:
        print(i, "- Even")
    else:
        print(i, "- Odd")


# ============================================================
# Unit 2 – Functions
# ============================================================

# Q1. Grocery store billing system
def calculate_total(qty, price):
    return qty * price

def apply_discount(total):
    if total >= 500:
        return total * 0.10
    elif total >= 200:
        return total * 0.05
    else:
        return 0

def display_bill(total, discount):
    print("Total Bill :", total)
    print("Discount   :", discount)
    print("Final Amount:", total - discount)

qty = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
total = calculate_total(qty, price)
discount = apply_discount(total)
display_bill(total, discount)

# Q2. Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))

# Q3. Fibonacci series using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter number of terms: "))
for i in range(terms):
    print(fibonacci(i), end=" ")
print()

# Q4. Sum, even count, max, and average of a list
numbers = [10, 25, 4, 7, 18, 3, 22]
total = 0
even_count = 0
maximum = numbers[0]
for num in numbers:
    total += num
    if num % 2 == 0:
        even_count += 1
    if num > maximum:
        maximum = num
average = total / len(numbers)
print("Sum     :", total)
print("Evens   :", even_count)
print("Maximum :", maximum)
print("Average :", average)

# Q5. 4-digit PIN authentication (max 3 attempts)
correct_pin = "1234"
attempts = 0
while attempts < 3:
    pin = input("Enter PIN: ")
    attempts += 1
    if pin == correct_pin:
        print("Access Granted!")
        break
    else:
        print("Wrong PIN.", 3 - attempts, "attempts left.")
else:
    print("Account locked!")

# Q6. Random number guessing game
import random
secret = random.randint(1, 100)
while True:
    guess = int(input("Guess the number (1-100): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! You guessed it.")
        break

# Q7. Prime check using for-else
num = int(input("Enter a number: "))
for i in range(2, num):
    if num % i == 0:
        print(num, "is NOT prime")
        break
else:
    print(num, "IS prime")

# Q8. Separate even and odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even numbers:", even)
print("Odd numbers :", odd)

# Q9. Skip multiples of 5; stop at 40
for i in range(1, 51):
    if i == 40:
        print("Stopping at 40")
        break
    if i % 5 == 0:
        continue
    print(i, end=" ")

# Q10. Right-angled triangle number pattern
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Q11. Largest and smallest elements using a function
def find_largest_smallest(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest

nums = [4, 17, 2, 9, 25, 6]
large, small = find_largest_smallest(nums)
print("Largest :", large)
print("Smallest:", small)

# Q12. Palindrome checker
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

word = input("Enter a string: ")
if is_palindrome(word):
    print(word, "is a Palindrome")
else:
    print(word, "is NOT a Palindrome")

# Q13. Reverse a number and sum its digits using while loop
num = int(input("Enter a number: "))
original = num
reverse = 0
digit_sum = 0
while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    digit_sum += digit
    num //= 10
print("Reversed Number :", reverse)
print("Sum of Digits   :", digit_sum)

# Q14. Simple banking system
balance = 0

def deposit(amount):
    global balance
    balance += amount
    print("Deposited. Balance:", balance)

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Withdrawn. Balance:", balance)

def show_balance():
    print("Balance:", balance)

while True:
    print("\n1.Deposit  2.Withdraw  3.Balance  4.Exit")
    choice = input("Choose: ")
    if choice == '1':
        deposit(float(input("Amount: ")))
    elif choice == '2':
        withdraw(float(input("Amount: ")))
    elif choice == '3':
        show_balance()
    elif choice == '4':
        print("Goodbye!")
        break

# Q15. Count positive, negative, and zero values
n = int(input("How many numbers? "))
positive = negative = zero = 0
for i in range(n):
    num = float(input("Enter number: "))
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1
print("Positive:", positive)
print("Negative:", negative)
print("Zero    :", zero)


# ============================================================
# Units 3, 4, 5 – Data Analysis (Wine Quality Dataset)
# ============================================================

print("\n Import Libraries and Read Dataset ")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Read dataset
df = pd.read_csv("/content/drive/MyDrive/Datasets/winequality.csv")
print("First five rows of the dataset:")
print(df.head())

# b) Data types and central tendency for Alcohol
print("\n Data Types and Central Tendency for Alcohol ")
print("\nDataset Data Types:")
print(df.dtypes)

mean_alcohol = df['alcohol'].mean()
median_alcohol = df['alcohol'].median()
mode_alcohol = df['alcohol'].mode()[0]
print("Mean Alcohol:", mean_alcohol)
print("Median Alcohol:", median_alcohol)
print("Mode Alcohol:", mode_alcohol)

# c) Measures of variability
print("\n Measures of Variability for Alcohol ")
range_alcohol = df['alcohol'].max() - df['alcohol'].min()
iqr_alcohol = df['alcohol'].quantile(0.75) - df['alcohol'].quantile(0.25)
std_alcohol = df['alcohol'].std()
var_alcohol = df['alcohol'].var()
print("Range:", range_alcohol)
print("Inter Quartile Range (IQR):", iqr_alcohol)
print("Standard Deviation:", std_alcohol)
print("Variance:", var_alcohol)

# d) Histogram
print("\n Histogram of Alcohol Distribution ")
plt.figure()
plt.hist(df['alcohol'], bins=20)
plt.title("Distribution of Alcohol Content")
plt.xlabel("Alcohol")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# e) Bar Plot
print("\n Bar Plot: Average Alcohol by Wine Quality ")
avg_alcohol = df.groupby('quality')['alcohol'].mean()
plt.figure()
avg_alcohol.plot(kind='bar')
plt.title("Average Alcohol Content by Wine Quality")
plt.xlabel("Wine Quality")
plt.ylabel("Average Alcohol")
plt.show()

# f) Boxplot
print("\n Boxplot: Volatile Acidity across Wine Quality ")
plt.figure()
sns.boxplot(x='quality', y='volatile acidity', data=df)
plt.title("Volatile Acidity Distribution by Wine Quality")
plt.show()

# g) Scatter Plot
print("\n Scatter Plot: Alcohol vs Wine Quality ")
plt.figure()
plt.scatter(df['alcohol'], df['quality'])
plt.title("Alcohol vs Wine Quality")
plt.xlabel("Alcohol")
plt.ylabel("Quality")
plt.show()

# h) Line Plot
print("\n Line Plot: Average Sulphates by Wine Quality ")
avg_sulphates = df.groupby('quality')['sulphates'].mean()
plt.figure()
plt.plot(avg_sulphates.index, avg_sulphates.values, marker='o')
plt.title("Average Sulphates by Wine Quality")
plt.xlabel("Wine Quality")
plt.ylabel("Average Sulphates")
plt.grid(True)
plt.show()

# i) One-Sample t-test
print("\n One-Sample t-test for Alcohol ")
t_stat, p_value = stats.ttest_1samp(df['alcohol'], 10)
print("T-statistic:", t_stat)
print("P-value:", p_value)
if p_value < 0.05:
    print("Result: Mean alcohol is significantly different from 10%")
else:
    print("Result: Mean alcohol is NOT significantly different from 10%")

# j) Independent Sample t-test
print("\n Independent Sample t-test ")
group1 = df[df['quality'] >= 6]['alcohol']
group2 = df[df['quality'] < 6]['alcohol']

# Levene's test
lev_stat, lev_p = stats.levene(group1, group2)
print("Levene Test p-value:", lev_p)
t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=(lev_p > 0.05))
print("T-statistic:", t_stat)
print("P-value:", p_value)
if p_value < 0.05:
    print("Result: Significant difference in alcohol between groups")
else:
    print("Result: No significant difference in alcohol between groups")

# k) Paired Sample t-test
print("\n Paired Sample t-test ")
df['alcohol_increased'] = df['alcohol'] * 1.10
t_stat, p_value = stats.ttest_rel(df['alcohol'], df['alcohol_increased'])
print("T-statistic:", t_stat)
print("P-value:", p_value)
if p_value < 0.05:
    print("Result: Significant difference after increasing alcohol")
else:
    print("Result: No significant difference")

# l) One-Way ANOVA
print("\n One-Way ANOVA ")
groups = [df[df['quality'] == q]['alcohol'] for q in df['quality'].unique()]
f_stat, p_value = stats.f_oneway(*groups)
print("F-statistic:", f_stat)
print("P-value:", p_value)
if p_value < 0.05:
    print("Result: Alcohol differs significantly across quality levels")
else:
    print("Result: No significant difference across quality levels")

# m) Chi-Square Test
print("\n Chi-Square Test ")
# Create alcohol categories
df['alcohol_level'] = pd.cut(df['alcohol'],
                             bins=3,
                             labels=["Low", "Medium", "High"])

# Contingency table
cont_table = pd.crosstab(df['alcohol_level'], df['quality'])
print("Contingency Table:")
print(cont_table)
chi2, p, dof, expected = stats.chi2_contingency(cont_table)
print("Chi-square value:", chi2)
print("P-value:", p)
if p < 0.05:
    print("Result: Significant association between alcohol level and wine quality")
else:
    print("Result: No significant association between alcohol level and wine quality")

# Pie chart (requires a 'Marks' column – uses a different dataset)
df['Marks'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie Chart of Marks Distribution')
plt.ylabel('')
plt.show()


# ============================================================
# Units 3, 4, 5 – Skewness, Kurtosis, KDE (Bank Dataset)
# ============================================================

# 26. Skewness of customers' age
skew_age = df['age'].skew()
print("\n Skewness of Age:", skew_age)

# 27. Skewness of account balance
skew_balance = df['balance'].skew()
print("\n Skewness of Account Balance:", skew_balance)

# 28. Kurtosis of customers' age
kurtosis_age = df['age'].kurt()
print("\n Kurtosis of Age:", kurtosis_age)

# 29. Kurtosis of account balance
kurtosis_balance = df['balance'].kurt()
print("\n Kurtosis of Account Balance:", kurtosis_balance)

# 30. Comparison of skewness and kurtosis (Age vs Balance)
print("\n Comparison of Skewness and Kurtosis")
print("   Age     -> Skewness:", skew_age, ", Kurtosis:", kurtosis_age)
print("   Balance -> Skewness:", skew_balance, ", Kurtosis:", kurtosis_balance)

# 31. KDE plot for Account Balance
print("\n Displaying KDE Plot for Account Balance")
sns.kdeplot(df['balance'])
plt.title('KDE Plot of Account Balance')
plt.xlabel('Balance')
plt.show()

# 33. KDE Plot with Different Bandwidths
print("\n Comparing KDE Plots with Different Bandwidths")
plt.figure()
sns.kdeplot(df['balance'], bw_adjust=0.5, label='bw=0.5')
sns.kdeplot(df['balance'], bw_adjust=1, label='bw=1')
sns.kdeplot(df['balance'], bw_adjust=3, label='bw=3')
plt.title('KDE of Balance with Different Bandwidths')
plt.xlabel('Balance')
plt.legend()
plt.show()

# 34. KDE Plot for Age with Mean, Median, Mode
print("\n KDE Plot for Age with Mean, Median, and Mode")
mean_age = df['age'].mean()
median_age = df['age'].median()
mode_age = df['age'].mode().iloc[0]
sns.kdeplot(df['age'])
plt.axvline(mean_age, color='red', label='Mean')
plt.axvline(median_age, color='black', label='Median')
plt.axvline(mode_age, color='green', label='Mode')
plt.title('KDE Plot of Age with Mean, Median, Mode')
plt.xlabel('Age')
plt.legend()
plt.show()

# QQ plot – Histogram and Q-Q Plot for Balance
print("\n Histogram and Q-Q Plot for Balance")
plt.figure()
sns.histplot(df['balance'], kde=True)
plt.title("Histogram of Balance")
plt.show()

# Shapiro-Wilk Test for Normality
print("\n Shapiro-Wilk Test for Normality (Balance)")
shapiro_stat, shapiro_p = stats.shapiro(df['balance'].sample(min(5000, len(df))))
print("Shapiro p-value:", shapiro_p)

# Stacked bar chart
print("\n Stacked Bar Chart")
cont_table.plot(kind='bar', stacked=True)
plt.title("Housing vs Deposit")
plt.show()

# Heatmap
print("\n Heatmap")
plt.figure()
sns.heatmap(cont_table, annot=True, fmt='d')
plt.title("Contingency Heatmap")
plt.show()

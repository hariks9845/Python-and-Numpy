# Python-and-Numpy
# Employee Performance & Salary Analytics System

A beginner-friendly data analysis project built using **Python and NumPy**. This project analyzes employee performance scores and salary data using fundamental data science techniques.

The application provides a menu-driven interface to explore employee data, calculate statistics, identify high and low performers, detect missing values and outliers, and generate a summary report.

---

## Features

- Employee dataset overview
- Performance analysis using statistical functions
- Employee filtering using Boolean masks
- Performance categorization using conditional logic
- Department-wise performance analysis
- Employee ranking using `np.argsort()`
- Salary analysis and salary increment calculation
- Performance-based bonus calculation
- Missing value detection and handling using `np.nan`
- Salary outlier detection using the IQR method
- Score normalization using Min-Max scaling
- Save and load NumPy arrays using `.npz` files
- Generate an employee analytics report

---

## Technologies Used

- Python
- NumPy
- VS Code

---

## Project Structure

```text
Employee_Analytics_Project/
│
├── employee_analytics.py
├── README.md
│
├── data/
│   └── employee_data.npz
│
└── reports/
    └── employee_report.txt
```

> The `data` and `reports` folders are created automatically when the corresponding features are used.

---

## Dataset

The project uses sample employee data containing:

- Employee names
- Departments
- Performance scores
- Salary information

Example:

```python
employees = np.array(["Arun", "Priya", "Rahul", "Sneha"])

scores = np.array([85, 45, 90, 35])

salaries = np.array([35000, 28000, 45000, 30000])
```

A missing performance score and an unusual salary value are intentionally included to demonstrate missing-value handling and outlier detection.

---

## NumPy Concepts Used

This project applies several NumPy concepts learned during data science practice:

| Concept | Usage in Project |
|---|---|
| NumPy Arrays | Store employee information |
| Array Attributes | Inspect data shape and type |
| Statistical Functions | Calculate mean, maximum, minimum, median, and standard deviation |
| Boolean Masking | Filter employees based on performance |
| `np.where()` | Categorize employee performance |
| `np.unique()` | Analyze departments |
| `np.argsort()` | Rank employees by performance |
| `np.isnan()` | Detect missing values |
| `np.nanmean()` | Calculate statistics while ignoring missing values |
| Broadcasting | Apply salary increments |
| Vectorized Operations | Calculate employee bonuses |
| Percentiles | Calculate Q1 and Q3 |
| IQR Method | Detect potential salary outliers |
| Normalization | Scale performance scores |
| `np.savez()` | Save multiple arrays |
| `np.load()` | Load saved NumPy data |

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project folder

```bash
cd Employee_Analytics_Project
```

### 3. Install NumPy

```bash
python3 -m pip install numpy
```

---

## How to Run the Project

Run the following command from the project directory:

```bash
python3 employee_analytics.py
```

The application will display a menu with different analysis options.

Example:

```text
===================================
 EMPLOYEE ANALYTICS SYSTEM
===================================

1. Dataset Overview
2. Performance Analysis
3. Employee Filtering
4. Performance Categories
5. Department Analysis
6. Employee Ranking
7. Salary Analysis
8. Bonus Calculation
9. Missing Value Analysis
10. Outlier Detection
11. Score Normalization
12. Save and Load Dataset
13. Generate Report
0. Exit
```

Enter the corresponding number to perform an analysis.

---

## Example Analysis

### Performance Analysis

The project calculates:

- Average performance score
- Highest performance score
- Lowest performance score
- Median score
- Standard deviation

### Employee Filtering

Employees can be filtered based on their performance score.

```python
passed = employees[scores >= 60]
failed = employees[scores < 60]
```

### Performance Categories

Employees are categorized into:

| Score | Category |
|---|---|
| 80 and above | Excellent |
| 60–79 | Good |
| Below 60 | Needs Improvement |
| Missing score | Not Available |

### Outlier Detection

The project uses the **Interquartile Range (IQR)** method to identify potential salary outliers.

```text
IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

Values outside these boundaries are flagged for further investigation.

---

## Output Files

### Saved Dataset

The employee dataset can be saved as:

```text
data/employee_data.npz
```

### Generated Report

The application can generate a summary report:

```text
reports/employee_report.txt
```

---

## Learning Outcomes

Through this project, I practiced applying Python and NumPy concepts to a practical data analysis problem.

Key skills demonstrated include:

- Data analysis using NumPy
- Data cleaning and missing value handling
- Boolean filtering and conditional operations
- Statistical analysis
- Outlier detection
- Data normalization
- Array sorting and ranking
- File handling and report generation

---

## Future Improvements

Future versions of this project could include:

- Reading employee data from CSV or Excel files using Pandas
- Data visualization using Matplotlib and Seaborn
- Interactive dashboards
- Machine learning models for performance prediction
- Database integration using MySQL or PostgreSQL
- Automated testing

---

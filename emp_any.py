
import numpy as np
import os

# ------------------------------------
# 1. CREATE EMPLOYEE DATASET
# ------------------------------------

employees = np.array([
    "Arun", "Priya", "Rahul", "Sneha", "Kiran",
    "Divya", "Amit", "Neha", "Ravi", "Anu"
])

departments = np.array([
    "IT", "HR", "IT", "Finance", "HR",
    "IT", "Finance", "IT", "HR", "Finance"
])

scores = np.array([
    85, 45, 90, 35, 70,
    60, 95, 40, np.nan, 80
])

salaries = np.array([
    35000, 28000, 45000, 30000, 32000,
    40000, 250000, 29000, 31000, 42000
], dtype=float)


# ------------------------------------
# 2. DATASET OVERVIEW
# ------------------------------------

def dataset_overview():

    print("\n========== DATASET OVERVIEW ==========")

    print("Employees:", employees)
    print("Departments:", departments)
    print("Scores:", scores)
    print("Salaries:", salaries)

    print("\nNumber of employees:", employees.size)
    print("Number of dimensions:", employees.ndim)
    print("Score dataset shape:", scores.shape)
    print("Salary data type:", salaries.dtype)


# ------------------------------------
# 3. PERFORMANCE ANALYSIS
# ------------------------------------

def performance_analysis():

    print("\n========== PERFORMANCE ANALYSIS ==========")

    average = np.nanmean(scores)
    highest = np.nanmax(scores)
    lowest = np.nanmin(scores)

    print("Average performance:", average)
    print("Highest performance:", highest)
    print("Lowest performance:", lowest)

    print("Median performance:", np.nanmedian(scores))
    print("Standard deviation:", np.nanstd(scores))


# ------------------------------------
# 4. EMPLOYEE FILTERING
# ------------------------------------

def employee_filtering():

    print("\n========== EMPLOYEE FILTERING ==========")

    passed = employees[scores >= 60]
    failed = employees[scores < 60]

    print("Employees who passed:", passed)
    print("Employees who failed:", failed)

    high_performers = employees[scores >= 80]

    print("High performers:", high_performers)


# ------------------------------------
# 5. PERFORMANCE CATEGORIES
# ------------------------------------

def performance_categories():

    print("\n========== PERFORMANCE CATEGORIES ==========")

    categories = np.where(
        np.isnan(scores),
        "Not Available",
        np.where(
            scores >= 80,
            "Excellent",
            np.where(scores >= 60, "Good", "Needs Improvement")
        )
    )

    for i in range(len(employees)):
        print(employees[i], ":", categories[i])


# ------------------------------------
# 6. DEPARTMENT ANALYSIS
# ------------------------------------

def department_analysis():

    print("\n========== DEPARTMENT ANALYSIS ==========")

    unique_departments = np.unique(departments)

    for dept in unique_departments:

        mask = departments == dept

        dept_scores = scores[mask]

        average = np.nanmean(dept_scores)

        print(dept, "Average Score:", average)


# ------------------------------------
# 7. EMPLOYEE RANKING
# ------------------------------------

def employee_ranking():

    print("\n========== EMPLOYEE RANKING ==========")

    # Place missing scores at the end
    sortable_scores = np.where(
        np.isnan(scores),
        -np.inf,
        scores
    )

    ranking = np.argsort(sortable_scores)[::-1]

    for index in ranking:

        if np.isnan(scores[index]):
            print(employees[index], ": Score unavailable")
        else:
            print(employees[index], ":", scores[index])


# ------------------------------------
# 8. SALARY ANALYSIS
# ------------------------------------

def salary_analysis():

    print("\n========== SALARY ANALYSIS ==========")

    print("Average salary:", np.mean(salaries))
    print("Highest salary:", np.max(salaries))
    print("Lowest salary:", np.min(salaries))

    # Calculate a 5% increment
    new_salaries = salaries + (salaries * 0.05)

    print("Salary after 5% increment:")
    print(new_salaries)


# ------------------------------------
# 9. BONUS CALCULATION
# ------------------------------------

def bonus_calculation():

    print("\n========== BONUS CALCULATION ==========")

    bonuses = np.where(
        scores >= 80,
        salaries * 0.10,
        np.where(scores >= 60, salaries * 0.05, 0)
    )

    for i in range(len(employees)):
        print(employees[i], "Bonus:", bonuses[i])


# ------------------------------------
# 10. MISSING VALUE ANALYSIS
# ------------------------------------

def missing_value_analysis():

    print("\n========== MISSING VALUE ANALYSIS ==========")

    missing = np.isnan(scores)

    print("Missing value mask:", missing)
    print("Number of missing scores:", np.sum(missing))

    average = np.nanmean(scores)

    cleaned_scores = np.where(
        np.isnan(scores),
        average,
        scores
    )

    print("Original scores:", scores)
    print("Cleaned scores:", cleaned_scores)


# ------------------------------------
# 11. OUTLIER DETECTION
# ------------------------------------

def outlier_detection():

    print("\n========== SALARY OUTLIER DETECTION ==========")

    q1 = np.percentile(salaries, 25)
    q3 = np.percentile(salaries, 75)

    iqr = q3 - q1

    lower = q1 - (1.5 * iqr)
    upper = q3 + (1.5 * iqr)

    outliers = salaries[
        (salaries < lower) | (salaries > upper)
    ]

    print("Q1:", q1)
    print("Q3:", q3)
    print("IQR:", iqr)
    print("Lower limit:", lower)
    print("Upper limit:", upper)
    print("Outlier salaries:", outliers)


# ------------------------------------
# 12. NORMALIZATION
# ------------------------------------

def score_normalization():

    print("\n========== SCORE NORMALIZATION ==========")

    minimum = np.nanmin(scores)
    maximum = np.nanmax(scores)

    normalized = (scores - minimum) / (maximum - minimum)

    print("Original scores:", scores)
    print("Normalized scores:", normalized)


# ------------------------------------
# 13. SAVE AND LOAD DATA
# ------------------------------------

def save_and_load():

    print("\n========== SAVE AND LOAD DATA ==========")

    os.makedirs("data", exist_ok=True)

    np.savez(
        "data/employee_data.npz",
        employees=employees,
        departments=departments,
        scores=scores,
        salaries=salaries
    )

    print("Employee dataset saved successfully!")

    loaded_data = np.load("data/employee_data.npz")

    print("Loaded employees:", loaded_data["employees"])
    print("Loaded scores:", loaded_data["scores"])


# ------------------------------------
# 14. GENERATE SUMMARY REPORT
# ------------------------------------

def generate_report():

    os.makedirs("reports", exist_ok=True)

    with open("reports/employee_report.txt", "w") as file:

        file.write("EMPLOYEE PERFORMANCE REPORT\n")
        file.write("===========================\n\n")

        file.write(f"Total employees: {len(employees)}\n")
        file.write(f"Average performance: {np.nanmean(scores):.2f}\n")
        file.write(f"Highest performance: {np.nanmax(scores)}\n")
        file.write(f"Lowest performance: {np.nanmin(scores)}\n")
        file.write(f"Average salary: {np.mean(salaries):.2f}\n")
        file.write(f"Missing scores: {np.sum(np.isnan(scores))}\n")

    print("Report generated: reports/employee_report.txt")


# ------------------------------------
# 15. MAIN PROGRAM
# ------------------------------------

def main():

    while True:

        print("\n===================================")
        print(" EMPLOYEE ANALYTICS SYSTEM")
        print("===================================")

        print("1. Dataset Overview")
        print("2. Performance Analysis")
        print("3. Employee Filtering")
        print("4. Performance Categories")
        print("5. Department Analysis")
        print("6. Employee Ranking")
        print("7. Salary Analysis")
        print("8. Bonus Calculation")
        print("9. Missing Value Analysis")
        print("10. Outlier Detection")
        print("11. Score Normalization")
        print("12. Save and Load Dataset")
        print("13. Generate Report")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            dataset_overview()

        elif choice == "2":
            performance_analysis()

        elif choice == "3":
            employee_filtering()

        elif choice == "4":
            performance_categories()

        elif choice == "5":
            department_analysis()

        elif choice == "6":
            employee_ranking()

        elif choice == "7":
            salary_analysis()

        elif choice == "8":
            bonus_calculation()

        elif choice == "9":
            missing_value_analysis()

        elif choice == "10":
            outlier_detection()

        elif choice == "11":
            score_normalization()

        elif choice == "12":
            save_and_load()

        elif choice == "13":
            generate_report()

        elif choice == "0":
            print("Thank you for using Employee Analytics System!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

def calculate_gross_salary(basic_salary):
    if basic_salary < 1500:
        hra = 0.10 * basic_salary
        da = 0.90 * basic_salary
    else:
        hra = 500
        da = 0.98 * basic_salary
    gross_salary = basic_salary + hra + da
    return gross_salary
basic_salary = float(input("Enter the basic salary: "))
gross_salary = calculate_gross_salary(basic_salary)
print(f"The gross salary is: Rs. {gross_salary:.2f}")
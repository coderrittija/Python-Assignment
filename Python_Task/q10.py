def calculate_division(marks):
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    if percentage >= 60:
        return "First Division"
    elif 50 <= percentage < 60:
        return "Second Division"
    elif 40 <= percentage < 50:
        return "Third Division"
    else:
        return "Fail"
marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]
division = calculate_division(marks)
print(f"The student obtained: {division}")
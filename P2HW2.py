# Grades
module_1 = float(input("Please enter your grade for Module 1? "))
module_2 = float(input("Please enter your grade for Module 2? "))
module_3 = float(input("Please enter your grade for Module 3? "))
module_4 = float(input("Please enter your grade for Module 4? "))
module_5 = float(input("Please enter your grade for Module 5? "))
module_6 = float(input("Please enter your grade for Module 6? "))

#Grades List
module_grades = [module_1, module_2, module_3, module_4, module_5, module_6]
#Grades Printed (Needs to be removed)
print(module_grades)
print("------------Results-------------")
#Lowest Grade
print(f"Lowest Grade: {min(module_grades)}")
#Highest Grade
print(f"Hghest Grade: {max(module_grades)}")
#Sum of Grades
print(f"Sum: {sum(module_grades)}")


#Formulas to get the Average
module_sum = sum(module_grades)
number_of_tests = len(module_grades)


#Grades Average

average = (module_sum / number_of_tests)
print("--------------Average---------------------------")

print(average)

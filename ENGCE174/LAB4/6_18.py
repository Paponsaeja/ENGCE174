grades = {'Alice': [85, 90, 92], 'Bob': [88,87,85], "charlie": [90,91,89]}
average_grades = {}

for student, greades_list in grades.items():
    average_grades[student] = sum(greades_list) / len(greades_list)
    
print('Average Greades:', average_grades)
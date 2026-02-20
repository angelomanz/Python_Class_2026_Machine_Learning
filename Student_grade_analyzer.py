grades = [85,92,78,95,88,76,90,93,82,97]

average =sum(grades) / len(grades)
minimun =min(grades)
maximum =max(grades)
a_grades =sum(1 for g in grades if g > 90)


print(f'Grades(sorted): {grades}')
print(f'Average: {average:.2F}')
print(f'Highest: {maximum}')
print(f'Lowest:  {minimum}')
print(f"A's (above 90):  {a_grades}")  
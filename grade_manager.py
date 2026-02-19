grades = []

grades.append(95)
grades.append(87)
grades.append(92)
grades.append(78)
grades.append(88)

print(f'Number of grades: {len(grades)}')
print(f'Highest grade: {max(grades)}')
print(f'Lowest grade: {min(grades)}')
print(f'average grade: {sum(grades) / len(grades):.2f}')

print(f'\nSorted grades (high to low):{grades}')
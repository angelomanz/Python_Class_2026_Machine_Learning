temperatures = [72,68,75,70,73,69,71]

average = sum(temperatures) / (len(temperatures))

print(f'Average:{average:.1F}F')
print(f'Highest: {max(temperatures)} F')
print(f'Lowest {min(temperatures)}F')
print(f'range: {max(temperatures) -min(temperatures)} f')
print(f'Days above average: {sum(t> average for t in temperatures)}')

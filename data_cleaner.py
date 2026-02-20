data = [10, -999, 25, 30, -999, 15, 40, -999, 35, 20]


clean_data = [x for x in data if x != -999]
average = sum(clean_data) / len(clean_data)
above_avg = [x for x in clean_data if x > average]
min_val = min(clean_data)
max_val = max(clean_data)
normalized = [(x - min_val) / (max_val - min_val) for x in clean_data]


print("Raw data:", data)
print("Clean data:", clean_data)
print("Average:", average)
print("Above average:", above_avg)
print("Normalized:", normalized)
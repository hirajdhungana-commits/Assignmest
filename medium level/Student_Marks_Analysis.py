marks = [45, 78, 62, 89, 55, 92, 38, 76]
highest_mark = max(marks)
lowest_mark = min(marks)

average = sum(marks) / len(marks)

count_average = 0
for mark in marks:
    if mark > average:
        count_average += 1
ascending_order = sorted(marks)

print(highest_mark)
print(lowest_mark)
print(average)
print(count_average)
print(ascending_order)
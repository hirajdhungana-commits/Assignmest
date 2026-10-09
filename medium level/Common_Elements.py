list1 = [10, 20, 30, 40, 50, 60, 60, 70]
list2 = [30, 40, 50, 70, 80, 90]

set1= set(list1)
set2= set(list2)


common = sorted(set1 & set2)
only_list1 = sorted(set1-set2)
only_list2 = sorted(set2-set1)

print("Common elements:", common)
print("Elements only in list1:", only_list1)    
print("Elements only in list2:", only_list2)
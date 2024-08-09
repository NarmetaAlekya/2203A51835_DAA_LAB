def selection_sort_descending(lst):
    n = len(lst)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if lst[j] > lst[max_idx]:
                max_idx = j
        lst[i], lst[max_idx] = lst[max_idx], lst[i]
    return lst
grades = []
n = int(input("Enter the number of grades: "))
print("Enter the grades:")
for _ in range(n):
    grade = int(input())
    grades.append(grade)
sorted_grades = selection_sort_descending(grades)
print("Sorted Grades:", sorted_grades)

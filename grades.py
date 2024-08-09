# Function to implement selection sort in descending order
def selection_sort_descending(lst):
    n = len(lst)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if lst[j] > lst[max_idx]:
                max_idx = j
        lst[i], lst[max_idx] = lst[max_idx], lst[i]
    return lst

# Take input from the user
grades = []
n = int(input("Enter the number of grades: "))

print("Enter the grades one by one:")
for _ in range(n):
    grade = int(input())
    grades.append(grade)

# Sort the grades in descending order
sorted_grades = selection_sort_descending(grades)
print("Sorted Grades (Highest to Lowest):", sorted_grades)

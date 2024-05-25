def greedy_subset_sum(arr, target):
    arr.sort(reverse=True)
    subset = []
    current_sum = 0
    for num in arr:
        if current_sum + num <= target:
            subset.append(num)
            current_sum += num
    
    if current_sum == target:
        return subset
    else:
        return subset, current_sum

arr = [3, 34, 4, 12, 5, 2]
target = 9
result = greedy_subset_sum(arr, target)

print("Подмнож:", result)

def length(lst):
    return len(lst)

def mean(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)

def range_of_list(lst):
    if len(lst) == 0:
        return 0
    return max(lst) - min(lst)

numbers = [1, 2, 3, 4, 5]
print(length(numbers))
print(mean(numbers))
print(range_of_list(numbers))

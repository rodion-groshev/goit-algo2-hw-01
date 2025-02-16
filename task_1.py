def find_min_max(lst):
    if len(lst) == 1:
        return lst[0], lst[0]

    if len(lst) == 2:
        return min(lst[0], lst[1]), max(lst[0], lst[1])

    mid = len(lst) // 2
    left = find_min_max(lst[:mid])
    right = find_min_max(lst[mid:])

    res_min = min(left[0], right[0])
    res_max = max(left[1], right[1])

    return res_min, res_max


if __name__ == '__main__':
    lst = [-5, -10, 2, 5, 20, 60, 5, 22, -55]
    result = find_min_max(lst)
    print("Min number", result[0])
    print("Max number:", result[1])

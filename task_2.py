def quick_select(lst, start, end, k):
    if start == end:
        return lst[start]

    pivot = pivot_sort(lst, start, end)

    if k == pivot:
        return lst[k]
    elif k < pivot:
        return quick_select(lst, start, pivot - 1, k)
    else:
        return quick_select(lst, pivot + 1, end, k)


def pivot_sort(lst, start, end):
    pivot = lst[end]
    i = start
    for j in range(start, end):
        if lst[j] <= pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[i], lst[end] = lst[end], lst[i]
    return i


def find_kth_smallest(lst, k):
    if k < 1 or k > len(lst):
        return None
    return quick_select(lst, 0, len(lst) - 1, k - 1)


if __name__ == '__main__':
    lst = [-5, -55, 5, 22, -2, 56, 18, 10]
    k = 5
    print(f"{k}-th smallest number: {find_kth_smallest(lst, k)}")

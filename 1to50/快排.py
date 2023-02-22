def quick_sort(data: list):
    if len(data) < 2:
        return data.sort()
    mid = data[len(data) // 2]
    left = []
    right = []
    data.remove(mid)
    for num in data:
        if num > mid:
            right.append(num)
        else:
            left.append(num)
    return quick_sort(left) + [mid] + quick_sort(right)

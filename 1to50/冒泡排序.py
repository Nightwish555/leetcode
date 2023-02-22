def bubbleSort(data: list):
    length = len(data)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

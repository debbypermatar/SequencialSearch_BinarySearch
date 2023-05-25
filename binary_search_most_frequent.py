def binary_search_most_frequent(data):
    max_count = 0
    most_frequent = None
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        count = 1
        left = mid - 1
        right = mid + 1

        while left >= 0 and data[left] == data[mid]:
            count += 1
            left -= 1

        while right < len(data) and data[right] == data[mid]:
            count += 1
            right += 1

        if count > max_count:
            max_count = count
            most_frequent = data[mid]

        if count == 1:
            break

        if left >= 0:
            high = left
        if right < len(data):
            low = right

    return most_frequent


my_list = [2, 2, 2, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 8]
most_frequent_element = binary_search_most_frequent(my_list)
print(f"Elemen yang paling banyak muncul adalah {most_frequent_element}")

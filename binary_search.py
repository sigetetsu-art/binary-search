def binary_search(list, item):
    low_index = 0
    high_index = len(list) - 1
    while(low_index <= high_index):
        mid_index = low_index + (high_index - low_index) // 2
        middle_value = list[mid_index]
        if(middle_value == item):
            return middle_value
        elif(middle_value > item):
            high_index = mid_index - 1
        elif(middle_value < item):
            low_index = mid_index + 1
    
    return -1

N, item = map(int, input().split())
list = list(map(int, input().split()))

print(binary_search(list, item))
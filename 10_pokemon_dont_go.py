distance = [int(digit) for digit in input().split(" ")]

copy_of_list = distance[:]

removed_element = 0
sum_of_removed = 0
track_index = []
while len(copy_of_list) > 0:
    current_index = int(input())
    track_index.append(current_index)

    if current_index < 0:
        removed_element = copy_of_list[0]
        sum_of_removed += removed_element
        copy_of_list[0] = copy_of_list[-1]
        copy_of_list[-1] = copy_of_list[0]
        copy_of_list = [x + removed_element if x <= removed_element else x - removed_element for x in copy_of_list]
    elif current_index > len(copy_of_list) - 1:
        removed_element = copy_of_list[-1]
        sum_of_removed += removed_element
        copy_of_list[-1] = copy_of_list[0]
        copy_of_list = [x + removed_element if x <= removed_element else x - removed_element for x in copy_of_list]

    else:
        removed_element = copy_of_list.pop(current_index)
        sum_of_removed += removed_element
        for i in range(len(copy_of_list)):
            if copy_of_list[i] <= removed_element:
                copy_of_list[i] += removed_element
            elif copy_of_list[i] > removed_element:
                copy_of_list[i] -= removed_element

print(sum_of_removed)

import sys
numbers = list(map(int, input().split(", ")))

max_value = - sys.maxsize
group_list = []

for _, number in enumerate(numbers):  # finding and storing the highest value
    if number > max_value:
        max_value = number

get_str = str(max_value)
if max_value % 10 == 0:  # finding the highest group range
    max_value = max_value
elif max_value <= 10:
    max_value = 10
else:
    max_value = (int(get_str[0]) + 1) * 10

temp_list = []
for current_group in range(10, max_value + 1, + 10):
    for _, current_num in enumerate(numbers[:]):
        if current_num <= current_group:
            temp_list.append(current_num)
            numbers.remove(current_num)

    print(f"Group of {current_group}'s: {temp_list}")
    temp_list.clear()

# 1.2:
# import sys
# numbers = list(map(int, input().split(", ")))
#
# max_value = - sys.maxsize
# group_list = []
#
# for i, number in enumerate(numbers):  # finding and storing the highest value
#     if number > max_value:
#         max_value = number
#
# get_str = str(max_value)
# last_two = get_str[-2:]
# if max_value % 10 == 0:  # finding the highest group range
#     max_value = max_value
# elif max_value > 100:
#     if int(last_two[0]) == 0:
#         result = int(last_two) - int(last_two[0]) * 10
#         max_value = int(get_str) + int(last_two[1]) * 10 - result
#     else:
#         result = int(last_two) - int(last_two[0]) * 10
#         max_value = int(get_str) + int(last_two[0]) * 10 - result
# else:
#     max_value = (int(get_str[0]) + 1) * 10
#
# for i in range(max_value, 0, - 10):  # store the groups in a different list
#     group_list.append(i)
#
# temp_list = []
# for i in range(len(group_list) - 1, -1, -1):
#     element = group_list[i]
#     for x, current_num in enumerate(numbers[:]):
#         if current_num <= element:
#             temp_list.append(current_num)
#             numbers.remove(current_num)
#
#     print(f"Group of {element}'s: {temp_list}")
#     temp_list.clear()

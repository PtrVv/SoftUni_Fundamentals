# A function that returns a loading bar depending on the number recieved in the input.
number = int(input())

percentage_list = []
str_of_number = str(number)
get_value = str_of_number[0]

if number >= 100:
    get_value = 10


def loading_bar(num: int):
    for _ in range(int(get_value)):
        percentage_list.append("%")
    while len(percentage_list) < 10:
        percentage_list.append(".")
    loading_list = ''.join(map(str, percentage_list))
    return loading_list


result = loading_bar(number)
if number < 100:
    print(f"{number}% [{result}]")
    print(f"Still loading...")
else:
    print(f"{number}% Complete!")
    print(f"[{result}]")

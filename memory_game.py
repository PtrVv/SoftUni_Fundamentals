elements = input().split(" ")

number_of_moves = 0
has_lost = True
command = input().split(" ")
while command[0] != "end":

    if len(elements) <= 0:
        print(f"You have won in {number_of_moves} turns!")
        has_lost = False
        break

    number_of_moves += 1
    first_index = int(command[0])
    second_index = int(command[1])

    if elements[first_index] == elements[second_index]:
        element_found = elements[first_index]
        elements = [x for x in elements if x != element_found]
        print(f"Congrats! You have found matching elements - {element_found}!")

    elif first_index == second_index or first_index < 0 or second_index < 0:
        to_middle = int(len(elements) / 2)
        add_element = f"-{number_of_moves}a"
        for x in range(number_of_moves):
            elements.insert(to_middle, add_element)
        print("Invalid input! Adding additional elements to the board")

    elif elements[first_index] != elements[second_index]:
        print("Try again!")

    command = input().split(" ")

if has_lost:
    print(f"Sorry you lose :(")
    print(*elements)

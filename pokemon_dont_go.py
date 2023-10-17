# A program that receives a sequence of integers - the distance to the pokemon. Then you will begin receiving integers, which will correspond to indexes in that sequence.
# The program ends when the sequence has no elements left.(there are no more pokemon left to be caught)
distance = [int(digit) for digit in input().split(" ")]

removed_element = 0
sum_of_removed = 0
while len(distance) > 0:
    current_index = int(input())

    if current_index < 0:
        removed_element = distance[0]
        sum_of_removed += removed_element
        distance[0] = distance[-1]
        distance = [x + removed_element if x <= removed_element else x - removed_element for x in distance]
        
    elif current_index > len(distance) - 1:
        removed_element = distance[-1]
        sum_of_removed += removed_element
        distance[-1] = distance[0]
        distance = [x + removed_element if x <= removed_element else x - removed_element for x in distance]

    else:
        removed_element = distance.pop(current_index)
        sum_of_removed += removed_element
        distance = [x + removed_element if x <= removed_element else x - removed_element for x in distance]

print(sum_of_removed)

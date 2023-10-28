# You are given a secret message to decipher
secret_message = input().split()


def swap_position(word, pos1, pos2):
    word[pos1], word[pos2] = word[pos2], word[pos1]
    return word


deciphered_list = []
joined_list = []
temp_list = []
for element in secret_message:
    temp_list.clear()
    joined_list.clear()
    for i in range(len(element)):
        if element[i].isnumeric():
            temp_list.append(element[i])
        else:
            joined_list.append(element[i])

    pos1, pos2 = 0, -1
    swap_position(joined_list, pos1, pos2)
    joined = "".join(temp_list)
    joined_list.insert(0, chr(int(joined)))
    deciphered_list.append("".join(joined_list))

print(" ".join(deciphered_list))

phonebook = {}

info = input().split("-")
while not info[0].isnumeric():

    key = info[0]
    value = info[1]

    if key in phonebook:
        phonebook[key] = value

    else:
        phonebook[key] = value

    info = input().split("-")

for _ in range(int(info[0])):
    search_contact = input()
    if search_contact in phonebook:
        print(f"{search_contact} -> {phonebook[search_contact]}")
    else:
        print(f"Contact {search_contact} does not exist.")

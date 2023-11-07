number_of_commands = int(input())

registered_plates = {}

for _ in range(number_of_commands):
    command = input().split()

    username = command[1]

    if command[0] == "register":
        license_plate = command[2]
        if username not in registered_plates:
            registered_plates[username] = license_plate
            print(f"{username} registered {license_plate} successfully")

        else:
            print(f"ERROR: already registered with plate number {registered_plates[username]}")

    elif command[0] == "unregister":
        if username in registered_plates:
            del registered_plates[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for user, plate in registered_plates.items():
    print(f"{user} => {plate}", end="\n")

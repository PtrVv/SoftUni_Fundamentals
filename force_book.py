info = input()

force_info = {}

while True:
    if info == "Lumpawaroo":
        break

    received = info.split()
    if "|" in received:
        info = info.split(" | ")
        force_side = info[0]
        force_user = info[1]
        user_in_force = False
        for value in force_info.values():
            if force_user in value:
                user_in_force = True
                break
        if not user_in_force:
            if force_side not in force_info.keys():
                force_info[force_side] = []
            force_info[force_side].append(force_user)

    else:
        info = info.split(" -> ")
        force_user = info[0]
        force_side = info[1]
        for value in force_info.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in force_info.keys():
            force_info[force_side] = []
        force_info[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    info = input()

for side, user in force_info.items():
    count_users = len(user)
    if count_users != 0:
        print(f"Side: {side}, Members: {count_users}")
        for u_name in user:
            print(f"! {u_name}", end="\n")

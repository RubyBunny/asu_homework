def read_shadow_file() -> list[list[str]]:
    with open("/etc/shadow", "r") as file:
        data = file.readlines()

    return list(
        filter(lambda x: x[1][:3] == "$y$", map(lambda x: x.split(":")[:2], data))
    )

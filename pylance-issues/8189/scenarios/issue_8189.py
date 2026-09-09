def read_commands(name: str) -> list[str]:
    with open(file=name, mode="r") as cmdfile:
        return cmdfile.readlines()

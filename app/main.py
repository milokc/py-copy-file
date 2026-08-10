def copy_file(command: str) -> None:
    splited = command.split()
    if len(splited) == 3 and splited[1] != splited[2] and splited[0] == "cp":
        file_old = splited[1]
        file_new = splited[2]
        try:
            with (open(file_old, "r") as file_in,
                  open(file_new, "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            pass

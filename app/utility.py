from typing import Any, Dict, List

from app import resurses
from app.commands import Command


def get_command(line: str) -> Command:
    return Command(line.split()[0])


def get_args(line: str) -> List[str]:
    return line.split(" ", 1)[1].split(", ")


def get_arg(mem: Dict, arg: str) -> int:
    if "not" in arg:
        if get_arg(mem, arg.replace("not ", "")):
            return 1
        else:
            return 0
    elif arg.isnumeric():
        return int(arg)
    else:
        return int(mem[arg])


def make(mem: Dict, command: Command, *args) -> Any:
    if command == Command.MOV:
        mem[args[0]] = args[1]
    elif command == Command.INC:
        mem[args[0]] = str(get_arg(mem, args[0]) + 1)
    elif command == Command.CMP:
        mem[resurses.FLAG] = get_arg(mem, args[0]) - get_arg(mem, args[1])
    elif command == Command.JMP:
        mem[resurses.COUNTER] = get_arg(mem, args[0]) - 1
    elif command == Command.JNE:
        if mem[resurses.FLAG] != 0:
            make(mem, Command.JMP, args[0])
    elif command == Command.PRINT:
        print(get_arg(mem, args[0]))

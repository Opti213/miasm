from typing import List

from app import resurses
from app.utility import make, get_command, get_args

mem = {}
mem[resurses.FLAG] = False
mem[resurses.COUNTER] = 0


def get_program(path_to_file: str) -> List[str]:
    with open(path_to_file, "r") as program:
        return [row.replace("\n", "") for row in program]


def do_programme(programme: List[str]):
    while mem[resurses.COUNTER] != len(programme):
        print(mem)
        current_line = programme[mem[resurses.COUNTER]]
        command = get_command(current_line)
        args = get_args(current_line)
        make(mem, command, *args)
        mem[resurses.COUNTER] += 1


programme = get_program("programme.txt")
do_programme(programme)

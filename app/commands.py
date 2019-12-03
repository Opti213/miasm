from enum import Enum


class Command(str, Enum):
    MOV = "MOV"
    INC = "INC"
    CMP = "CMP"
    JMP = "JMP"
    JNE = "JNE"
    PRINT = "PRINT"
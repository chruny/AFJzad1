class Instruction:
    command = ''
    parameter1 = ''
    parameter2 = ''
    parameter3 = ''
    program = ''

    def __init__(self,program):
        self.program = program

    def read(self,):
        print()

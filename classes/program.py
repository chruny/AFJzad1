from classes.instruction import Instruction
import sys


class Program:
    lines = []
    variables = {}

    def load_file_to_lines(self, name):
        with open(name) as f:
            lines_1 = f.readlines()
            for line in lines_1:
                line = [x.strip for x in line.split(',')]
                instruction = Instruction()
                if len(line) == 4:
                    instruction.command = line[0]
                    instruction.parameter1 = line[1]
                    instruction.parameter2 = line[2]
                    instruction.parameter3 = line[3]
                    self.lines.append(instruction)
                elif len(line) == 3:
                    instruction.command = line[0]
                    instruction.parameter1 = line[1]
                    instruction.parameter2 = line[2]
                    self.lines.append(instruction)
                elif len(line) == 2:
                    instruction.parameter1 = line[1]
                    instruction.command = line[0]
                    self.lines.append(instruction)
                else:
                    sys.exit("Bad format of instruction")

    def set_variable(self,name,value):
        self.variables[name] = value

    def get_variable(self,name):
        return self.variables[name]

    def check_if_variable_exists(self,name):
        if name in self.variables:
            return True
        else:
            return False

    def execute_program(self):
        print()

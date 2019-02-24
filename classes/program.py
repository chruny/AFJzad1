from classes.instruction import Instruction
import sys


class Program:
    lines = []
    variables = {}

    __iterator = 0
    __iterator_changed = False

    def load_file_to_lines(self, name):
        with open(name) as f:
            lines_1 = f.readlines()
            for line in lines_1:
                line = [x.strip() for x in line.split(',')]
                instruction = Instruction(self)
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
                elif len(line) == 1:
                    instruction.command = line[0]
                    self.lines.append(instruction)
                else:
                    sys.exit("Bad format of instruction")

    def set_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        variable = self.variables[name]
        return variable

    def check_if_variable_exists(self, name):
        if name in self.variables:
            return True
        else:
            return False

    def set_iterator(self, value):
        self.__iterator = value
        self.__iterator_changed = True

    def get_iterator(self):
        return self.__iterator

    def execute_program(self):
        while self.__iterator < len(self.lines):
            self.__iterator_changed = False
            row = Instruction(self)
            row = self.lines[self.__iterator]
            row.execute_instruction()
            if not self.__iterator_changed:
                self.__iterator = self.__iterator + 1

    def check_length_of_program(self, iterator):
        if (len(self.lines)) > iterator - 1:
            return True
        else:
            return False

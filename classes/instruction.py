import sys


class Instruction:
    command = ''
    parameter1 = ''
    parameter2 = ''
    parameter3 = ''
    program = ''

    def __init__(self, program):
        self.program = program

    def read(self):
        # print('Get key input:')
        sys.stdout.write('Write a number: ')
        input_key = int(input())
        if self.program.set_variable(self.parameter1, input_key):
            sys.stdout.write('Succesfuly added\n')
            # print('Succesfuly added')

    def write(self):
        if self.program.check_if_variable_exists(self.parameter1):
            sys.stdout.write(str(self.parameter1) + '=' + str(self.program.get_variable(self.parameter1)))
            # print(self.parameter1, '=', self.program.get_variable(self.parameter1))
        else:
            sys.stdout.write('Variable ', str(self.parameter1), 'dont exists\n')
            # print('Variable ', self.parameter1, 'dont exists')
            quit()

    def sum(self):
        param1, param2 = self.check_parameters()
        variable = (param1 + param2)
        if self.program.set_variable(self.parameter3, variable):
            sys.stdout.write('=' + str(variable) + '\n')
            # print(variable)

    def sub(self):
        param1, param2 = self.check_parameters()
        variable = (param1 - param2)
        if self.program.set_variable(self.parameter3, variable):
            sys.stdout.write('= ' + str(variable) + '\n')
            # print(variable)

    def multiply(self):
        param1, param2 = self.check_parameters()
        variable = (param1 * param2)
        if self.program.set_variable(self.parameter3, variable):
            sys.stdout.write('= ' + str(variable) + '\n')
            # print(variable)

    def less(self):
        param1, param2 = self.check_parameters()
        variable = (param1 < param2)
        if self.program.set_variable(self.parameter3, variable):
            sys.stdout.write('=' + variable + '\n')
            # print(variable)

    def greater(self):
        param1, param2 = self.check_parameters()
        variable = (param1 > param2)
        if self.program.set_variable(self.parameter3, variable):
            sys.stdout.write('=' + str(variable) + '\n')
            # print(variable)

    def less_or_equal(self):
        param1, param2 = self.check_parameters()
        variable = (param1 <= param2)
        if self.program.set_variable(self.parameter3, variable):
            sys.stdout.write('=' + str(variable) + '\n')
            # print(variable)

    def greater_or_equal(self):
        param1, param2 = self.check_parameters()
        variable = (param1 >= param2)
        if self.program.set_variable(self.parameter3, variable):
            sys.stdout.write('=' + str(variable) + '\n')
            # print(variable)

    def check_parameters(self):
        param1 = ''
        param2 = ''
        try:
            param1 = int(self.parameter1)
        except ValueError:
            param1 = self.program.get_variable(self.parameter1)

        try:
            param2 = int(self.parameter2)
        except ValueError:
            param2 = self.program.get_variable(self.parameter2)

        return param1, param2

    def check_parameter_if_jump(self):
        if self.parameter1 == 'True':
            return True
        elif self.parameter1 == 'False':
            return False
        else:
            if self.program.check_if_variable_exists(self.parameter1):
                return self.program.get_variable(self.parameter1)
            else:
                sys.stdout.write('Error: Variable "' + str(self.parameter1) + '" dont exists\n')
                # print('Error: Variable "', self.parameter1, '" dont exists')
                quit()

    def equal(self):
        param1, param2 = self.check_parameters()
        variable = (param1 == param2)
        if self.program.set_variable(self.parameter3, variable):
            sys.stdout.write('=' + str(variable) + '\n')
            # print(variable)

    def set(self):
        if isinstance(int(self.parameter2), int):
            if self.program.set_variable(self.parameter1, int(self.parameter2)):
                sys.stdout.write(str(self.parameter2) + '\n')
                # print(int(self.parameter2))
        else:
            if self.program .set_variable(self.parameter1, int(self.program.get_variable(self.parameter2))):
                print()

    def jump(self):
        if self.program.check_length_of_program(int(self.parameter1)):
            self.program.set_iterator(int(self.parameter1) - 1)
        else:
            sys.stdout.write("Illegal Jump" + str(self.program.get_iterator()) + '\n')
            # print("Illegal Jump", self.program.get_iterator())
            sys.exit()
        pass

    def jumpt(self):
        variable = self.check_parameter_if_jump()
        if variable:
            if self.program.check_length_of_program(int(self.parameter2)):
                self.program.set_iterator(int(self.parameter2) - 1)
            else:
                sys.stdout.write("Illegal Jump" + str(self.program.get_iterator()) + '\n')
                # print("Illegal Jump", self.program.get_iterator())
                sys.exit()

    def jumpf(self):
        variable = self.check_parameter_if_jump()
        if not variable:
            if self.program.check_length_of_program(int(self.parameter2)):
                self.program.set_iterator(int(self.parameter2) - 1)
            else:
                sys.stdout.write("Illegal Jump" + str(self.program.get_iterator()) + '\n')
                # print("Illegal Jump", self.program.get_iterator())
                sys.exit()

    def execute_instruction(self):
        if self.command == 'READ':
            self.read()
        elif self.command == 'WRITE':
            self.write()
        elif self.command == '+':
            self.sum()
        elif self.command == '-':
            self.sub()
        elif self.command == '*':
            self.multiply()
        elif self.command == '<':
            self.less()
        elif self.command == '>':
            self.greater()
        elif self.command == '<=':
            self.less_or_equal()
        elif self.command == '>=':
            self.greater_or_equal()
        elif self.command == '==':
            self.equal()
        elif self.command == '=':
            self.set()
        elif self.command == 'JUMP':
            self.jump()
        elif self.command == 'JUMPT':
            self.jumpt()
        elif self.command == 'JUMPF':
            self.jumpf()

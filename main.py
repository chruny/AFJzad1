import sys

from classes.program import Program


def main(filename):
    program = Program()
    program.load_file_to_lines(filename)
    program.execute_program()


if __name__ == '__main__':
    main(sys.argv[0])

class Instruction(object):
    def __init__(self, var, change, c_var, condition):
        self.var = var
        self.change = change
        self.c_var = c_var
        self.condition = condition

def clean_instr(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        lines = []
        for line in f.readlines():
            line = line.split()
            if line[1] == 'inc':
                change = int(line[2])
            else:
                change = -int(line[2])
            c_var = line[4]
            condition = line[5:]
            lines.append(Instruction(line[0], change, c_var, condition))
        return lines

def eval_condition(c_var, condition):
    """
    Helper function to evaluate instruction conditions
    """
    condition[1] = int(condition[1])
    if condition[0] == '>':
        return registers[c_var] > condition[1]
    elif condition[0] == '<':
        return registers[c_var] < condition[1]
    elif condition[0] == '>=':
        return registers[c_var] >= condition[1]
    elif condition[0] == '<=':
        return registers[c_var] <= condition[1]
    elif condition[0] == '==':
        return registers[c_var] == condition[1]
    elif condition[0] == '!=':
        return registers[c_var] != condition[1]


def dec8a(instr):
    """
    Args:
        instr (list): list of instruction objects
    """
    registers = {}
    for instr in data:
        if instr.var not in registers.keys():
            registers[instr.var] = 0
        if instr.c_var not in registers.keys():
            registers[instr.c_var] = 0
        if eval_condition(instr.c_var, instr.condition):
            registers[instr.var] += instr.change
        if max(registers.values()) > max_value:
            max_value = max(registers.values())

    return max(registers.values())

def dec8b(instr):
    """
    Args:
        instr (list): list of instruction objects
    """
    registers = {}
    max_value = 0
    for instr in data:
        if instr.var not in registers.keys():
            registers[instr.var] = 0
        if instr.c_var not in registers.keys():
            registers[instr.c_var] = 0
        if eval_condition(instr.c_var, instr.condition):
            registers[instr.var] += instr.change
        if max(registers.values()) > max_value:
            max_value = max(registers.values())

    return max_value

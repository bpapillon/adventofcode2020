import re


def execute_instruction(operation, amount, accumulator, idx):
    if operation == 'acc':
        accumulator += amount
        idx += 1
    elif operation == 'jmp':
        idx += amount
    elif operation == 'nop':
        idx += 1
    return (idx, accumulator)


def parse_instruction(instruction):
    match = re.match(r'^(acc|jmp|nop) \+*(\-*[0-9]+)$', instruction)
    return (match.group(1), int(match.group(2)))


def execute(instructions):
    idx = 0
    accumulator = 0
    instruction = instructions[idx]
    while instruction is not None:
        operation, amount = instruction
        instructions[idx] = None
        idx, accumulator = execute_instruction(operation, amount, accumulator, idx)
        if idx == len(instructions):
            return accumulator
        instruction = instructions[idx]
    return False


def toggle(instructions, idx):
    operation, amount = instructions[idx]
    if operation == 'acc':
        instructions[idx] = (operation, amount)
    if operation == 'jmp':
        instructions[idx] = ('nop', amount)
    if operation == 'nop':
        instructions[idx] = ('jmp', amount)
    return instructions


filename = 'input.txt'
instructions = map(parse_instruction, open(filename, 'rb').read().strip().split('\n'))
for idx in range(len(instructions)):
    cur_instructions = instructions[:]
    toggle(cur_instructions, idx)
    val = execute(cur_instructions)
    if val is not False:
        print val
        break

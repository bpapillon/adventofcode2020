import re


def parse_instruction(instruction):
    match = re.match(r'^(acc|jmp|nop) \+*(\-*[0-9]+)$', instruction)
    return (match.group(1), int(match.group(2)))


filename = 'input.txt'
instructions = open(filename, 'rb').read().strip().split('\n')

idx = 0
accumulator = 0
instruction = instructions[idx]
while instruction is not None:
    instructions[idx] = None
    operation, amount = parse_instruction(instruction)
    if operation == 'acc':
        accumulator += amount
        idx += 1
    elif operation == 'jmp':
        idx += amount
    elif operation == 'nop':
        idx += 1
    instruction = instructions[idx]

print 'accumulator value: ' + str(accumulator)

import re


def parse_line(line):
    pattern = r'([0-9]+)\-([0-9]+) ([a-z])\: ([a-z]+)$'
    match = re.match(pattern, line)
    positions = map(int, [match.group(1), match.group(2)])
    char = match.group(3)
    password = match.group(4)
    return (password, char, positions)


def valid_password(line):
    password, char, positions = parse_line(line)
    relevant_chars = map(lambda x: password[x - 1], positions)
    matches = [relevant_char for relevant_char in relevant_chars if relevant_char == char]
    return len(matches) == 1


lines = open('input.txt', 'rb').read().strip().split("\n")
valid_lines = [line for line in lines if valid_password(line)]
print len(valid_lines)

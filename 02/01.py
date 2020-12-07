import re


def parse_line(line):
    pattern = r'([0-9]+)\-([0-9]+) ([a-z])\: ([a-z]+)$'
    match = re.match(pattern, line)
    min_occurrences = int(match.group(1))
    max_occurrences = int(match.group(2))
    char = match.group(3)
    password = match.group(4)
    return (password, char, min_occurrences, max_occurrences)


def valid_password(line):
    password, char, min_occurrences, max_occurrences = parse_line(line)
    occurrences = password.count(char)
    return occurrences >= min_occurrences and occurrences <= max_occurrences


lines = open('input.txt', 'rb').read().strip().split("\n")
valid_lines = [line for line in lines if valid_password(line)]
print len(valid_lines)

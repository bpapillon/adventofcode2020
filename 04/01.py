import re


def parse_passport(lines):
    return dict(map(lambda x: x.split(':'), re.split(r'\s+', lines)))


def passport_is_valid(passport):
    required_keys = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    return len(required_keys - set(passport.keys())) == 0


def passports_from_file(filename):
    passport_entries = open(filename, 'rb').read().strip().split("\n\n")
    return map(parse_passport, passport_entries)


def valid_passports_from_file(filename):
    passports = passports_from_file(filename)
    return [passport for passport in passports if passport_is_valid(passport)]


filename = 'input.txt'
print len(valid_passports_from_file(filename))

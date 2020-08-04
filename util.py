import hashlib


def hash_string(input_string):
    hash_object = hashlib.sha1(input_string.encode())
    pb_hash = hash_object.hexdigest()
    return pb_hash


def generate_string_from_list(number_list):
    generated_string = ''
    for number in number_list:
        generated_string += number_to_letter(number)
    return generated_string


def number_to_letter(number):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return alpha[int(number)]


def generate_rainbow_table():
    rainbow_table = {}
    f = open('hashes.txt', 'r')
    line = f.readline()

    while line:
        sequence = line.split(' ')[0]
        hash_string = line.split(' ')[1]
        rainbow_table[hash_string[:-1]] = sequence
        line = f.readline()

    f.close()
    return rainbow_table

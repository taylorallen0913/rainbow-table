import util

f = open('hashes.txt', 'w')


for x in range(26):
    for y in range(26):
        for z in range(26):
            sequence_list = []
            sequence_list.append(x)
            sequence_list.append(y)
            sequence_list.append(z)
            generated_string = util.generate_string_from_list(sequence_list)
            hash_string = util.hash_string(generated_string)
            f.write(f"{generated_string} {hash_string}\n")

f.close()

rainbow_table = util.generate_rainbow_table()

print(rainbow_table['7e240de74fb1ed08fa08d38063f6a6a91462a815'])

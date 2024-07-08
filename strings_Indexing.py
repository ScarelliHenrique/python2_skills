# Indexing strings.
the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()
#-----------------------------------------
the_string = 'Hello World!'

# Print each character with its index
for ix in range(len(the_string)):
    print(f"Character '{the_string[ix]}' at index {ix}", end=', ')

print()
#-----------------------------------------
#indexing=acessing elements of a sequence using []    [start:end:step]

credit_number="1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[::2])

last_digits=credit_number[-4:]
print(f'XXXX-XXXX-XXXX-{last_digits}')
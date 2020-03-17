# На вход подаётся список имён.
# Найти и вывести самое длинное имя
# и его длину соответственно.

inp = input()
names = inp.split(' ')

max_name = names[0]
for name in names:
    if len(name) >= len(max_name):
        max_name = name

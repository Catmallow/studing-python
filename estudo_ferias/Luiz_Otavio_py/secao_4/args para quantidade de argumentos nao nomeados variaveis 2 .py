x, y, *resto = 1, 2, 3, 4, 5, 6, 7, 8
print(x, y, resto)

print(type(resto))

def soma(args):
    total = 0
    for numero in args:
        total += numero
    return total
soma(resto)
print(type(resto))
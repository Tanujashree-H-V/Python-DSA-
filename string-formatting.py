def print_formatted(number):
    # your code goes here
     width = len(bin(number)[2:])

     for i in range(1, number + 1):
        dec = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)

        print(dec, octal, hexa, binary)

print_formatted(17)

Paste this **complete and clean version** 

```python
def binary_to_decimal(b):
    return int(b, 2)

def octal_to_decimal(o):
    return int(o, 8)

def hex_to_decimal(h):
    return int(h, 16)

print("Number System Conversion Calculator")
print("1. Decimal to Binary")
print("2. Decimal to Octal")
print("3. Decimal to Hexadecimal")
print("4. Binary to Decimal")
print("5. Octal to Decimal")
print("6. Hexadecimal to Decimal")

choice = int(input("Enter your choice: "))

if choice == 1:
    n = int(input("Enter decimal number: "))
    print("Binary:", bin(n)[2:])

elif choice == 2:
    n = int(input("Enter decimal number: "))
    print("Octal:", oct(n)[2:])

elif choice == 3:
    n = int(input("Enter decimal number: "))
    print("Hexadecimal:", hex(n)[2:].upper())

elif choice == 4:
    b = input("Enter binary number: ")
    print("Decimal:", binary_to_decimal(b))

elif choice == 5:
    o = input("Enter octal number: ")
    print("Decimal:", octal_to_decimal(o))

elif choice == 6:
    h = input("Enter hexadecimal number: ")
    print("Decimal:", hex_to_decimal(h))

else:
    print("Invalid choice")

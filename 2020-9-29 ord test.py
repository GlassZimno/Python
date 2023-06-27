#Nick Zimny
#29/9/2020
for i in range(65, 91):
  print(chr(i), end = "")
print()
for i in range(97, 123):
  print(chr(i), end = "")
print()
for i in range(48, 58):
  print(chr(i), end = "")
print()
char = input("Please enter a character: ")
num = ord(char)
num *= 99
print(num)

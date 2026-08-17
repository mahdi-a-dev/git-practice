# 1
print("-----------1-----------")
number = int(input("Enter a number: "))
print("yes" if number % 2 == 0 and number % 5 == 0 else "no")

# 2
print("-----------2-----------")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

is_rectangle = (x < y + z) and (y < x + z) and (z < x + y)
motesivi_azla = (x == y) and (y == z)
motesavi_saghein = (x == y) or (y == z) or (x == z)
mokhtalef_azla = (x != y) and (y != z) and (x != z)
ghaem_zavie = x ** 2 == (y ** 2 + z ** 2) or y ** 2 == (x ** 2 + z ** 2) or z ** 2 == (x ** 2 + y ** 2)

if is_rectangle:
    print("True")
    if motesivi_azla:
        print("motesavi azla ast.")
    if motesavi_saghein:
        print("motesavi saghein ast.")
    if mokhtalef_azla:
        print("mokhtalef azla ast.")
    if ghaem_zavie:
        print("ghaem zavie ast.")

else:
    print("False")

# 3
print("-----------3-----------")
ch = input("enter ch: ")
if 48 <= ord(ch) <= 57:
    print("is number")
elif 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
    print("is letter")
else:
    print("Others!")
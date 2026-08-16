#1
print("---------1---------")
data = bytes([10, 20, 30, 40])
print(data.hex())

#2
print("---------2---------")
hex_string = "48656c6c6f"
byte_array = bytearray.fromhex(hex_string)
print(byte_array)

#3
print("---------3---------")
data = bytearray([10, 20, 30, 40])
print(data.hex())
data[1] = 99
print(data.hex())

#4
print("---------4---------")
a = bytes([10, 20, 30])
b = bytes([40, 50, 60])
result = a + b
print(result.hex())

#5
print("---------5---------")
data = bytes([10, 20, 30, 40, 20, 60])
print("true" if 20 in data else "false")

#6
print("---------6---------")
data = bytes([10, 20, 30, 40])
numbers = list(data)
print(numbers)

#7
print("---------7---------")
data = bytes([10, 20, 30, 40, 20, 60])
index = data.index(30)
print(indexdata = bytes([10, 20, 30, 40, 20, 60]))

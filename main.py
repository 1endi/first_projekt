# if умова:
#     блок коду
#name = 'Jack'
# if name == 'Jack':
#     print(f'Hello {name}')

# if name == 'Jack1':
#     print(f'Hello{name}') 
#ord('a')
# name = ''
# while True:
#     #print("String to capitalize [type q to quit]:")
#     name = input("Who are you? ")
#     if name != "Jack":
#         continue
#     print("Hello Jack. What is the password?")
#     password = input("Please set password ")
#     if password == "secret":
#         break
# print("Ok")

# fruit = "apple"
# for char in fruit:
#      print(char)print("test")

# test = "test"
# for item in range(5):
#     print(f"literation: {item}")
# i = 0
# while i < 5:
#     print(f"literation: {i}")
#     i = i + 1

# b = 3
# a = 2
# c = a + b
# for item in range(5, 16, c):  # range(start, end, step)
#     print(f"literation: {item}")  

# for index, value in enumerate("test", 1):
#     print(f"index is {index} - Value: {value}")

#for item in range(1, 10, 1.5):
#    print(item)                   #не можна дробове

# for number in range(5):
#     print(number)
#     if number == 2:
#         continue # break
# else:
#     print("We Finished!")

# for index, value in enumerate("Test", 1):
#     print(index, value)
# try:
#     Block
# except:
#      block
 
value_1 = int(input("please set first value: "))
value_2 = int(input("Please set second value: "))
result = 0

try:        #обробка помилок (мусить бути try і exept)
 #можна писати it, if і т.д.
     result = value_1/value_2
except ZeroDivisionError:
    #можна писати if, it, for і т.д.
     print("You can't by zero")
except ValueError:
    print("Wrong ValueError")
print(result)
file01 = input("enter file name: ")
try:
    with open(file01, "r") as file:
     content = file.read()
     print(content)
except FileNotFoundError:
    print("file not found............")      
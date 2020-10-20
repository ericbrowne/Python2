# Eric Browne
def greet2(number, name):
    count =1
    string = "hello"+ name
    if number != 1:
        count = number
    for i in range(0,count):
        string = string + "!"
    return string
print(greet2(4,'eric'))

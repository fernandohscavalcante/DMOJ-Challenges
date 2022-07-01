celsius = int(input())
def conv(c):
     f = 9/5 * celsius + 32
     return f
fahrenheit = conv(celsius)
print(int(fahrenheit))
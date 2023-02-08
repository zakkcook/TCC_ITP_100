'''
write a program that uses nested loops to draw this pattern:
'''
x = 7
y = 7
z = ""


while(y>0):
    while(x>0):
        z = z + '*'
        x = x - 1
    print(z)
    y = y - 1
# x = 1, y = 1
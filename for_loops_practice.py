import turtle
turtle.ht()


print ("To make a triangle using astrics I need you to write this statement out: print_tirangle(# of lines here)")

def print_triangle(n_lines):
    for i in range(1,n_lines):
        print(i*"*")

my_drawing=[(0,0),(0,100),(100,100), (100,0), (0,0)]


for i in range(len(my_drawing)):
    turtle.goto(my_drawing[i])

x=3

x=x+3

x-=3

print(x-3)

print(x)

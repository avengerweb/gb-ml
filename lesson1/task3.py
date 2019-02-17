# Diagram: https://drive.google.com/file/d/1kFg-w3n_3cYiaRjikXsFOlvMWkYwb5NO/view?usp=sharing
x1 = int(input("Enter the x coordinate of first point: "))
y1 = int(input("Enter the y coordinate of first point: "))

x2 = int(input("Enter the x coordinate of second point: "))
y2 = int(input("Enter the y coordinate of second point: "))

x_diff = x1 - x2
k = 0

if x_diff != 0:
    k = (y1 - y2) / x_diff

b = y2 - k * x2

# I can add here several conditions for k and b and make pretty output of the equation, but i`m lazy (big flow-chart)
print("y = %i * x + (%i)" % (k, b))

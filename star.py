row = int(input("Enter no of rows : "))
a = " * "
stars_count = 1
while row > 0:
    print(" " * row + a * stars_count)
    row -= 1
    stars_count += 1

range=input("Table till which number")
y="*"
i=1
while i<=int(range):
    a=i *  y
    i=i+1
    print(a)


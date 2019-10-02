#a1q2
#xs and ls are coordinates of the bottom left

def in_out(xs, ys, side):
    print("(",xs,",", ys,",", side,")")

    xq=float(input("Enter a number for the x coordinate of a query point:"))
    yq=float(input("Enter a number for the y coordinate of a query point:"))

    xrange= xs + side #range for x in which the query can exist
    yrange=ys + side #range for y in which the query cam exist

    #checking if points are in range and returns True or False
    return (((xrange - xq) >= xs) == ((yrange - yq) >= ys))

#Take all the user input
xs=float(input("Enter the x coordinate:"))
ys=float(input("Enter the y coordinate:"))
side=float(input("Enter the length of the side of the square:"))

in_out(xs, ys, side)

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle(Point):
    def __init__(self , bottomleft = 0, topright = 0, colour = 'red'): #constructor
        self.bottomleft = bottomleft
        self.topright = topright
        self.colour = colour

    def __eq__(self, other): #boolean return
        return self.bottomleft == other.bottomleft and self.topright == other.topright

    def __repr__(self): #return when user does "r1"
        return 'Rectangle({},{},"{}")'.format(self.bottomleft,self.topright,self.colour)

    def __str__(self): #return when user does "print(r1)"
        return  'I am a '+self.colour+' rectangle with bottom left corner at '+str(self.bottomleft)+' and top right corner at '+str(self.topright)

    def get_bottom_left(self): #return bottom left coordinate
        return self.bottomleft

    def get_top_right(self): #return top right coordinate
        return self.topright

    def get_color(self): #return colour
        return self.colour

    def reset_color(self, newcolour): #reset colour
        self.colour = newcolour

    def get_perimeter(self): #return parameter of rectangle
        side_sum = (self.topright.x - self.bottomleft.x) + (self.topright.y - self.bottomleft.x)
        return 2*side_sum

    def get_area(self): #return area of rectangle
        area = (self.topright.x - self.bottomleft.x) * (self.topright.y - self.bottomleft.x)
        return area

    def move(self ,dx, dy): #move rectangle coordinates
        Point.move(self.bottomleft, dx, dy)
        Point.move(self.topright, dx, dy)

    def intersects(self, other): #return True if the calling rectangle intersects given rectangle
        if (self.topright.x<other.bottomleft.x) or (other.topright.x<self.bottomleft.x) or (self.topright.y<other.bottomleft.y) or (other.topright.y<self.bottomleft.y):
            return False
        return True

    def contains(self, x, y): #see if given points are in the rectangle
        return (x>=self.bottomleft.x and x<=self.topright.x) and (y>=self.bottomleft.y and y<=self.topright.y)


class Canvas:
    def __init__(self):
        self.l = []

    def __repr__(self):
        return 'Canvas ('+str(self.l)+')'

    def __len__(self): #needed since len isnt in the class
        return len(self.l)

    def add_one_rectangle(self, rectangle): #add a rectangle to array
        self.l.append(rectangle)

    def count_same_color(self, colour): #see if colour is already there
        count= 0
        for i in self.l:
            temp =i.get_color()
            if temp == colour:
                count +=1
        return count

    def total_perimeter(self): #get total permimiter by scanning array
        total = 0
        for i in self.l:
            total += i.get_perimeter()
        return total

    def min_enclosing_rectangle(self): #calculate min encolsing rectangle
        x=0
        y=0
        x1=0
        y1=0
        for i in self.l:
            a = i.get_top_right()
            b = i.get_bottom_left()
            a1 = a.get()
            b1 = b.get()
            if a1[0]>x:
                x = a1[0]
            if a1[1]>y:
                y = a1[1]
            if b1[0]<x1:
                x1=b1[0]
            if b1[0]<y1:
                x1=b1[1]
        string = 'Rectangle ('+str(Point(x1,y1))+' , '+str(Point(x,y))+' , '+self.colour+')'
        return string

    def common_point(self): #True if one point intersects all rectangles
        for i in range(len(self.l)):
            for j in range(i+1,len(self.l)):
                if i!= ( len(self.l) -1 ):
                    var = self.l[i].intersects(self.l[j])
                    if var == False:
                        return False
        return var


'''
#TEST CASES (COMPLETE )
if __name__ == "__main__":  #COMPLETE
    r1 = Rectangle(Point(), Point(1,1), "red")
    r1
    print ( r1.get_color() )
    print ( r1.get_bottom_left() )
    print ( r1.get_top_right() )
    r1.reset_color("blue")
    print ( r1.get_color() )
    r1
    r1.move(2,3)
    r1
    print(r1)
    r2=eval(repr(r1))
    r2
    print (r1 is r2)
    print (r1==r2 )
    r3=Rectangle(Point(), Point(2,1), "red")
    print ( r3.get_perimeter() )
    r4=Rectangle(Point(1,1), Point(2,2.5), "blue")
    print( r4.get_area() )
    r5=Rectangle(Point(1,1), Point(2,2.5), "blue")
    print ( r4 == r5 )
    print  ( r4 is r5 )
    r=Rectangle(Point(1,1), Point(2,5), "blue")
    print ( r.contains(1.5,1) )
    print ( r.contains(2,2) )
    print (r.contains(0,0) )

if __name__ == "__main__": #COMPLETE
    r1=Rectangle(Point(1,1), Point(2,2), "blue")
    r2=Rectangle(Point(2,2.5), Point(3,3), "blue")
    r3=Rectangle(Point(1.5,0),Point(1.7,3),"red")
    print(r3)
    print( r1.intersects(r2) )
    print( r2.intersects(r1) )
    print( r1.intersects(r3) )
    print( r2.intersects(r3) )

#canvas test cases
if __name__ == "__main__":  #WORKS
    c=Canvas()
    r1=Rectangle(Point(-2,-2), Point(-1,2), "blue")
    r2=Rectangle(Point(-2,-2), Point(2,-1), "blue")
    r3=Rectangle(Point(1,-2), Point(2,2), "blue")
    r4=Rectangle(Point(-2,1), Point(2,2), "blue")
    c.add_one_rectangle(r1)
    c.add_one_rectangle(r2)
    c.add_one_rectangle(r3)
    c.add_one_rectangle(r4)
    print ( c.common_point() )

if __name__ == "__main__" : #WORKS
    c=Canvas()
    print ( len(c) )
    r1=Rectangle(Point(1,1), Point(2,2), "blue")
    r2=Rectangle(Point(2,2.5), Point(3,3), "blue")
    r3=Rectangle(Point(1.5,0),Point(1.7,3),"red")
    c.add_one_rectangle(r1)
    c.add_one_rectangle(r2)
    c.add_one_rectangle(r3)
    c.add_one_rectangle( Rectangle(Point(0,0),Point(100,100),"orange") )
    print ( len(c) )
    print(c)
    print ( c.count_same_color("blue") )
    print ( c.count_same_color("red") )
    print ( c.count_same_color("purple") )

if __name__ == " __main__": #WORKS
    c=Canvas()
    r1=Rectangle(Point(1,1), Point(2,2), "blue")
    r2=Rectangle(Point(1,1), Point(4,4), "blue")
    r3=Rectangle(Point(-2,-2), Point(-1,-1), "blue")
    c.add_one_rectangle(r1)
    c.add_one_rectangle(r2)
    c.add_one_rectangle(r3)
    print ( c.total_perimeter() )
'''

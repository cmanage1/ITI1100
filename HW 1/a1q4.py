#a1q4

##Functions that are being called
def convertsecond(lightyears):
    sec= 365.26 * 24 * 60 * 60 *lightyears
    return sec

def convertdistance(sec):
    km= sec * 300000
    return km

def calculatestarD(d1, d2):
    dl = d1+d2 #add the two distances
    sec = convertsecond(dl)
    km =convertdistance(sec)
    return km

#Actual code
lightyears=float(input("Input a number of light-years:"))
sec=convertsecond(lightyears)
distance=convertdistance(sec)
print("The number of seconds is", sec)
print("The distance is", distance, "km.")


star1d=float(input("Input the distance to the first star, in light years:"))
star2d=float(input("Input the distance to the first start, in light years:"))

starD=calculatestarD(star1d, star2d)
print("The distance between the two stars is", starD, "km.")

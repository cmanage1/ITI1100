import math

def calculate(v):
    angles=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    distance= []

    for i in range (len(angles)):
        angles[i]= (math.pi/180) * angles[i]

        d=  2* (v**2) * math.cos(angles[i]) * math.sin(angles[i])
        d = d/ 9.8
        distance.append(d)
    print(distance)

vel= float(input("Please enter a speed (m/s):"))
calculate(vel)

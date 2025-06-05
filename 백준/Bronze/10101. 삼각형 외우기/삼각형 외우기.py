angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

angle = [angle1, angle2, angle3]

if angle[0] == angle[1] == angle[2] == 60:
    print("Equilateral")
elif sum(angle) == 180 and (angle[0] == angle[1] or angle[1] == angle[2] or angle[0] == angle[2]):
    print("Isosceles")
elif sum(angle) == 180 and (angle[0] != angle[1] and angle[1] != angle[2] and angle[0] != angle[2]):
    print("Scalene")
elif sum(angle) != 180:
    print("Error")
import math
#Firstly import the inputs and import math package for square root and square process
Ax=float(input("Enter coordinate x of dot A: "))
print(Ax)
Ay=float(input("Enter coordinate y of dot A: "))
print(Ay)
Bx=float(input("Enter coordinate x of dot B: "))
print(Bx)
By=float(input("Enter coordinate y of dot B: "))
print(By)
Cx=float(input("Enter coordinate x of dot C: "))
print(Cx)
Cy=float(input("Enter coordinate y of dot C: "))
print(Cy)

#Then trying to find the length of part of triangle
AB = (Bx-Ax)**2 + (By-Ay)**2
print("Length of AB is : " + str(math.sqrt(AB)))
BC = float((Cx-Bx)**2 + (Cy-By)**2)
print("Length of BC is : " + str(math.sqrt(BC)))
AC = float((Cx-Ax)**2 + (Cy-Ay)**2)
print("Length of AC is : " + str(math.sqrt(AC)))

# This statements id showing the type of triangle
if AB==AC and AB==BC and AC==BC:
    print("Triangle IS 'Equilateral'")
else :
    print("Triangle IS NOT'Equilateral'")


if AB==BC:
    print("Triangle IS'Isosceles'")
else :
    print("Triangle IS NOT 'Isosceles'")

BAC=AB**2 + AC**2 #AB square + AC square to find the right triangle

if BC**2 == BAC:
    print("Triangle is 'RIGHT'")
else:
    print("Triangle is NOT 'RIGHT'")
#BCC=float(BC)
P=float(math.sqrt(AB)+math.sqrt(AC)+math.sqrt(BC)) #P=Perimeter of triangle
print("Perimeter :" + str(P))
# The last part of task
for i in range(int(P)+1):
    if i % 2  == 0:
        print(i)


print("Have a good day!")


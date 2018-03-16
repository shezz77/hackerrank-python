from collections import namedtuple

Point = namedtuple('Point', 'x,y')

pt1 = Point(1, 2)
pt2 = Point(3, 4)

dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)

print(dot_product)


Car = namedtuple('Car', 'Price Mileage Color Class')
xyz = Car(Price=100000, Mileage=30, Color='Red', Class='Y')
print(xyz.Color)


n = int(input())
a = input()
total = 0

Student = namedtuple('Student', a)

for _ in range(n):
    student = Student(*input().split())
    total += int(Student.MARKS)

print('{:.2f}'.format(total/n))


import math

g = 9810
width = 1.2
height = 1.8
l = 3.9
angle_in_degrees = 60

# แปลงมุมจากองศาเป็นเรเดียน
angle_in_radians = math.radians(angle_in_degrees)

sin = math.sin(angle_in_radians)

Hc = l * sin
rounded_Hc = round(Hc, 2)  # ปัดเศษให้เหลือทศนิยม 2 ตำแหน่ง

A = width * height

Fr = g * rounded_Hc * A

print(Fr)



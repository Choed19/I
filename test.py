import math

g = float(input("กรุณาป้อนค่า g: "))
width = float(input("กรุณาป้อนค่า width: "))
height = float(input("กรุณาป้อนค่า height: "))
l = float(input("กรุณาป้อนค่า l: "))
angle_in_degrees = float(input("กรุณาป้อนค่า angle_in_degrees: "))

# Step 1
angle_in_radians = math.radians(angle_in_degrees)
sin = math.sin(angle_in_radians)
Hc = l * sin
rounded_Hc = round(Hc, 2)
A = width * height
Fr = g * rounded_Hc * A

# Step 2
Lxc = width * height**3 / 12
Yc = 3.9
Ayc = A * Yc

# หา Yp ด้วยสูตร Lxc/Ayc+Yc
Yp = Lxc / Ayc + Yc
rounded_Yp = round(Yp, 2)

# แรงกดของน้ำ (Fr), แรงดึงของเชือก (F)
F = (0.97 * Fr) / 1.8
rounded_F = round(F, 0)

print(rounded_F)

import math
# ค่า g คือค่าความเร่งเนื่องจากความโน้มถ่วงของโลก
g = float(input("กรุณาป้อนค่า g: "))
width = float(input("กรุณาป้อนค่า width: "))
height = float(input("กรุณาป้อนค่า height: "))
l = float(input("กรุณาป้อนค่า l: "))
angle_in_degrees = float(input("กรุณาป้อนค่า angle_in_degrees: "))

#Step 1
# แปลงมุมจากองศาเป็นเรเดียน
angle_in_radians = math.radians(angle_in_degrees)
sin = math.sin(angle_in_radians)
Hc = l * sin
rounded_Hc = round(Hc, 2)  # ปัดเศษให้เหลือทศนิยม 2 ตำแหน่ง
A = width * height
Fr = g * rounded_Hc * A
#Step 2
Lxc = width*height**3/12
#Yc เท่ากับ 3.9 เนื่องจากประตูน้ำมีความสูง 3.9 เมตร และมุมเอียงของประตูน้ำเท่ากับ 60 องศา
Yc = 3.9
Ayc = A*Yc

# หา Yp ด้วยสูตร Lxc/Ayc+Yc

Yp = Lxc/Ayc+Yc
rounded_Yp = round(Yp, 2)  # ปัดเศษให้เหลือทศนิยม 2 ตำแหน่ง
# แรงกดของน้ำ (Fr),แรงดึงของเชือก (F)
# 0.97 คือระยะจากจุดหมุนถึงจุดที่แรงกดของน้ำกระทำต่อวัตถุ
# 1.8 คือระยะจากจุดหมุนถึงจุดที่แรงดึงของเชือกกระทำต่อวัตถุ
#นำระยะจากจุดหมุนถึงจุดที่แรงกดของน้ำกระทำต่อวัตถุมาคูณกับแรงดันน้ำแล้วส่วนด้วยระยะจากจุดหมุนถึงจุดที่แรงดึงของเชือกกระทำต่อวัตถุ

F = (0.97*Fr)/1.8
rounded_F = round(F, 0) # ปัดเศษให้เหลือทศนิยม 0 ตำแหน่ง
print (rounded_F)
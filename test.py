import tkinter as tk
import math

def calculate_force():
    g = float(entry_g.get())
    width = float(entry_width.get())
    height = float(entry_height.get())
    l = float(entry_l.get())
    angle_in_degrees = float(entry_angle.get())

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
    Yc = 3.9
    Ayc = A*Yc
    Yp = Lxc/Ayc+Yc
    rounded_Yp = round(Yp, 2)  # ปัดเศษให้เหลือทศนิยม 2 ตำแหน่ง

    # แรงกดของน้ำ (Fr), แรงดึงของเชือก (F)
    F = (0.97*Fr)/1.8
    rounded_F = round(F, 0) # ปัดเศษให้เหลือทศนิยม 0 ตำแหน่ง

def clear_entries():
    # ล้างค่าใน Entry Widgets
    entry_g.delete(0, tk.END)
    entry_width.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    entry_l.delete(0, tk.END)
    entry_angle.delete(0, tk.END)

    result_label.config(text=f"Force (F): {rounded_F}")

# สร้างหน้าต่าง Tkinter
window = tk.Tk()
window.title("คำนวณแรง")

# Label และ Entry Widgets สำหรับกรอกค่า
label_g = tk.Label(window, text="ค่า g:")
label_g.grid(row=0, column=0)
entry_g = tk.Entry(window)
entry_g.grid(row=0, column=1)

label_width = tk.Label(window, text="ค่าความกว้าง :")
label_width.grid(row=1, column=0)
entry_width = tk.Entry(window)
entry_width.grid(row=1, column=1)

label_height = tk.Label(window, text="ค่าความสูง :")
label_height.grid(row=2, column=0)
entry_height = tk.Entry(window)
entry_height.grid(row=2, column=1)

label_l = tk.Label(window, text="ค่าความลึก:")
label_l.grid(row=3, column=0)
entry_l = tk.Entry(window)
entry_l.grid(row=3, column=1)

label_angle = tk.Label(window, text="ค่าองค์ศา:")
label_angle.grid(row=4, column=0)
entry_angle = tk.Entry(window)
entry_angle.grid(row=4, column=1)

# ปุ่ม "คำนวณ" และ Label สำหรับแสดงผลลัพธ์
calculate_button = tk.Button(window, text="คำนวณ Force", command=calculate_force)
calculate_button.grid(row=5, column=0, columnspan=2)

result_label = tk.Label(window, text="Force (F):")
result_label.grid(row=6, column=0, columnspan=2)

# ปุ่ม "ล้างข้อมูล" สำหรับล้างค่าทั้งหมด
clear_button = tk.Button(window, text="ล้างข้อมูล", command=clear_entries)
clear_button.grid(row=7, column=0, columnspan=2)

# เริ่มการทำงานของหน้าต่าง Tkinter
window.mainloop()

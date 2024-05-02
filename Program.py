import tkinter as tk

def say_hello():
    label.config(text="Hello, " + entry.get())

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Resizable GUI")

# กำหนดขนาดของหน้าต่าง
root.geometry("400x300")  # กำหนดขนาดเป็น 400x300 พิกเซล

# เพิ่ม Label
label = tk.Label(root, text="Enter your name:")
label.pack()

# เพิ่ม Entry
entry = tk.Entry(root)
entry.pack()

# เพิ่ม Button สำหรับการคลิก
button = tk.Button(root, text="Say Hello", command=say_hello)
button.pack()

# เริ่มการรันโปรแกรม
root.mainloop()

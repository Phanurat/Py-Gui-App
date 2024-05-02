import tkinter as tk

def read_file():
    # เปิดไฟล์
    try:
        with open("pages_link/link.txt", "r") as file:
            # อ่านเนื้อหาจากไฟล์
            file_content = file.read()
            # แสดงเนื้อหาใน Text Widget
            text_widget.delete("1.0", "end")
            text_widget.insert("1.0", file_content)
    except FileNotFoundError:
        text_widget.delete("1.0", "end")
        text_widget.insert("1.0", "File not found!")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Read File GUI")

# เพิ่ม Text Widget สำหรับแสดงเนื้อหาไฟล์
text_widget = tk.Text(root)
text_widget.pack()

# เพิ่ม Button สำหรับอ่านไฟล์และแสดงเนื้อหา
button = tk.Button(root, text="Read File", command=read_file)
button.pack()

# เริ่มการรันโปรแกรม
root.mainloop()

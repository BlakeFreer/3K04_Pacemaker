from tkinter import *
from PIL import ImageTk,Image
 
root = Tk()
root.title(string="DCM")
root_img = PhotoImage(file = "DCM/images/MacFireball.png")
root.iconphoto(False,root_img)
root.geometry ("950x400")
root.configure(bg = "black")

username_input = Entry(root, width = 35, font=("Helvetica", 12))
# username_input.pack(padx = 10, pady = 10)
username_input.insert(0, "Username@example.com")

password_input = Entry(root, show = "*", width = 35, font=("Helvetica", 12))
# password_input.pack(padx = 10, pady = 10)
password_input.insert(0, "Password123")

myButton1 = Button(root, text="Sign In", padx = 30, pady = 5, bg="red")
myButton2 = Button(root, text="Create Account", padx = 30, pady = 5, bg="orange")

fire_img = Image.open("DCM/images/FlameLogo.png")
resized_fire_img = fire_img.resize((500,400))
fire_img = ImageTk.PhotoImage(resized_fire_img)
fire_label = Label(image = fire_img)
# fire_label.pack()

sign_in_canvas = Canvas(root, width = 200, height = 60, bg = "black")
sign_in_canvas.create_text(100, 30, text = "Welcome!", fill = "white", font=('Helvetica 15 bold'))

line_canvas = Canvas(root, width = 325, height = 5, bg = "black")
line_canvas.create_line(0, 5, 325, 5, fill="green", width=5)

fire_label.grid(row = 0, column = 0, rowspan = 6)
sign_in_canvas.grid(row = 0,column = 1, padx = 100, pady = 5)
username_input.grid(row = 1, column = 1, padx = 100, pady = 5)
password_input.grid(row = 2, column = 1, padx = 100, pady = 5)
myButton1.grid(row = 3,column = 1, padx = 100, pady = 5)
line_canvas.grid(row = 4,column = 1, padx = 100)
myButton2.grid(row = 5,column = 1, padx = 100, pady = 5)

root.mainloop()
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import ast


#window initialization
window = Tk()
window.title("Create an account")
window.geometry("950x400")
window.configure(bg='#838383')
window.resizable(False,False)


#Store username/passwords in a text file
def sign_up():
	username_input = username.get()
	password_input = password.get()
	password2_input = password_confirm.get()

	if password_input == password2_input:
		#Read file and write data
		try:
			file = open('database.txt', 'r+')
			r = ast.literal_eval(file.read())

			#store username/password in hashmap
			dictionary = {username_input:password_input}
			r.update(dictionary)
			file.truncate(0)
			file.close()

			file = open('database.txt', 'w')
			w = file.write(str(r))

			messagebox.showinfo('Registration', 'Congratulations! You have successfully signed up.')
		#Create database.txt file
		except:
			file = open('database.txt', 'w')
			dictionary2 = str({'Username':'Password'})
			file.write(dictionary2)
			file.close()

	else:
		messagebox.showerror('Error', "Make sure both passwords match.")


#relocate to sign in 
def sign_in():
	window.destroy()




#Fire logo
fire_img = Image.open("DCM/images/FlameLogo.png")
resized_fire_img = fire_img.resize((500,400))
fire_img = ImageTk.PhotoImage(resized_fire_img)
fire_label = Label(image = fire_img)

fire_label.grid(row = 0, column = 0, rowspan = 6)

frame = Frame(window, width = 350, height = 300, bg = '#fff')
frame.place(x = 555, y = 50)

header = Label(frame, text = 'Register', fg = 'black', bg = 'white', font=('Helvetica 23 bold'))
header.place(x = 100, y = 5)



#Username interface
def user_in(e):
	username.delete(0, 'end')

def user_out(e):
	if username.get() == '':
		username.insert(0, 'Username*')

username = Entry(frame, width = 25, fg = 'black', border = 0, bg = 'white', font=('Helvetica 11 bold'))
username.place(x = 30, y = 80)
username.insert(0, 'Username*')
username.bind("<FocusIn>", user_in)
username.bind("<FocusOut>", user_out)
Frame(frame, width = 295, height = 2, bg = 'black').place(x = 25, y = 107)



#Password interface
def pass_in(e):
	password.delete(0, 'end')

def pass_out(e):
	if password.get() == '':
		password.insert(0, 'Password*')

password = Entry(frame, width = 25, fg = 'black', border = 0, bg = 'white', font=('Helvetica 11 bold'))
password.place(x = 30, y = 150)
password.insert(0, 'Password*')
password.bind("<FocusIn>", pass_in)
password.bind("<FocusOut>", pass_out)
Frame(frame, width = 295, height = 2, bg = 'black').place(x = 25, y = 177)

#Confirm Password
def pass_in(e):
	password_confirm.delete(0, 'end')

def pass_out(e):
	if password_confirm.get() == '':
		password_confirm.insert(0, 'Confirm Password*')

password_confirm = Entry(frame, width = 25, fg = 'black', border = 0, bg = 'white', font=('Helvetica 11 bold'))
password_confirm.place(x = 30, y = 220)
password_confirm.insert(0, 'Confirm Password*')
password_confirm.bind("<FocusIn>", pass_in)
password_confirm.bind("<FocusOut>", pass_out)
Frame(frame, width = 295, height = 2, bg = 'black').place(x = 25, y = 247)





myButton1 = Button(frame, width = 39, pady = 7, text = 'Sign up', bg = 'orange', fg = 'black', border = 0, font = 'Helvetica 9 bold', command = sign_up).place(x = 35, y = 260)
myButton2 = Button(frame, width = 6, text = 'Login', border = 0, bg = 'white', cursor = 'hand2', fg = 'black', font=('Helvetica 9 bold'), command = sign_in).place(x = 300, y = 0)

window.mainloop()
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import ast


#Set interface of window
root = Tk()
root.title(string="DCM")
root_img = PhotoImage(file = "DCM/images/MacFireball.png")
root.iconphoto(False,root_img)
root.geometry ("950x400")
root.configure(bg = "black")
root.resizable(False,False)


#Username interface
def user_in(e):
	username_input.delete(0,'end')

def user_out(e):
	username = username_input.get()
	if username == '':
		username_input.insert(0,'Username@example.com')

username_input = Entry(root, width = 35, font=("Helvetica", 12))
# username_input.pack(padx = 10, pady = 10)
username_input.insert(0, "Username@example.com")
username_input.bind('<FocusIn>', user_in)
username_input.bind('<FocusOut>', user_out)


#Password interface
def pass_in(e):
	password_input.delete(0,'end')

def pass_out(e):
	password = password_input.get()
	if password == '':
		password_input.insert(0,'Password123')

password_input = Entry(root, show = "*", width = 35, font=("Helvetica", 12))
# password_input.pack(padx = 10, pady = 10)
password_input.insert(0, "Password123")
password_input.bind('<FocusIn>', pass_in)
password_input.bind('<FocusOut>', pass_out)

#Sign in
def sign_in():

	username = username_input.get()
	password = password_input.get()

	options = [
		"Off", 
		"DDD", 
		"VDD", 
		"DDI", 
		"DOO", 
		"AOO", 
		"AAI", 
		"VOO", 
		"VVI", 
		"AAT", 
		"VVT", 
		"DDDR", 
		"VDDR", 
		"DDIR", 
		"DOOR", 
		"AOOR", 
		"AAIR", 
		"VOOR", 
		"VVIR"
	]

	clicked = StringVar()
	clicked.set(options[0])


	file = open('database.txt', 'r')
	r = ast.literal_eval(file.read())
	file.close()

	if username in r.keys() and password == r[username]:
		screen = Toplevel(root)
		screen.title("Pacemaker DCM System Dashboard")
		screen.config(bg = "white")
		drop = OptionMenu(screen, clicked, *options)
		drop.pack()

		screen.mainloop()

	else:
		messagebox.showerror("Invalid", "Invalid username/password. Please try again.")

##############################################################################################
#Create Account Buttons
def sign_up_account():

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
				window.destroy()

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

##############################################################################################
myButton1 = Button(root, text="Sign In", padx = 30, pady = 5, bg="red", command = sign_in)
myButton2 = Button(root, text="Create Account", padx = 30, pady = 5, bg="orange", command = sign_up_account)


#Fireball
fire_img = Image.open("DCM/images/FlameLogo.png")
resized_fire_img = fire_img.resize((500,400))
fire_img = ImageTk.PhotoImage(resized_fire_img)
fire_label = Label(image = fire_img)
# fire_label.pack()


#Welcome message
sign_in_canvas = Canvas(root, width = 200, height = 60, bg = "black")
sign_in_canvas.create_text(100, 30, text = "Welcome!", fill = "white", font=('Helvetica 15 bold'))

line_canvas = Canvas(root, width = 325, height = 5, bg = "black")
line_canvas.create_line(0, 5, 325, 5, fill="green", width=5)


#positioning the user interface
fire_label.grid(row = 0, column = 0, rowspan = 6)
sign_in_canvas.grid(row = 0,column = 1, padx = 100, pady = 5)
username_input.grid(row = 1, column = 1, padx = 100, pady = 5)
password_input.grid(row = 2, column = 1, padx = 100, pady = 5)
myButton1.grid(row = 3,column = 1, padx = 100, pady = 5)
line_canvas.grid(row = 4,column = 1, padx = 100)
myButton2.grid(row = 5,column = 1, padx = 100, pady = 5)

root.mainloop()
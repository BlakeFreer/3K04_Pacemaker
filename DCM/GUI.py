from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import ast

# Set interface of welcome window
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
		#username_input.insert(0,'Username@example.com')
		username_input.insert(0,'user')

username_input = Entry(root, width = 35, font=("Helvetica", 12))
# username_input.pack(padx = 10, pady = 10)
#username_input.insert(0, "Username@example.com")
username_input.insert(0, "user")
username_input.bind('<FocusIn>', user_in)
username_input.bind('<FocusOut>', user_out)


#Password interface
def pass_in(e):
	password_input.delete(0,'end')

def pass_out(e):
	password = password_input.get()
	if password == '':
		#password_input.insert(0,'Password123')
		password_input.insert(0,'pass')

password_input = Entry(root, show = "*", width = 35, font=("Helvetica", 12))
# password_input.pack(padx = 10, pady = 10)
#password_input.insert(0, "Password123")
password_input.insert(0, "pass")
password_input.bind('<FocusIn>', pass_in)
password_input.bind('<FocusOut>', pass_out)




#Sign in
def sign_in():
	username = username_input.get()
	password = password_input.get()

	#Values for modes/parameters
	modes = [
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

	LRL = (30, 35, 40, 45, 50, 
		   51, 52, 53, 54, 55, 
		   56, 57, 58, 59, 60, 
		   61, 62, 63, 64, 65, 
		   66, 67, 68, 69, 70, 
		   71, 72, 73, 74, 75, 
		   76, 77, 78, 79, 80, 
	       81, 82, 83, 84, 85, 
	       86, 87, 88, 89, 90, 
		   95, 100, 105, 110, 115, 
		  120, 125, 130, 135, 140, 
	      145, 150, 155, 160, 165, 
		  170, 175) 

	AV_PAR = ("Off", 0.5, 0.6, 0.7, 0.8, 0.9,
				1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 
				1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 
				2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 
			    2.8, 2.9, 3.0, 3.1, 3.2, 3.5, 
			    4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 
			    7.0)

	AV_PW = (0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 
		      0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 
		      1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 
		      1.8, 1.9)


	#drop down menu for modes
	clicked = StringVar()
	clicked.set(modes[0])


	file = open('DCM/database.txt', 'r')
	r = ast.literal_eval(file.read())
	file.close()

	if username in r.keys() and password == r[username]:
		#setting up window interface
		screen = Toplevel(root)
		screen.title("Pacemaker DCM System Dashboard")
		screen.config(bg = "white")
		screen_img = PhotoImage(file = "DCM/images/MacFireball.png")
		screen.iconphoto(False,root_img)

		#mode selection
		drop = OptionMenu(screen, clicked, *modes)
		drop.pack()

		frame = Frame(screen)
		frame.pack()

		parameter_frame = LabelFrame(frame, text = "Parameters", font = ("Helvetica", 20))
		parameter_frame.grid(row = 0, column = 0, padx = 20, pady = 20)

		LRL_label = Label(parameter_frame, text = "Lower Rate Limit (ppm)", font = ("Helvetica", 15))
		URL_label = Label(parameter_frame, text = "Upper Rate Limit (ppm)", font = ("Helvetica", 15))
		APAR_label = Label(parameter_frame, text = "Atrial Pulse Amplitude Regulated (V)", font = ("Helvetica", 15))
		APW_label = Label(parameter_frame, text = "Atrial Pulse Width (ms)", font = ("Helvetica", 15))
		VPAR_label = Label(parameter_frame, text = "Ventricular Pulse Amplitude Regulated (V)", font = ("Helvetica", 15))
		VPW_label = Label(parameter_frame, text = "Ventricular Pulse Width (ms)", font = ("Helvetica", 15))	 
		VRP_label = Label(parameter_frame, text = "Ventricular Refractory Period (ms)", font = ("Helvetica", 15))
		ARP_label = Label(parameter_frame, text = "Atrial Refractory Period (ms)", font = ("Helvetica", 15))

		LRL_spinbox = Spinbox(parameter_frame, values = LRL, font = ("Helvetica", 15))
		URL_spinbox = Spinbox(parameter_frame, from_ = 50, to = 175, increment = 5, font = ("Helvetica", 15))
		APAR_spinbox = Spinbox(parameter_frame, values = AV_PAR, font = ("Helvetica", 15))
		APW_spinbox = Spinbox(parameter_frame, values = AV_PW, increment = 0.1, font = ("Helvetica", 15))
		VPAR_spinbox = Spinbox(parameter_frame, values = AV_PAR, font = ("Helvetica", 15))
		VPW_spinbox = Spinbox(parameter_frame, values = AV_PW, font = ("Helvetica", 15))
		VRP_spinbox = Spinbox(parameter_frame, from_ = 150, to = 500, increment = 10, font = ("Helvetica", 15))
		ARP_spinbox = Spinbox(parameter_frame, from_ = 150, to = 500, increment = 10, font = ("Helvetica", 15))

		def output_params():
			mode = clicked.get()
			LRL = LRL_spinbox.get()
			URL = URL_spinbox.get()
			APAR = APAR_spinbox.get()
			APW = APW_spinbox.get()
			VPAR = VPAR_spinbox.get()
			VPW = VPW_spinbox.get()
			VRP = VRP_spinbox.get()
			ARP = ARP_spinbox.get()

			output_dict = {
				"Mode": mode,
				"LRL": LRL,
				"URL": URL,
				"APAR": APAR,
				"APW": APW,
				"VPAR": VPAR,
				"VPW": VPW,
				"VRP": VRP,
				"ARP": ARP
			}
			#Printing selected parameters 
			print(output_dict)
		
		myButton3 = Button(screen, text="Select", padx = 30, pady = 5, bg="red", command = output_params)


		LRL_label.grid(row = 0, column = 0)
		URL_label.grid(row = 0, column = 1)	
		APAR_label.grid(row = 2, column = 0)
		APW_label.grid(row = 4, column = 0)
		VPAR_label.grid(row = 2, column = 1)
		VPW_label.grid(row = 4, column = 1)
		VRP_label.grid(row = 6, column = 1)
		ARP_label.grid(row = 6, column = 0)

		LRL_spinbox.grid(row = 1, column = 0)
		URL_spinbox.grid(row = 1, column = 1)		
		APAR_spinbox.grid(row = 3, column = 0)
		APW_spinbox.grid(row = 5, column = 0)
		VPAR_spinbox.grid(row = 3, column = 1)
		VPW_spinbox.grid(row = 5, column = 1)
		VRP_spinbox.grid(row = 7, column = 1)
		ARP_spinbox.grid(row = 7, column = 0)
		myButton3.pack()


		#Create padding for spinboxes
		for widget in parameter_frame.winfo_children():
			widget.grid_configure(padx = 10, pady =5)

		screen.mainloop()

	else:
		messagebox.showerror("Invalid", "Invalid username/password. Please try again.")

##############################################################################################
#Create Account Buttons
def sign_up_account():
	#Window interface
	window = Toplevel(root)
	window.title("Create an account")
	window.geometry("950x400")
	window.configure(bg='white')
	window.resizable(False,False)
	window_img = PhotoImage(file = "DCM/images/MacFireball.png")
	window.iconphoto(False,root_img)

	#Store username/passwords in a text file
	def sign_up():
		flag = 0

		username_input = username.get()
		password_input = password.get()
		password2_input = password_confirm.get()


		if password_input == password2_input:
			#Read file and write data
			try:
				file = open('DCM/database.txt', 'r+')
				r = ast.literal_eval(file.read())

				file1 = open('DCM/database.txt', 'r+')
				pre_r = ast.literal_eval(file1.read())
				file1.close()

				dictionary = {username_input:password_input}

				r.update(dictionary)
				file.truncate(0)
				file.close()

				#store username/password in hashmap

				if len(r) < 11:

					if username_input in pre_r:
						flag = 1
						messagebox.showerror('Error', "Unfortunately your account was not created. The provided username already exists.")

					else:
						file = open('DCM/database.txt', 'w')
						w = file.write(str(r))

						messagebox.showinfo('Registration', 'Congratulations! You have successfully signed up.')
						window.destroy()
				else:
					messagebox.showerror('Error', "Unfortunately your account was not created. There are a maximum of 10 members only.")

			#Create database.txt file
			except:
				file = open('DCM/database.txt', 'w')
				dictionary2 = str({'Username':'Password'})
				file.write(dictionary2)
				file.close()

		else:
			messagebox.showerror('Error', "Make sure both passwords match.")

		if (flag == 1):
			file = open('DCM/database.txt', 'w')
			file.write(str(pre_r))
			file.close()


	#relocate to sign in 
	def sign_in():
		window.destroy()



	#signup interface
	img = PhotoImage(file = "DCM/images/heart.png")
	Label(window, image = img, border = 0, bg = 'white').place(x = 50, y = 10)

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


	myButton1 = Button(frame, width = 39, pady = 7, text = 'Sign up', bg = 'pink', fg = 'black', border = 0, font = 'Helvetica 9 bold', command = sign_up).place(x = 35, y = 260)
	myButton2 = Button(frame, width = 6, text = 'Login', border = 0, bg = 'orange', cursor = 'hand2', fg = 'black', font=('Helvetica 9 bold'), command = sign_in).place(x = 300, y = 0)

	window.mainloop()

##############################################################################################
myButton1 = Button(root, text="Sign In", padx = 30, pady = 5, bg="red", command = sign_in)
myButton2 = Button(root, text="Create Account", padx = 30, pady = 5, bg="orange", command = sign_up_account)


#Heart
heart_img = Image.open("DCM/images/heart.png")
resized_heart_img = heart_img.resize((500,400))
heart_img = ImageTk.PhotoImage(resized_heart_img)
heart_label = Label(image = heart_img)


#Welcome message
sign_in_canvas = Canvas(root, width = 200, height = 60, bg = "black")
sign_in_canvas.create_text(100, 30, text = "Welcome!", fill = "white", font=('Helvetica 15 bold'))

line_canvas = Canvas(root, width = 325, height = 5, bg = "black")
line_canvas.create_line(0, 5, 325, 5, fill="green", width=5)


#positioning the user interface
heart_label.grid(row = 0, column = 0, rowspan = 6)
sign_in_canvas.grid(row = 0,column = 1, padx = 100, pady = 5)
username_input.grid(row = 1, column = 1, padx = 100, pady = 5)
password_input.grid(row = 2, column = 1, padx = 100, pady = 5)
myButton1.grid(row = 3,column = 1, padx = 100, pady = 5)
line_canvas.grid(row = 4,column = 1, padx = 100)
myButton2.grid(row = 5,column = 1, padx = 100, pady = 5)

root.mainloop()
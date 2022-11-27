from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import ast
import json
import sys
import serial
import serial.tools.list_ports
import struct
import time
import SerialConverter

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
		username_input.insert(0,'Username@example.com')

username_input = Entry(root, width = 35, font=("Helvetica", 12))
username_input.insert(0, "Username@example.com")
username_input.bind('<FocusIn>', user_in)
username_input.bind('<FocusOut>', user_out)


#Password interface
def pass_in(e):
	password_input.delete(0,'end')

def pass_out(e):
	password = password_input.get()
	if password == '':
		password_input.insert(0,'Password')

password_input = Entry(root, show = "*", width = 35, font=("Helvetica", 12))
password_input.insert(0, "Password123")
password_input.insert(0, "pass")
password_input.bind('<FocusIn>', pass_in)
password_input.bind('<FocusOut>', pass_out)


#Sign in
def sign_in():
	username = username_input.get()
	password = password_input.get()

	#open and read database file
	file = open('DCM/database.txt', 'r')
	r = ast.literal_eval(file.read())
	file.close()

	if username in r.keys():
		f = open(f"DCM/saved/{username}_output.txt", "a")
		f.close()

		with open(f"DCM/saved/{username}_output.txt", "r") as f:
			flag = f.read()
	else:
		flag = ""

	#Values for modes/parameters
	if (flag == ""):
		modes = [
			"Off", 
			"AAT",
			"VVT",
			"AOO",
			"AAI",
			"VOO",
			"VVI",
			"VDD",
			"DOO",
			"DDI",
			"DDD",
			"AOOR",
			"AAIR",
			"VOOR",
			"VVIR",
			"VDDR",
			"DOOR",
			"DDIR",
			"DDDR"
		]
	else:			
		with open(f"DCM/saved/{username}_output.txt",'r',) as file:
			for line in file:
				pass
			last_line = line
			data = line.split(":")

			del data[0]

			for i in range(len(data)):
				data[i] = data[i].split(",", 1)[0]

			data[-1] = data[-1].split("}", 1)[0]

			for i in range(len(data)):
				data[i] = data[i].replace('"', '')
				data[i] = data[i].replace(' ', '')

		modes = [
			"Off", 
			"AAT",
			"VVT",
			"AOO",
			"AAI",
			"VOO",
			"VVI",
			"VDD",
			"DOO",
			"DDI",
			"DDD",
			"AOOR",
			"AAIR",
			"VOOR",
			"VVIR",
			"VDDR",
			"DOOR",
			"DDIR",
			"DDDR"
		]

		for i in range(len(modes)):
			if (modes[i] == data[0]):
				modes[0] = data[0]
				modes[i] = "Off"

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

	AV_delay_offset = ("Off", -10, -20, -30, -40,
						-50, -60, -70, -80, -90, 
						-100)

	AVS = (0.25, 0.5, 0.75, 1, 1.5, 2, 2.5,
		3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 
		7.5, 8, 8.5, 9, 9.5, 10)

	PVARP_ext = ("Off", 50, 100, 150, 200, 250,
				300, 350, 400, 450, 500)

	RS = ("Off",3, 6, 9, 12, 15, 18, 21, 25)

	ATRD = (10, 20, 40, 60, 80, 100, 200, 300,
			400, 500, 600, 700, 800, 900, 1000,
			1100, 1200, 1300, 1400, 1500, 1600, 
			1700, 1800, 1900, 2000)

	#drop down menu for modes
	clicked = StringVar()
	clicked.set(modes[0])

	#open and read database file
	file = open('DCM/database.txt', 'r')
	r = ast.literal_eval(file.read())
	file.close()

	if username in r.keys() and password == r[username]:
		#setting up window interface
		screen = Toplevel(root)
		screen.title("Pacemaker DCM System Dashboard")
		screen.config(bg = "white")
		# screen.geometry ("1500x775")
		screen.resizable(False,False)
		screen_img = PhotoImage(file = "DCM/images/MacFireball.png")
		screen.iconphoto(False,root_img)

		# Serial Connection
		com = 'COM4'
		speed = 115200

		try:
			# Initialize Serial connecton
			serie = serial.Serial(port=com,baudrate=speed, timeout=10)
			print("CONNECTED TO " + com)
			serie.flush()
			con_status = True
		except:
			# Error in creating a Serial connection
			print("An error occured: unable to open the specified port " + com)
			con_status = False

		# Checking connection status
		con_canvas = Canvas(screen, width = 80, height = 30, bg = "#FAF9F6")
		con_canvas.create_text(42, 18, text = "Connected!", fill = "green", font=('Helvetica 10 bold'))
		con_canvas.pack()

		if (con_status == False):
			discon_canvas = Canvas(screen, width = 96, height = 30, bg = "#FAF9F6")
			discon_canvas.create_text(50, 18, text = "Disconnected!", fill = "red", font=('Helvetica 10 bold'))
			discon_canvas.place(x = 670, y = 0)
			# discon_canvas.place(x = 697, y = 0)

		def sel_mode(pos_arg):
			# Showing relevant parameters for selected mode
			if (clicked.get() == "Off"):
				LRL_spinbox.configure(state = "disabled")
				URL_spinbox.configure(state = "disabled")
				MSR_spinbox.configure(state = "disabled")
				FAD_spinbox.configure(state = "disabled")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "disabled")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "disabled")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "disabled")
				VPW_spinbox.configure(state = "disabled")
				AS_spinbox.configure(state = "disabled")
				VS_spinbox.configure(state = "disabled")
				VRP_spinbox.configure(state = "disabled")
				ARP_spinbox.configure(state = "disabled")
				PVARP_spinbox.configure(state = "disabled")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "disabled")
				RT_spinbox.configure(state = "disabled")
				RF_spinbox.configure(state = "disabled")
				RecT_spinbox.configure(state = "disabled")

			if (clicked.get() == "AAT"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "disabled")
				FAD_spinbox.configure(state = "disabled")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "readonly")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "disabled")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "readonly")
				VPW_spinbox.configure(state = "disabled")
				AS_spinbox.configure(state = "disabled")
				VS_spinbox.configure(state = "disabled")
				VRP_spinbox.configure(state = "disabled")
				ARP_spinbox.configure(state = "readonly")
				PVARP_spinbox.configure(state = "readonly")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "disabled")
				RT_spinbox.configure(state = "disabled")
				RF_spinbox.configure(state = "disabled")
				RecT_spinbox.configure(state = "disabled")

			if (clicked.get() == "VVT"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "disabled")
				FAD_spinbox.configure(state = "disabled")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "disabled")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "readonly")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "disabled")
				VPW_spinbox.configure(state = "readonly")
				AS_spinbox.configure(state = "disabled")
				VS_spinbox.configure(state = "readonly")
				VRP_spinbox.configure(state = "readonly")
				ARP_spinbox.configure(state = "disabled")
				PVARP_spinbox.configure(state = "disabled")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "disabled")
				RT_spinbox.configure(state = "disabled")
				RF_spinbox.configure(state = "disabled")
				RecT_spinbox.configure(state = "disabled")

			if (clicked.get() == "AOO"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "disabled")
				FAD_spinbox.configure(state = "disabled")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "readonly")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "disabled")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "readonly")
				VPW_spinbox.configure(state = "disabled")
				AS_spinbox.configure(state = "disabled")
				VS_spinbox.configure(state = "disabled")
				VRP_spinbox.configure(state = "disabled")
				ARP_spinbox.configure(state = "disabled")
				PVARP_spinbox.configure(state = "disabled")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "disabled")
				RT_spinbox.configure(state = "disabled")
				RF_spinbox.configure(state = "disabled")
				RecT_spinbox.configure(state = "disabled")

			if (clicked.get() == "AAI"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "disabled")
				FAD_spinbox.configure(state = "disabled")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "readonly")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "disabled")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "readonly")
				VPW_spinbox.configure(state = "disabled")
				AS_spinbox.configure(state = "readonly")
				VS_spinbox.configure(state = "disabled")
				VRP_spinbox.configure(state = "disabled")
				ARP_spinbox.configure(state = "readonly")
				PVARP_spinbox.configure(state = "readonly")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "disabled")
				RT_spinbox.configure(state = "disabled")
				RF_spinbox.configure(state = "disabled")
				RecT_spinbox.configure(state = "disabled")

			if (clicked.get() == "VOO"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "disabled")
				FAD_spinbox.configure(state = "disabled")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "disabled")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "readonly")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "disabled")
				VPW_spinbox.configure(state = "readonly")
				AS_spinbox.configure(state = "disabled")
				VS_spinbox.configure(state = "disabled")
				VRP_spinbox.configure(state = "disabled")
				ARP_spinbox.configure(state = "disabled")
				PVARP_spinbox.configure(state = "disabled")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "disabled")
				RT_spinbox.configure(state = "disabled")
				RF_spinbox.configure(state = "disabled")
				RecT_spinbox.configure(state = "disabled")
			
			if (clicked.get() == "VVI"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "disabled")
				FAD_spinbox.configure(state = "disabled")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "disabled")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "readonly")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "disabled")
				VPW_spinbox.configure(state = "readonly")
				AS_spinbox.configure(state = "disabled")
				VS_spinbox.configure(state = "readonly")
				VRP_spinbox.configure(state = "readonly")
				ARP_spinbox.configure(state = "disabled")
				PVARP_spinbox.configure(state = "disabled")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "disabled")
				RT_spinbox.configure(state = "disabled")
				RF_spinbox.configure(state = "disabled")
				RecT_spinbox.configure(state = "disabled")

			if (clicked.get() == "VDD"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "disabled")
				FAD_spinbox.configure(state = "readonly")
				DAD_spinbox.configure(state = "readonly")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "disabled")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "readonly")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "disabled")
				VPW_spinbox.configure(state = "readonly")
				AS_spinbox.configure(state = "disabled")
				VS_spinbox.configure(state = "readonly")
				VRP_spinbox.configure(state = "readonly")
				ARP_spinbox.configure(state = "disabled")
				PVARP_spinbox.configure(state = "disabled")
				PVARPE_spinbox.configure(state = "readonly")
				ATRFM_spinbox.configure(state = "readonly")
				ATRD_spinbox.configure(state = "readonly")
				ATRFT_spinbox.configure(state = "readonly")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "disabled")
				RT_spinbox.configure(state = "disabled")
				RF_spinbox.configure(state = "disabled")
				RecT_spinbox.configure(state = "disabled")

			if (clicked.get() == "DOO"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "disabled")
				FAD_spinbox.configure(state = "readonly")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "readonly")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "readonly")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "readonly")
				VPW_spinbox.configure(state = "readonly")
				AS_spinbox.configure(state = "disabled")
				VS_spinbox.configure(state = "disabled")
				VRP_spinbox.configure(state = "disabled")
				ARP_spinbox.configure(state = "disabled")
				PVARP_spinbox.configure(state = "disabled")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "disabled")
				RT_spinbox.configure(state = "disabled")
				RF_spinbox.configure(state = "disabled")
				RecT_spinbox.configure(state = "disabled")

			if (clicked.get() == "DDI"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "disabled")
				FAD_spinbox.configure(state = "readonly")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "readonly")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "readonly")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "readonly")
				VPW_spinbox.configure(state = "readonly")
				AS_spinbox.configure(state = "readonly")
				VS_spinbox.configure(state = "readonly")
				VRP_spinbox.configure(state = "readonly")
				ARP_spinbox.configure(state = "readonly")
				PVARP_spinbox.configure(state = "readonly")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "disabled")
				RT_spinbox.configure(state = "disabled")
				RF_spinbox.configure(state = "disabled")
				RecT_spinbox.configure(state = "disabled")

			if (clicked.get() == "DDD"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "disabled")
				FAD_spinbox.configure(state = "readonly")
				DAD_spinbox.configure(state = "readonly")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "readonly")
				APAR_spinbox.configure(state = "readonly")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "readonly")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "readonly")
				VPW_spinbox.configure(state = "readonly")
				AS_spinbox.configure(state = "readonly")
				VS_spinbox.configure(state = "readonly")
				VRP_spinbox.configure(state = "readonly")
				ARP_spinbox.configure(state = "readonly")
				PVARP_spinbox.configure(state = "readonly")
				PVARPE_spinbox.configure(state = "readonly")
				ATRFM_spinbox.configure(state = "readonly")
				ATRD_spinbox.configure(state = "readonly")
				ATRFT_spinbox.configure(state = "readonly")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "disabled")
				RT_spinbox.configure(state = "disabled")
				RF_spinbox.configure(state = "disabled")
				RecT_spinbox.configure(state = "disabled")

			if (clicked.get() == "AOOR"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "readonly")
				FAD_spinbox.configure(state = "disabled")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "readonly")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "disabled")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "readonly")
				VPW_spinbox.configure(state = "disabled")
				AS_spinbox.configure(state = "disabled")
				VS_spinbox.configure(state = "disabled")
				VRP_spinbox.configure(state = "disabled")
				ARP_spinbox.configure(state = "disabled")
				PVARP_spinbox.configure(state = "disabled")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "readonly")
				RT_spinbox.configure(state = "readonly")
				RF_spinbox.configure(state = "readonly")
				RecT_spinbox.configure(state = "readonly")

			if (clicked.get() == "AAIR"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "readonly")
				FAD_spinbox.configure(state = "disabled")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "readonly")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "disabled")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "readonly")
				VPW_spinbox.configure(state = "disabled")
				AS_spinbox.configure(state = "readonly")
				VS_spinbox.configure(state = "disabled")
				VRP_spinbox.configure(state = "disabled")
				ARP_spinbox.configure(state = "readonly")
				PVARP_spinbox.configure(state = "readonly")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "readonly")
				RT_spinbox.configure(state = "readonly")
				RF_spinbox.configure(state = "readonly")
				RecT_spinbox.configure(state = "readonly")

			if (clicked.get() == "VOOR"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "readonly")
				FAD_spinbox.configure(state = "disabled")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "disabled")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "readonly")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "disabled")
				VPW_spinbox.configure(state = "readonly")
				AS_spinbox.configure(state = "disabled")
				VS_spinbox.configure(state = "disabled")
				VRP_spinbox.configure(state = "disabled")
				ARP_spinbox.configure(state = "disabled")
				PVARP_spinbox.configure(state = "disabled")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "readonly")
				RT_spinbox.configure(state = "readonly")
				RF_spinbox.configure(state = "readonly")
				RecT_spinbox.configure(state = "readonly")

			if (clicked.get() == "VVIR"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "readonly")
				FAD_spinbox.configure(state = "disabled")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "disabled")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "readonly")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "disabled")
				VPW_spinbox.configure(state = "readonly")
				AS_spinbox.configure(state = "disabled")
				VS_spinbox.configure(state = "readonly")
				VRP_spinbox.configure(state = "readonly")
				ARP_spinbox.configure(state = "disabled")
				PVARP_spinbox.configure(state = "disabled")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "readonly")
				RT_spinbox.configure(state = "readonly")
				RF_spinbox.configure(state = "readonly")
				RecT_spinbox.configure(state = "readonly")

			if (clicked.get() == "VDDR"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "readonly")
				FAD_spinbox.configure(state = "readonly")
				DAD_spinbox.configure(state = "readonly")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "disabled")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "readonly")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "disabled")
				VPW_spinbox.configure(state = "readonly")
				AS_spinbox.configure(state = "disabled")
				VS_spinbox.configure(state = "readonly")
				VRP_spinbox.configure(state = "readonly")
				ARP_spinbox.configure(state = "disabled")
				PVARP_spinbox.configure(state = "disabled")
				PVARPE_spinbox.configure(state = "readonly")
				ATRFM_spinbox.configure(state = "readonly")
				ATRD_spinbox.configure(state = "readonly")
				ATRFT_spinbox.configure(state = "readonly")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "readonly")
				RT_spinbox.configure(state = "readonly")
				RF_spinbox.configure(state = "readonly")
				RecT_spinbox.configure(state = "readonly")

			if (clicked.get() == "DOOR"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "readonly")
				FAD_spinbox.configure(state = "readonly")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "readonly")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "readonly")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "readonly")
				VPW_spinbox.configure(state = "readonly")
				AS_spinbox.configure(state = "disabled")
				VS_spinbox.configure(state = "disabled")
				VRP_spinbox.configure(state = "disabled")
				ARP_spinbox.configure(state = "disabled")
				PVARP_spinbox.configure(state = "disabled")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "readonly")
				RT_spinbox.configure(state = "readonly")
				RF_spinbox.configure(state = "readonly")
				RecT_spinbox.configure(state = "readonly")

			if (clicked.get() == "DDIR"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "readonly")
				FAD_spinbox.configure(state = "readonly")
				DAD_spinbox.configure(state = "disabled")
				MDAD_spinbox.configure(state = "disabled")
				SADO_spinbox.configure(state = "disabled")
				APAR_spinbox.configure(state = "readonly")
				APAU_spinbox.configure(state = "disabled")
				VPAR_spinbox.configure(state = "readonly")
				VPAU_spinbox.configure(state = "disabled")
				APW_spinbox.configure(state = "readonly")
				VPW_spinbox.configure(state = "readonly")
				AS_spinbox.configure(state = "readonly")
				VS_spinbox.configure(state = "readonly")
				VRP_spinbox.configure(state = "readonly")
				ARP_spinbox.configure(state = "readonly")
				PVARP_spinbox.configure(state = "readonly")
				PVARPE_spinbox.configure(state = "disabled")
				ATRFM_spinbox.configure(state = "disabled")
				ATRD_spinbox.configure(state = "disabled")
				ATRFT_spinbox.configure(state = "disabled")
				VB_spinbox.configure(state = "disabled")
				AT_spinbox.configure(state = "readonly")
				RT_spinbox.configure(state = "readonly")
				RF_spinbox.configure(state = "readonly")
				RecT_spinbox.configure(state = "readonly")

			if (clicked.get() == "DDDR"):
				LRL_spinbox.configure(state = "readonly")
				URL_spinbox.configure(state = "readonly")
				MSR_spinbox.configure(state = "readonly")
				FAD_spinbox.configure(state = "readonly")
				DAD_spinbox.configure(state = "readonly")
				MDAD_spinbox.configure(state = "readonly")
				SADO_spinbox.configure(state = "readonly")
				APAR_spinbox.configure(state = "readonly")
				APAU_spinbox.configure(state = "readonly")
				VPAR_spinbox.configure(state = "readonly")
				VPAU_spinbox.configure(state = "readonly")
				APW_spinbox.configure(state = "readonly")
				VPW_spinbox.configure(state = "readonly")
				AS_spinbox.configure(state = "readonly")
				VS_spinbox.configure(state = "readonly")
				VRP_spinbox.configure(state = "readonly")
				ARP_spinbox.configure(state = "readonly")
				PVARP_spinbox.configure(state = "readonly")
				PVARPE_spinbox.configure(state = "readonly")
				ATRFM_spinbox.configure(state = "readonly")
				ATRD_spinbox.configure(state = "readonly")
				ATRFT_spinbox.configure(state = "readonly")
				VB_spinbox.configure(state = "readonly")
				AT_spinbox.configure(state = "readonly")
				RT_spinbox.configure(state = "readonly")
				RF_spinbox.configure(state = "readonly")
				RecT_spinbox.configure(state = "readonly")

		#mode selection
		drop = OptionMenu(screen, clicked, *modes, command = sel_mode)
		drop.pack()

		#frame for parameters
		frame = Frame(screen)
		frame.pack()

		parameter_frame = LabelFrame(frame, text = "Parameters", font = ("Helvetica", 20))
		parameter_frame.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = 20)

		#Parameter labels
		LRL_label = Label(parameter_frame, text = "Lower Rate Limit (ppm)", font = ("Helvetica", 15))
		URL_label = Label(parameter_frame, text = "Upper Rate Limit (ppm)", font = ("Helvetica", 15))
		MSR_label = Label(parameter_frame, text = "Maximum Sensor Rate (ppm)", font = ("Helvetica", 15))
		FAD_label = Label(parameter_frame, text = "Fixed AV Delay (ms)", font = ("Helvetica", 15))
		DAD_label = Label(parameter_frame, text = "Dynamic AV Delay (ms)", font = ("Helvetica", 15))
		MDAD_label = Label(parameter_frame, text = "Minimum Dynamic AV Delay (ms)", font = ("Helvetica", 15))
		SADO_label = Label(parameter_frame, text = "Sensed AV Delay Offset (ms)", font = ("Helvetica", 15))
		APAR_label = Label(parameter_frame, text = "Atrial Pulse Amplitude Regulated (V)", font = ("Helvetica", 15))
		APAU_label = Label(parameter_frame, text = "APA Unregulated (V)", font = ("Helvetica", 15))
		VPAR_label = Label(parameter_frame, text = "Ventricular Pulse Amplitude Regulated (V)", font = ("Helvetica", 15))
		VPAU_label = Label(parameter_frame, text = "VPA Unregulated (V)", font = ("Helvetica", 15))
		APW_label = Label(parameter_frame, text = "Atrial Pulse Width (ms)", font = ("Helvetica", 15))
		VPW_label = Label(parameter_frame, text = "Ventricular Pulse Width (ms)", font = ("Helvetica", 15))
		AS_label = Label(parameter_frame, text = "Atrial Sensitivity (mV)", font = ("Helvetica", 15))
		VS_label = Label(parameter_frame, text = "Ventricular Sensitivity (mV)", font = ("Helvetica", 15))
		VRP_label = Label(parameter_frame, text = "Ventricular Refractory Period (ms)", font = ("Helvetica", 15))
		ARP_label = Label(parameter_frame, text = "Atrial Refractory Period (ms)", font = ("Helvetica", 15))
		PVARP_label = Label(parameter_frame, text = "Post Ventricular Atrial Refractory Period (ms)", font = ("Helvetica", 15))
		PVARPE_label = Label(parameter_frame, text = "PVARP Extension (ms)", font = ("Helvetica", 15))
		ATRFM_label = Label(parameter_frame, text = "Atrial Tachycardia Response Fallback Mode", font = ("Helvetica", 15))
		ATRD_label = Label(parameter_frame, text = "ATR Duration (cc)", font = ("Helvetica", 15))
		ATRFT_label = Label(parameter_frame, text = "ATR Fallback Time (min)", font = ("Helvetica", 15))
		VB_label = Label(parameter_frame, text = "Ventricular Blanking (ms)", font = ("Helvetica", 15))
		AT_label = Label(parameter_frame, text = "Activity Threshold", font = ("Helvetica", 15))
		RT_label = Label(parameter_frame, text = "Reaction Time (s)", font = ("Helvetica", 15))
		RF_label = Label(parameter_frame, text = "Response Factor", font = ("Helvetica", 15))
		RecT_label = Label(parameter_frame, text = "Recovery Time (min)", font = ("Helvetica", 15))

		#Parameter spinboxes

		if (flag == ""):
			LRL_spinbox = Spinbox(parameter_frame, values = LRL, font = ("Helvetica", 15))
			URL_spinbox = Spinbox(parameter_frame, from_ = 50, to = 175, increment = 5, font = ("Helvetica", 15))
			MSR_spinbox = Spinbox(parameter_frame, from_ = 50, to = 175, increment = 5, font = ("Helvetica", 15))
			FAD_spinbox = Spinbox(parameter_frame, from_ = 70, to = 300, increment = 5, font = ("Helvetica", 15))
			DAD_spinbox = Spinbox(parameter_frame, values = ("Off", "On"), font = ("Helvetica", 15))
			MDAD_spinbox = Spinbox(parameter_frame, from_ = 30, to = 100, increment = 10, font = ("Helvetica", 15))
			SADO_spinbox = Spinbox(parameter_frame, values = AV_delay_offset, font = ("Helvetica", 15))
			APAR_spinbox = Spinbox(parameter_frame, values = AV_PAR, font = ("Helvetica", 15))
			APAU_spinbox = Spinbox(parameter_frame, values = ("Off", 1.25, 2.5, 3.75, 5), font = ("Helvetica", 15))
			VPAR_spinbox = Spinbox(parameter_frame, values = AV_PAR, font = ("Helvetica", 15))
			VPAU_spinbox = Spinbox(parameter_frame, values = ("Off", 1.25, 2.5, 3.75, 5), font = ("Helvetica", 15))
			APW_spinbox = Spinbox(parameter_frame, values = AV_PW, increment = 0.1, font = ("Helvetica", 15))
			VPW_spinbox = Spinbox(parameter_frame, values = AV_PW, font = ("Helvetica", 15))
			AS_spinbox = Spinbox(parameter_frame, values = AVS, font = ("Helvetica", 15))
			VS_spinbox = Spinbox(parameter_frame, values = AVS, font = ("Helvetica", 15))
			VRP_spinbox = Spinbox(parameter_frame, from_ = 150, to = 500, increment = 10, font = ("Helvetica", 15))
			ARP_spinbox = Spinbox(parameter_frame, from_ = 150, to = 500, increment = 10, font = ("Helvetica", 15))
			PVARP_spinbox = Spinbox(parameter_frame, from_ = 150, to = 500, increment = 10, font = ("Helvetica", 15))
			PVARPE_spinbox = Spinbox(parameter_frame, values = PVARP_ext, font = ("Helvetica", 15))
			ATRFM_spinbox = Spinbox(parameter_frame, values = ("On", "Off"), font = ("Helvetica", 15))
			ATRD_spinbox = Spinbox(parameter_frame, values = ATRD, font = ("Helvetica", 15))
			ATRFT_spinbox = Spinbox(parameter_frame, from_ = 1, to = 5, increment = 1, font = ("Helvetica", 15))
			VB_spinbox = Spinbox(parameter_frame, from_ = 30, to = 60, increment = 10, font = ("Helvetica", 15))
			AT_spinbox = Spinbox(parameter_frame, values = ("V-Low", "Low", "Med-Low", "Med", "Med-High", "High", "V-High"), font = ("Helvetica", 15))
			RT_spinbox = Spinbox(parameter_frame, from_ = 10, to = 50, increment = 10, font = ("Helvetica", 15))
			RF_spinbox = Spinbox(parameter_frame, from_ = 1, to = 16, increment = 1, font = ("Helvetica", 15))
			RecT_spinbox = Spinbox(parameter_frame, from_ = 2, to = 16, increment = 1, font = ("Helvetica", 15))

		else:
			LRL_spinbox = Spinbox(parameter_frame, values = LRL, font = ("Helvetica", 15))
			LRL_spinbox.delete(0,END)
			LRL_spinbox.insert(0, data[1])

			URL_spinbox = Spinbox(parameter_frame, from_ = 50, to = 175, increment = 5, font = ("Helvetica", 15))
			URL_spinbox.delete(0,END)
			URL_spinbox.insert(0, data[2])

			MSR_spinbox = Spinbox(parameter_frame, from_ = 50, to = 175, increment = 5, font = ("Helvetica", 15))
			MSR_spinbox.delete(0,END)
			MSR_spinbox.insert(0, data[3])

			FAD_spinbox = Spinbox(parameter_frame, from_ = 70, to = 300, increment = 5, font = ("Helvetica", 15))
			FAD_spinbox.delete(0,END)
			FAD_spinbox.insert(0, data[4])

			DAD_spinbox = Spinbox(parameter_frame, values = ("Off", "On"), font = ("Helvetica", 15))
			DAD_spinbox.delete(0,END)
			DAD_spinbox.insert(0, data[5])

			MDAD_spinbox = Spinbox(parameter_frame, from_ = 30, to = 100, increment = 10, font = ("Helvetica", 15))
			MDAD_spinbox.delete(0,END)
			MDAD_spinbox.insert(0, data[6])

			SADO_spinbox = Spinbox(parameter_frame, values = AV_delay_offset, font = ("Helvetica", 15))
			SADO_spinbox.delete(0,END)
			SADO_spinbox.insert(0, data[7])

			APAR_spinbox = Spinbox(parameter_frame, values = AV_PAR, font = ("Helvetica", 15))
			APAR_spinbox.delete(0,END)
			APAR_spinbox.insert(0, data[8])

			APAU_spinbox = Spinbox(parameter_frame, values = ("Off", 1.25, 2.5, 3.75, 5), font = ("Helvetica", 15))
			APAU_spinbox.delete(0,END)
			APAU_spinbox.insert(0, data[9])

			VPAR_spinbox = Spinbox(parameter_frame, values = AV_PAR, font = ("Helvetica", 15))
			VPAR_spinbox.delete(0,END)
			VPAR_spinbox.insert(0, data[10])

			VPAU_spinbox = Spinbox(parameter_frame, values = ("Off", 1.25, 2.5, 3.75, 5), font = ("Helvetica", 15))
			VPAU_spinbox.delete(0,END)
			VPAU_spinbox.insert(0, data[11])

			APW_spinbox = Spinbox(parameter_frame, values = AV_PW, increment = 0.1, font = ("Helvetica", 15))
			APW_spinbox.delete(0,END)
			APW_spinbox.insert(0, data[12])

			VPW_spinbox = Spinbox(parameter_frame, values = AV_PW, font = ("Helvetica", 15))
			VPW_spinbox.delete(0,END)
			VPW_spinbox.insert(0, data[13])

			AS_spinbox = Spinbox(parameter_frame, values = AVS, font = ("Helvetica", 15))
			AS_spinbox.delete(0,END)
			AS_spinbox.insert(0, data[14])

			VS_spinbox = Spinbox(parameter_frame, values = AVS, font = ("Helvetica", 15))
			VS_spinbox.delete(0,END)
			VS_spinbox.insert(0, data[15])

			VRP_spinbox = Spinbox(parameter_frame, from_ = 150, to = 500, increment = 10, font = ("Helvetica", 15))
			VRP_spinbox.delete(0,END)
			VRP_spinbox.insert(0, data[16])

			ARP_spinbox = Spinbox(parameter_frame, from_ = 150, to = 500, increment = 10, font = ("Helvetica", 15))
			ARP_spinbox.delete(0,END)
			ARP_spinbox.insert(0, data[17])

			PVARP_spinbox = Spinbox(parameter_frame, from_ = 150, to = 500, increment = 10, font = ("Helvetica", 15))
			PVARP_spinbox.delete(0,END)
			PVARP_spinbox.insert(0, data[18])

			PVARPE_spinbox = Spinbox(parameter_frame, values = PVARP_ext, font = ("Helvetica", 15))
			PVARPE_spinbox.delete(0,END)
			PVARPE_spinbox.insert(0, data[19])

			ATRFM_spinbox = Spinbox(parameter_frame, values = ("On", "Off"), font = ("Helvetica", 15))
			ATRFM_spinbox.delete(0,END)
			ATRFM_spinbox.insert(0, data[20])

			ATRD_spinbox = Spinbox(parameter_frame, values = ATRD, font = ("Helvetica", 15))
			ATRD_spinbox.delete(0,END)
			ATRD_spinbox.insert(0, data[21])

			ATRFT_spinbox = Spinbox(parameter_frame, from_ = 1, to = 5, increment = 1, font = ("Helvetica", 15))
			ATRFT_spinbox.delete(0,END)
			ATRFT_spinbox.insert(0, data[22])

			VB_spinbox = Spinbox(parameter_frame, from_ = 30, to = 60, increment = 10, font = ("Helvetica", 15))
			VB_spinbox.delete(0,END)
			VB_spinbox.insert(0, data[23])

			AT_spinbox = Spinbox(parameter_frame, values = ("V-Low", "Low", "Med-Low", "Med", "Med-High", "High", "V-High"), font = ("Helvetica", 15))
			AT_spinbox.delete(0,END)
			AT_spinbox.insert(0, data[24])

			RT_spinbox = Spinbox(parameter_frame, from_ = 10, to = 50, increment = 10, font = ("Helvetica", 15))
			RT_spinbox.delete(0,END)
			RT_spinbox.insert(0, data[25])

			RF_spinbox = Spinbox(parameter_frame, from_ = 1, to = 16, increment = 1, font = ("Helvetica", 15))
			RF_spinbox.delete(0,END)
			RF_spinbox.insert(0, data[26])

			RecT_spinbox = Spinbox(parameter_frame, from_ = 2, to = 16, increment = 1, font = ("Helvetica", 15))
			RecT_spinbox.delete(0,END)
			RecT_spinbox.insert(0, data[27])

		# Turning parameters off by default until a mode is selected
		LRL_spinbox.configure(state = "disabled")
		URL_spinbox.configure(state = "disabled")
		MSR_spinbox.configure(state = "disabled")
		FAD_spinbox.configure(state = "disabled")
		DAD_spinbox.configure(state = "disabled")
		MDAD_spinbox.configure(state = "disabled")
		SADO_spinbox.configure(state = "disabled")
		APAR_spinbox.configure(state = "disabled")
		APAU_spinbox.configure(state = "disabled")
		VPAR_spinbox.configure(state = "disabled")
		VPAU_spinbox.configure(state = "disabled")
		APW_spinbox.configure(state = "disabled")
		VPW_spinbox.configure(state = "disabled")
		AS_spinbox.configure(state = "disabled")
		VS_spinbox.configure(state = "disabled")
		VRP_spinbox.configure(state = "disabled")
		ARP_spinbox.configure(state = "disabled")
		PVARP_spinbox.configure(state = "disabled")
		PVARPE_spinbox.configure(state = "disabled")
		ATRFM_spinbox.configure(state = "disabled")
		ATRD_spinbox.configure(state = "disabled")
		ATRFT_spinbox.configure(state = "disabled")
		VB_spinbox.configure(state = "disabled")
		AT_spinbox.configure(state = "disabled")
		RT_spinbox.configure(state = "disabled")
		RF_spinbox.configure(state = "disabled")
		RecT_spinbox.configure(state = "disabled")


		#print output of selected parameters
		def output_params():
			mode = clicked.get()
			LRL = LRL_spinbox.get()
			URL = URL_spinbox.get()
			MSR = MSR_spinbox.get()
			FAD = FAD_spinbox.get()
			DAD = DAD_spinbox.get()
			MDAD = MDAD_spinbox.get()
			SADO = SADO_spinbox.get()
			APAR = APAR_spinbox.get()
			APAU = APAU_spinbox.get()
			VPAR = VPAR_spinbox.get()
			VPAU = VPAU_spinbox.get()
			APW = APW_spinbox.get()
			VPW = VPW_spinbox.get()
			AS = AS_spinbox.get()
			VS = VS_spinbox.get()
			VRP = VRP_spinbox.get()
			ARP = ARP_spinbox.get()
			PVARP = PVARP_spinbox.get()
			PVARPE = PVARPE_spinbox.get()
			ATRFM = ATRFM_spinbox.get()
			ATRD = ATRD_spinbox.get()
			ATRFT = ATRFT_spinbox.get()
			VB = VB_spinbox.get()
			AT = AT_spinbox.get()
			RT = RT_spinbox.get()
			RF = RF_spinbox.get()
			RecT = RecT_spinbox.get()

			# Restrictions between parameters
			if (int(LRL) >= int(URL)):
				messagebox.showerror("Invalid Parameters", "Lower Rate Limit must be less than upper rate limit. Please try again.")

			elif(int(VRP) > 60000/int(URL) - 50 or int(ARP) > 60000/int(URL) - 50):
				messagebox.showerror("Invalid Parameters", "Refractory Period must be lowered to give time for the pacemaker to detect the heart's natural freqeuncy. Please try again.")
			
			else:
				output_dict = {
					"Mode": mode,
					"LRL": LRL,
					"URL": URL,
					"MSR": MSR,
					"FAD": FAD,
					"DAD": DAD,
					"MDAD": MDAD,
					"SADO": SADO,
					"APAR": APAR,
					"APAU": APAU,
					"VPAR": VPAR,
					"VPAU": VPAU,
					"APW": APW,
					"VPW": VPW,
					"AS": AS,
					"VS": VS,
					"VRP": VRP,
					"ARP": ARP,
					"PVARP": PVARP,
					"PVARPE": PVARPE,
					"ATRFM": ATRFM,
					"ATRD": ATRD,
					"ATRFT": ATRFT,
					"VB": VB,
					"AT": AT,
					"RT": RT,
					"RF": RF,
					"RecT": RecT
				}

				#Outputting selected parameters to text file
				with open(f"DCM/saved/{username}_output.txt", "a") as f:
					output_str = json.dumps(output_dict)
					f.write(output_str + "\n")
			
			if (con_status == False):
				messagebox.showerror("Connection Error", "Parameters are saved, please log in again with the pacemaker connected to send data")
			else:
				messagebox.showinfo("Success", "Parameters were succesfully sent!")
				serial.write(bytearray(SerialConverter.ConvertData(dict)))
					
		def graph_data():
			pass

		# Creating submit button wth associated command
		myButton3 = Button(frame, text="Submit", padx = 30, pady = 5, bg="red", activebackground = "green", command = output_params)

		# Creating Electrogram Graph with assocated command
		myButton5 = Button(frame, text="Electrogram", padx = 30, pady = 5, bg="red", activebackground = "green", command = graph_data)
		
		myButton3.grid(row = 1, column = 0)
		myButton5.grid(row = 1, column = 1)

		try:
			myButton3.bind('<Destroy>', close_serial(serie))
		except:
			pass

		# Position parameter labels
		LRL_label.grid(row = 0, column = 0)
		URL_label.grid(row = 0, column = 1)	
		MSR_label.grid(row = 0, column = 2)
		FAD_label.grid(row = 0, column = 3)
		DAD_label.grid(row = 2, column = 0)
		MDAD_label.grid(row = 2, column = 1)
		SADO_label.grid(row = 2, column = 2)
		APAR_label.grid(row = 2, column = 3)
		APAU_label.grid(row = 4, column = 0)
		VPAR_label.grid(row = 4, column = 1)
		VPAU_label.grid(row = 4, column = 2)
		APW_label.grid(row = 4, column = 3)
		VPW_label.grid(row = 6, column = 0)
		AS_label.grid(row = 6, column = 1)
		VS_label.grid(row = 6,column = 2)
		VRP_label.grid(row = 6, column = 3)
		ARP_label.grid(row = 8, column = 0)
		PVARP_label.grid(row = 8, column = 1)
		PVARPE_label.grid(row = 8, column = 2)
		ATRFM_label.grid(row = 8, column = 3)
		ATRD_label.grid(row = 10, column = 0)
		ATRFT_label.grid(row = 10, column = 1)
		VB_label.grid(row = 10, column = 2)
		AT_label.grid(row = 10, column = 3)
		RT_label.grid(row = 12, column = 0)
		RF_label.grid(row = 12, column = 1)
		RecT_label.grid(row = 12, column = 2)
		 
		# Position parameter spinboxes
		LRL_spinbox.grid(row = 1, column = 0)
		URL_spinbox.grid(row = 1, column = 1)		
		MSR_spinbox.grid(row = 1, column = 2)
		FAD_spinbox.grid(row = 1, column = 3)
		DAD_spinbox.grid(row = 3, column = 0)
		MDAD_spinbox.grid(row = 3, column = 1)
		SADO_spinbox.grid(row = 3, column = 2)
		APAR_spinbox.grid(row = 3, column = 3)
		APAU_spinbox.grid(row = 5, column = 0)
		VPAR_spinbox.grid(row = 5, column = 1)
		VPAU_spinbox.grid(row = 5, column = 2)
		APW_spinbox.grid(row = 5, column = 3)
		VPW_spinbox.grid(row = 7, column = 0)
		AS_spinbox.grid(row = 7, column = 1)
		VS_spinbox.grid(row = 7, column = 2)
		VRP_spinbox.grid(row = 7, column = 3)
		ARP_spinbox.grid(row = 9, column = 0)
		PVARP_spinbox.grid(row = 9, column = 1)
		PVARPE_spinbox.grid(row = 9, column = 2)
		ATRFM_spinbox.grid(row = 9, column = 3)
		ATRD_spinbox.grid(row = 11, column = 0)
		ATRFT_spinbox.grid(row = 11, column = 1)
		VB_spinbox.grid(row = 11, column = 2)
		AT_spinbox.grid(row = 11, column = 3)
		RT_spinbox.grid(row = 13, column = 0)
		RF_spinbox.grid(row = 13, column = 1)
		RecT_spinbox.grid(row = 13, column = 2)

		# Creating padding for spinboxes
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

		special_character = False

		#Check for special characters in username
		for character in username_input:
			if (not character.isalnum()):
				special_character = True

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
					#test case if username already exists
					if username_input in pre_r:
						flag = 1
						messagebox.showerror('Error', "Unfortunately your account was not created. The provided username already exists.")
					elif special_character == True:
						flag = 1
						messagebox.showerror('Error',"Please make sure to only include alphabetical or numerical characters.")
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

		#rewrite textfile if empty
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

	#setting up interface of password confirm
	password_confirm = Entry(frame, width = 25, fg = 'black', border = 0, bg = 'white', font=('Helvetica 11 bold'))
	password_confirm.place(x = 30, y = 220)
	password_confirm.insert(0, 'Confirm Password*')
	password_confirm.bind("<FocusIn>", pass_in)
	password_confirm.bind("<FocusOut>", pass_out)
	Frame(frame, width = 295, height = 2, bg = 'black').place(x = 25, y = 247)

	#Sign up/login buttons in registration
	myButton1 = Button(frame, width = 39, pady = 7, text = 'Sign up', bg = 'pink', fg = 'black', border = 0, font = 'Helvetica 9 bold', command = sign_up).place(x = 35, y = 260)
	myButton2 = Button(frame, width = 6, text = 'Login', border = 0, bg = 'orange', cursor = 'hand2', fg = 'black', font=('Helvetica 9 bold'), command = sign_in).place(x = 300, y = 0)

	window.mainloop()

##############################################################################################



#"sign in" and "create account" button in welcome screen
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

#green bar
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

def close_serial(serie):
	serie.close()

root.mainloop()